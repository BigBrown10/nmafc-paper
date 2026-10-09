# NMAFC paper

A peer-review submission comparing a compacting two-tier conversational memory
against retrieval-augmented generation on LoCoMo, with both arms answering the
same 1,985 questions in one benchmarking window.

`paper.md` is the only place the prose lives. Everything else is generated
from it or feeds into it.

## What is here

| File | What it is |
|---|---|
| `paper.md` | the source. Edit this and nothing else |
| `references.py` | the bibliography as data, one entry per source |
| `build.py` | renders the source to LaTeX, Word and Markdown |
| `analysis.py` | recomputes every number in every table |
| `make_figures.py` | redraws every figure |
| `data/` | the per-question predictions of both arms |
| `figures/` | each figure as PDF for LaTeX and PNG for Word |
| `main.tex` | generated. Upload this to Overleaf |
| `refs.bib` | generated. Not needed for the Overleaf build |
| `NMAFC-paper.docx` | generated. Word, for tracked-changes review |
| `paper-rendered.md` | generated. Reading copy with numbers filled in |

## Rebuilding

```
python make_figures.py     # only when a figure changes
python build.py            # after any edit to paper.md
```

`build.py` needs `python-docx` and `matplotlib`. `analysis.py` and the
numbers it prints need neither, only the standard library. Nothing here
contacts a model or needs an API key.

The build reports the running-text word count on its own, split into body and
appendix. Table cells, captions and the reference list are left out of it,
because they are what turns a 7,000 word paper into an alarming 8,000 word
one without a word of prose being added.

The body is sized to the eight pages an ACL or EMNLP submission allows, under
which references and appendices are unlimited and do not count. Two figures
and two tables sit in the body and everything else is in an appendix, chosen
on one test: a float stays in the body only if it shows something no body
table already shows. The accuracy-by-category figure went to the appendix
because Table 1 carries every number in it.

The build assigns figure, table and equation numbers from the order the
blocks appear in `paper.md`, resolves every cross-reference against those
numbers, and stops with an error on an unresolved reference or an unknown
citation key. It also prints how many references were cited and names any
that were not, so an entry cannot sit unused in the bibliography.

## Producing the PDF

There is no LaTeX installation on this machine, so the PDF is made on
Overleaf.

1. Start a blank Overleaf project.
2. Upload `main.tex` and the whole `figures` folder, keeping the folder name.
3. Set the compiler to pdfLaTeX.
4. Compile once. The bibliography is written into `main.tex` as a
   `thebibliography` block, so there is no bibtex pass and no `.bst` file to
   go missing.

The layout is two columns at 10pt on A4. The title and the abstract span the
width above the columns. Every figure spans both columns, because each one is
a strip of panels around twice as wide as it is tall, and so do the six
widest tables; the rest sit inside a single column. The float counters in the
preamble are loosened, since a spanning float can only be placed at the top
of a later page and the defaults run out of room with thirteen of them.

Page counts cannot be checked on this machine, since there is no LaTeX here.
The estimate comes from arithmetic in column-inches: a page holds two columns
of 10.13in, a line of prose in a 3.205in column holds about eight words at
12pt leading, so a full page of pure prose is about 970 words. Each spanning
float costs twice its own height, and the figure heights are read from the
MediaBox of the PDFs rather than guessed. On that basis the body runs to
roughly 7.7 pages. Only an Overleaf compile settles it.

`refs.bib` is there for a journal that asks for a BibTeX file. It carries the
same entries from the same source, so it cannot disagree with the rendered
list.

## Editing conventions

Figures, tables and display equations are fenced blocks:

```
::: figure id=accuracy src=figures/fig2_accuracy_by_category
The caption goes here, as one or more sentences.
:::

::: table id=main
The caption goes here.

| a | b |
|---|---|
| 1 | 2 |
:::

::: equation id=decay
w(\Delta t) = w_0 e^{-\lambda \Delta t}
:::
```

Refer to them in the prose as `{@fig:accuracy}`, `{@tab:main}` and
`{@eq:decay}`. Write the word yourself, so `Figure {@fig:accuracy}`.

Cite with `[@key]` for a parenthetical citation and `[-@key]` for a narrative
one. Several keys in one bracket are separated by a semicolon:
`[@lewis2020; @karpukhin2020]`. The keys are the top-level names in
`references.py`.

Maths is LaTeX. Inline maths sits between single dollar signs and is
flattened to Unicode for the Word file; display maths is rendered to an image
for Word and typeset properly in the PDF. Use `\leq` rather than `\le`: the
Word renderer does not know the short form.

## House style

British spelling. Harvard referencing. Sentence case in headings. No em
dashes, no curly quotes, no bold inside body prose. Preprints carry
`preprint: True` in `references.py` and are labelled `[Preprint]` in the
rendered list with the repository and the date the cited version was posted,
so a reader can tell refereed work from work that has not been refereed.

Every claim about the system's own behaviour is supported by the released
data rather than by a citation. A source is cited for a method, a benchmark
or someone else's finding, never for a number this study measured.
