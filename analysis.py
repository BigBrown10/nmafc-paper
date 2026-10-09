"""Recompute every number that appears in the paper from the per-question data.

Standard library only. Run it from this folder:

    python analysis.py

Each row of data/locomo_all.json holds one question, the gold answer, and both
arms' predictions from the same benchmarking window against the same persisted
stores. That pairing is what licenses McNemar's exact test: the arms agree on
most questions, and the disagreements carry the whole signal.
"""

from __future__ import annotations

import json
import math
import pathlib
import re
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).parent
DATA = HERE / "data"

SCORED = ("single-hop", "temporal", "multi-hop", "open-domain")
CHARS_PER_TOKEN = 4

# The rule that decides whether a prediction counts as declining to answer.
# It is stated here rather than described in prose because the measured rate
# depends almost entirely on what the rule counts: the same phenomenon reads
# as 3.6% under a narrow rule and 16.6% under this one. Read the predictions
# it selects before quoting any number that comes out of it.
DECLINE = re.compile(
    r"no (information|mention|record|relevant)"
    r"|not (mentioned|available|specified|stated|provided|found|in the)"
    r"|does not (have|appear|mention)"
    r"|cannot (be )?(determin|answer|find)"
    r"|unknown|unclear|no facts",
    re.I,
)


def mcnemar_exact(rows, a: str, b: str) -> tuple[int, int, float]:
    """Two-sided exact binomial test on the discordant pairs only."""
    only_a = sum(1 for r in rows if r[a] and not r[b])
    only_b = sum(1 for r in rows if r[b] and not r[a])
    n = only_a + only_b
    if n == 0:
        return only_a, only_b, 1.0
    lo = min(only_a, only_b)
    tail = sum(math.comb(n, k) for k in range(lo + 1))
    return only_a, only_b, min(1.0, 2 * tail / 2 ** n)


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson interval, which behaves near 0 and 1 where Wald does not."""
    if n == 0:
        return 0.0, 0.0
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (centre - half), 100 * (centre + half)


def pct(rows, key: str) -> float:
    return sum(r[key] for r in rows) / len(rows) * 100


def tok(rows, key: str) -> float:
    return sum(r[key] for r in rows) / len(rows) / CHARS_PER_TOKEN


def quantile(values: list[float], q: float) -> float:
    """Nearest-rank percentile on the sorted sample."""
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, math.ceil(q * len(ordered)) - 1))
    return ordered[idx]


def words(text: str) -> list[str]:
    """One tokeniser, shared with make_figures.py so the table in the
    paper and the figure beside it cannot disagree."""
    return re.findall(r"[a-z0-9']+", (str(text) or "").lower())


def token_f1(pred: str, gold: str) -> float:
    """Token-overlap F1, the SQuAD measure, with no model in the loop."""
    p, g = words(pred), words(gold)
    if not p or not g:
        return 0.0
    overlap = sum((Counter(p) & Counter(g)).values())
    if not overlap:
        return 0.0
    precision, recall = overlap / len(p), overlap / len(g)
    return 2 * precision * recall / (precision + recall)


def load(name: str) -> list[dict]:
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


def head_to_head(label: str, rows, a_ok, b_ok, a_ch, b_ch) -> None:
    won, lost, p = mcnemar_exact(rows, a_ok, b_ok)
    ka = sum(r[a_ok] for r in rows)
    kb = sum(r[b_ok] for r in rows)
    la, ha = wilson(ka, len(rows))
    lb, hb = wilson(kb, len(rows))
    print(f"  {label:<14} n={len(rows):<5} "
          f"{pct(rows, a_ok):5.1f}% [{la:4.1f},{ha:4.1f}]  "
          f"{pct(rows, b_ok):5.1f}% [{lb:4.1f},{hb:4.1f}]  "
          f"{pct(rows, a_ok) - pct(rows, b_ok):+5.1f}  "
          f"+{won}/-{lost:<4} p={p:<10.3g} "
          f"{tok(rows, a_ch):5.0f}t vs {tok(rows, b_ch):5.0f}t")


def main() -> None:
    rows = load("locomo_all")
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_cat[row["category"]].append(row)

    print(f"\n== Table 2: paired LoCoMo, {len(rows)} questions ==")
    print(f"  {'category':<14} {'n':<7} {'ours (95% CI)':<22} "
          f"{'RAG (95% CI)':<22} {'lead':<7} {'discord':<10} "
          f"{'McNemar':<12} context")
    for category in SCORED:
        head_to_head(category, by_cat[category],
                     "ours_ok", "rag_ok", "ours_chars", "rag_chars")
    head_to_head("adversarial", by_cat["adversarial"],
                 "ours_ok", "rag_ok", "ours_chars", "rag_chars")
    print()
    head_to_head("SCORED (4)", [r for r in rows if r["category"] in SCORED],
                 "ours_ok", "rag_ok", "ours_chars", "rag_chars")
    head_to_head("ALL (5)", rows,
                 "ours_ok", "rag_ok", "ours_chars", "rag_chars")

    print("\n== Table 3: agreement structure ==")
    for name, subset in [("SCORED (4)",
                          [r for r in rows if r["category"] in SCORED]),
                         ("ALL (5)", rows)]:
        both = sum(1 for r in rows
                   if r in subset and r["ours_ok"] and r["rag_ok"])
        neither = sum(1 for r in subset
                      if not r["ours_ok"] and not r["rag_ok"])
        won, lost, _ = mcnemar_exact(subset, "ours_ok", "rag_ok")
        print(f"  {name:<12} both={both:<5} neither={neither:<5} "
              f"ours only={won:<5} RAG only={lost:<5} "
              f"agreement={100 * (both + neither) / len(subset):.1f}%")

    print("\n== Section 5.3: the shape of the adversarial loss ==")
    adv = by_cat["adversarial"]
    d_ours = sum(1 for r in adv if DECLINE.search(str(r["ours_pred"])))
    d_rag = sum(1 for r in adv if DECLINE.search(str(r["rag_pred"])))
    print(f"  decline rate over {len(adv)} adversarial questions: "
          f"ours {100 * d_ours / len(adv):.1f}%  "
          f"RAG {100 * d_rag / len(adv):.1f}%")
    lost = [r for r in adv if r["rag_ok"] and not r["ours_ok"]]
    declined = [r for r in lost if DECLINE.search(str(r["ours_pred"]))]
    answered = [r for r in lost if r not in declined]
    print(f"  of {len(lost)} questions lost, {len(declined)} are our arm "
          f"declining and {len(answered)} are it answering differently")
    print("  on those {n}, token F1 against the gold: ours {a:.3f}  "
          "RAG {b:.3f}".format(
              n=len(answered),
              a=sum(token_f1(r["ours_pred"], r["gold"])
                    for r in answered) / len(answered),
              b=sum(token_f1(r["rag_pred"], r["gold"])
                    for r in answered) / len(answered)))

    print("\n== Table 3b: the lead by gold-answer length ==")
    bins = [("1 to 2", 1, 2), ("3 to 4", 3, 4),
            ("5 to 8", 5, 8), ("9 or more", 9, 10 ** 6)]
    for label, low, high in bins:
        for name, pool in [("all 5", rows),
                           ("scored 4",
                            [r for r in rows
                             if r["category"] in SCORED])]:
            subset = [r for r in pool
                      if low <= len(words(r["gold"])) <= high]
            won, lost, p = mcnemar_exact(subset, "ours_ok", "rag_ok")
            print(f"  {label:<10} {name:<9} n={len(subset):<5} "
                  f"{pct(subset, 'ours_ok') - pct(subset, 'rag_ok'):+5.1f}  "
                  f"+{won}/-{lost:<4} p={p:.3g}")
    print("  inside the adversarial category alone:")
    for label, low, high in (bins[0], bins[-1]):
        subset = [r for r in by_cat["adversarial"]
                  if low <= len(words(r["gold"])) <= high]
        print(f"    {label:<10} n={len(subset):<5} "
              f"ours {pct(subset, 'ours_ok'):.1f}%  "
              f"RAG {pct(subset, 'rag_ok'):.1f}%")

    print("\n== Figure 6b: mean token F1 against the gold ==")
    def mean_f1(subset, key: str) -> float:
        return sum(token_f1(r[key], r["gold"]) for r in subset) / len(subset)

    for category in SCORED + ("adversarial",):
        subset = by_cat[category]
        print(f"  {category:<14} ours {mean_f1(subset, 'ours_pred'):.3f}"
              f"   RAG {mean_f1(subset, 'rag_pred'):.3f}")

    print("\n== Table 8 (Appendix A): by conversation ==")
    by_conv: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_conv[row["conv"]].append(row)
    for conv in sorted(by_conv):
        head_to_head(conv, by_conv[conv],
                     "ours_ok", "rag_ok", "ours_chars", "rag_chars")

    print("\n== Table 4: latency, milliseconds ==")
    print(f"  {'arm':<6} {'p50':>8} {'p75':>8} {'p90':>8} {'p99':>8} "
          f"{'max':>8} {'mean':>8}")
    for arm, key in [("ours", "ours_ms"), ("RAG", "rag_ms")]:
        vals = [r[key] for r in rows if r.get(key)]
        print(f"  {arm:<6} " + " ".join(
            f"{quantile(vals, q):8.0f}" for q in (0.5, 0.75, 0.9, 0.99, 1.0))
            + f" {sum(vals) / len(vals):8.0f}")

    print("\n== Table 5: open-domain retrieval width, paired ==")
    ship = {r["question"]: r for r in load("od_ship")}
    for name in ("od_ship", "od_ground", "od_wide"):
        arm = load(name)
        pairs = [{"a": r["ok"], "b": ship[r["question"]]["ok"],
                  "ac": r["chars"], "bc": ship[r["question"]]["chars"]}
                 for r in arm if r["question"] in ship]
        won, lost, p = mcnemar_exact(pairs, "a", "b")
        print(f"  {name:<12} n={len(pairs):<5} {pct(pairs, 'a'):5.1f}%  "
              f"vs shipped {pct(pairs, 'b'):5.1f}%  "
              f"{pct(pairs, 'a') - pct(pairs, 'b'):+5.1f}  "
              f"+{won}/-{lost:<4} p={p:<8.3g} {tok(pairs, 'ac'):5.0f}t")
    rag = load("od_ship")
    print(f"  {'RAG':<12} n={len(rag):<5} {pct(rag, 'rag_ok'):5.1f}%"
          f"{'':<22}{'':<16} {tok(rag, 'rag_chars'):5.0f}t")

    print("\n== Table 6: the list-shape gate, paired ==")
    lgs = {r["question"]: r for r in load("lg_ship")}
    wide = load("lg_wide")
    pairs = [{"a": r["ok"], "b": lgs[r["question"]]["ok"],
              "ac": r["chars"], "bc": lgs[r["question"]]["chars"]}
             for r in wide if r["question"] in lgs]
    won, lost, p = mcnemar_exact(pairs, "a", "b")
    print(f"  wide vs shipped  n={len(pairs)}  {pct(pairs, 'a'):.1f}% vs "
          f"{pct(pairs, 'b'):.1f}%  {pct(pairs, 'a') - pct(pairs, 'b'):+.1f}  "
          f"+{won}/-{lost}  p={p:.3g}  "
          f"{tok(pairs, 'ac'):.0f}t vs {tok(pairs, 'bc'):.0f}t")

    print("\n== Table 7: answer-shape clauses in the prompt, paired ==")
    for name in ("commit_short_all", "commit_exact"):
        arm = load(name)
        cats: dict[str, list[dict]] = defaultdict(list)
        for r in arm:
            cats[r["category"]].append(r)
        won, lost, p = mcnemar_exact(arm, "ok", "shipped_ok")
        print(f"  {name}: n={len(arm)} {pct(arm, 'ok'):.1f}% vs shipped "
              f"{pct(arm, 'shipped_ok'):.1f}%  "
              f"{pct(arm, 'ok') - pct(arm, 'shipped_ok'):+.1f}  "
              f"+{won}/-{lost}  p={p:.3g}")
        for c in ("adversarial", "temporal", "single-hop", "multi-hop",
                  "open-domain"):
            if not cats[c]:
                continue
            w, l, pp = mcnemar_exact(cats[c], "ok", "shipped_ok")
            print(f"      {c:<13} n={len(cats[c]):<5} "
                  f"{pct(cats[c], 'ok') - pct(cats[c], 'shipped_ok'):+5.1f}  "
                  f"+{w}/-{l:<4} p={pp:.3g}")

    print("\n== Minimum detectable effect, two-sided alpha=0.05 ==")
    for n in (108, 214, 322, 830, 1539, 1985):
        # Normal approximation to McNemar with a 25% discordance rate.
        d = 0.25 * n
        mde = 1.96 * math.sqrt(d) / n * 100
        print(f"  n={n:<6} discordant~{d:.0f}  smallest detectable "
              f"lead ~{mde:.1f} points")
    print()


if __name__ == "__main__":
    main()
