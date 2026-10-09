"""The bibliography, as data.

Every entry here was resolved against Crossref by DOI content negotiation, or
against the arXiv API by identifier, on 10 September 2026. Nothing was written
from memory. The build script turns this dictionary into refs.bib for the LaTeX
build and into Harvard reference entries for the Markdown and Word renderings,
so the two can never disagree about who wrote what.

Items with `preprint: True` are labelled as such in the rendered list, with the
repository and the date the version cited was posted, because a reader has to
be able to tell refereed work from work that has not been refereed.
"""

from __future__ import annotations

# Field meanings follow BibTeX. `authors` is a list of (family, given) pairs
# exactly as the registry returned them.
REFERENCES: dict[str, dict] = {
    "maharana2024": {
        "type": "inproceedings",
        "authors": [("Maharana", "Adyasha"), ("Lee", "Dong-Ho"),
                    ("Tulyakov", "Sergey"), ("Bansal", "Mohit"),
                    ("Barbieri", "Francesco"), ("Fang", "Yuwei")],
        "year": 2024,
        "title": "Evaluating very long-term conversational memory of "
                 "LLM agents",
        "booktitle": "Proceedings of the 62nd Annual Meeting of the "
                     "Association for Computational Linguistics "
                     "(Volume 1: Long Papers)",
        "pages": "13851--13870",
        "publisher": "Association for Computational Linguistics",
        "doi": "10.18653/v1/2024.acl-long.747",
    },
    "lewis2020": {
        "type": "inproceedings",
        "authors": [("Lewis", "Patrick"), ("Perez", "Ethan"),
                    ("Piktus", "Aleksandra"), ("Petroni", "Fabio"),
                    ("Karpukhin", "Vladimir"), ("Goyal", "Naman"),
                    ("Kuttler", "Heinrich"), ("Lewis", "Mike"),
                    ("Yih", "Wen-tau"), ("Rocktaschel", "Tim"),
                    ("Riedel", "Sebastian"), ("Kiela", "Douwe")],
        "year": 2020,
        "title": "Retrieval-augmented generation for knowledge-intensive "
                 "NLP tasks",
        "booktitle": "Advances in Neural Information Processing Systems 33",
        "publisher": "Curran Associates",
        "eprint": "2005.11401",
    },
    "karpukhin2020": {
        "type": "inproceedings",
        "authors": [("Karpukhin", "Vladimir"), ("Oguz", "Barlas"),
                    ("Min", "Sewon"), ("Lewis", "Patrick"),
                    ("Wu", "Ledell"), ("Edunov", "Sergey"),
                    ("Chen", "Danqi"), ("Yih", "Wen-tau")],
        "year": 2020,
        "title": "Dense passage retrieval for open-domain question answering",
        "booktitle": "Proceedings of the 2020 Conference on Empirical "
                     "Methods in Natural Language Processing (EMNLP)",
        "pages": "6769--6781",
        "publisher": "Association for Computational Linguistics",
        "doi": "10.18653/v1/2020.emnlp-main.550",
    },
    "robertson2009": {
        "type": "article",
        "authors": [("Robertson", "Stephen"), ("Zaragoza", "Hugo")],
        "year": 2009,
        "title": "The probabilistic relevance framework: BM25 and beyond",
        "journal": "Foundations and Trends in Information Retrieval",
        "volume": "3", "number": "4", "pages": "333--389",
        "doi": "10.1561/1500000019",
    },
    "cormack2009": {
        "type": "inproceedings",
        "authors": [("Cormack", "Gordon V."), ("Clarke", "Charles L. A."),
                    ("Buettcher", "Stefan")],
        "year": 2009,
        "title": "Reciprocal rank fusion outperforms Condorcet and "
                 "individual rank learning methods",
        "booktitle": "Proceedings of the 32nd International ACM SIGIR "
                     "Conference on Research and Development in "
                     "Information Retrieval",
        "pages": "758--759", "publisher": "ACM",
        "doi": "10.1145/1571941.1572114",
    },
    "reimers2019": {
        "type": "inproceedings",
        "authors": [("Reimers", "Nils"), ("Gurevych", "Iryna")],
        "year": 2019,
        "title": "Sentence-BERT: sentence embeddings using Siamese "
                 "BERT-networks",
        "booktitle": "Proceedings of the 2019 Conference on Empirical "
                     "Methods in Natural Language Processing and the 9th "
                     "International Joint Conference on Natural Language "
                     "Processing (EMNLP-IJCNLP)",
        "pages": "3980--3990",
        "publisher": "Association for Computational Linguistics",
        "doi": "10.18653/v1/D19-1410",
    },
    "malkov2020": {
        "type": "article",
        "authors": [("Malkov", "Yu A."), ("Yashunin", "D. A.")],
        "year": 2020,
        "title": "Efficient and robust approximate nearest neighbor search "
                 "using hierarchical navigable small world graphs",
        "journal": "IEEE Transactions on Pattern Analysis and Machine "
                   "Intelligence",
        "volume": "42", "number": "4", "pages": "824--836",
        "doi": "10.1109/TPAMI.2018.2889473",
    },
    "johnson2021": {
        "type": "article",
        "authors": [("Johnson", "Jeff"), ("Douze", "Matthijs"),
                    ("Jegou", "Herve")],
        "year": 2021,
        "title": "Billion-scale similarity search with GPUs",
        "journal": "IEEE Transactions on Big Data",
        "volume": "7", "number": "3", "pages": "535--547",
        "doi": "10.1109/TBDATA.2019.2921572",
    },
    "liu2024": {
        "type": "article",
        "authors": [("Liu", "Nelson F."), ("Lin", "Kevin"),
                    ("Hewitt", "John"), ("Paranjape", "Ashwin"),
                    ("Bevilacqua", "Michele"), ("Petroni", "Fabio"),
                    ("Liang", "Percy")],
        "year": 2024,
        "title": "Lost in the middle: how language models use long contexts",
        "journal": "Transactions of the Association for Computational "
                   "Linguistics",
        "volume": "12", "pages": "157--173",
        "doi": "10.1162/tacl_a_00638",
    },
    "cuconasu2024": {
        "type": "inproceedings",
        "authors": [("Cuconasu", "Florin"), ("Trappolini", "Giovanni"),
                    ("Siciliano", "Federico"), ("Filice", "Simone"),
                    ("Campagnano", "Cesare"), ("Maarek", "Yoelle"),
                    ("Tonellotto", "Nicola"), ("Silvestri", "Fabrizio")],
        "year": 2024,
        "title": "The power of noise: redefining retrieval for RAG systems",
        "booktitle": "Proceedings of the 47th International ACM SIGIR "
                     "Conference on Research and Development in "
                     "Information Retrieval",
        "pages": "719--729", "publisher": "ACM",
        "doi": "10.1145/3626772.3657834",
    },
    "huang2025": {
        "type": "article",
        "authors": [("Huang", "Lei"), ("Yu", "Weijiang"), ("Ma", "Weitao"),
                    ("Zhong", "Weihong"), ("Feng", "Zhangyin"),
                    ("Wang", "Haotian"), ("Chen", "Qianglong"),
                    ("Peng", "Weihua"), ("Feng", "Xiaocheng"),
                    ("Qin", "Bing"), ("Liu", "Ting")],
        "year": 2025,
        "title": "A survey on hallucination in large language models: "
                 "principles, taxonomy, challenges, and open questions",
        "journal": "ACM Transactions on Information Systems",
        "volume": "43", "number": "2", "pages": "1--55",
        "doi": "10.1145/3703155",
    },
    "zhong2024": {
        "type": "inproceedings",
        "authors": [("Zhong", "Wanjun"), ("Guo", "Lianghong"),
                    ("Gao", "Qiqi"), ("Ye", "He"), ("Wang", "Yanlin")],
        "year": 2024,
        "title": "MemoryBank: enhancing large language models with "
                 "long-term memory",
        "booktitle": "Proceedings of the AAAI Conference on Artificial "
                     "Intelligence",
        "volume": "38", "number": "17", "pages": "19724--19731",
        "doi": "10.1609/aaai.v38i17.29946",
    },
    "zheng2023": {
        "type": "inproceedings",
        "authors": [("Zheng", "Lianmin"), ("Chiang", "Wei-Lin"),
                    ("Sheng", "Ying"), ("Zhuang", "Siyuan"),
                    ("Wu", "Zhanghao"), ("Zhuang", "Yonghao"),
                    ("Lin", "Zi"), ("Li", "Zhuohan"), ("Li", "Dacheng"),
                    ("Xing", "Eric P."), ("Zhang", "Hao"),
                    ("Gonzalez", "Joseph E."), ("Stoica", "Ion")],
        "year": 2023,
        "title": "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena",
        "booktitle": "Advances in Neural Information Processing Systems 36",
        "publisher": "Curran Associates",
        "eprint": "2306.05685",
    },
    "rajpurkar2016": {
        "type": "inproceedings",
        "authors": [("Rajpurkar", "Pranav"), ("Zhang", "Jian"),
                    ("Lopyrev", "Konstantin"), ("Liang", "Percy")],
        "year": 2016,
        "title": "SQuAD: 100,000+ questions for machine comprehension "
                 "of text",
        "booktitle": "Proceedings of the 2016 Conference on Empirical "
                     "Methods in Natural Language Processing",
        "pages": "2383--2392",
        "publisher": "Association for Computational Linguistics",
        "doi": "10.18653/v1/D16-1264",
    },
    "mcnemar1947": {
        "type": "article",
        "authors": [("McNemar", "Quinn")],
        "year": 1947,
        "title": "Note on the sampling error of the difference between "
                 "correlated proportions or percentages",
        "journal": "Psychometrika",
        "volume": "12", "number": "2", "pages": "153--157",
        "doi": "10.1007/BF02295996",
    },
    "wilson1927": {
        "type": "article",
        "authors": [("Wilson", "Edwin B.")],
        "year": 1927,
        "title": "Probable inference, the law of succession, and "
                 "statistical inference",
        "journal": "Journal of the American Statistical Association",
        "volume": "22", "number": "158", "pages": "209--212",
        "doi": "10.1080/01621459.1927.10502953",
    },
    "dietterich1998": {
        "type": "article",
        "authors": [("Dietterich", "Thomas G.")],
        "year": 1998,
        "title": "Approximate statistical tests for comparing supervised "
                 "classification learning algorithms",
        "journal": "Neural Computation",
        "volume": "10", "number": "7", "pages": "1895--1923",
        "doi": "10.1162/089976698300017197",
    },
    "bliss1973": {
        "type": "article",
        "authors": [("Bliss", "T. V. P."), ("Lømo", "T.")],
        "year": 1973,
        "title": "Long-lasting potentiation of synaptic transmission in "
                 "the dentate area of the anaesthetized rabbit following "
                 "stimulation of the perforant path",
        "journal": "The Journal of Physiology",
        "volume": "232", "number": "2", "pages": "331--356",
        "doi": "10.1113/jphysiol.1973.sp010273",
    },
    "murre2015": {
        "type": "article",
        "authors": [("Murre", "Jaap M. J."), ("Dros", "Joeri")],
        "year": 2015,
        "title": "Replication and analysis of Ebbinghaus' forgetting curve",
        "journal": "PLOS ONE",
        "volume": "10", "number": "7", "pages": "e0120644",
        "doi": "10.1371/journal.pone.0120644",
    },
    "squire2015": {
        "type": "article",
        "authors": [("Squire", "Larry R."), ("Genzel", "Lisa"),
                    ("Wixted", "John T."), ("Morris", "Richard G.")],
        "year": 2015,
        "title": "Memory consolidation",
        "journal": "Cold Spring Harbor Perspectives in Biology",
        "volume": "7", "number": "8", "pages": "a021766",
        "doi": "10.1101/cshperspect.a021766",
    },
    "collins1975": {
        "type": "article",
        "authors": [("Collins", "Allan M."), ("Loftus", "Elizabeth F.")],
        "year": 1975,
        "title": "A spreading-activation theory of semantic processing",
        "journal": "Psychological Review",
        "volume": "82", "number": "6", "pages": "407--428",
        "doi": "10.1037/0033-295X.82.6.407",
    },
    "anderson1983": {
        "type": "article",
        "authors": [("Anderson", "John R.")],
        "year": 1983,
        "title": "A spreading activation theory of memory",
        "journal": "Journal of Verbal Learning and Verbal Behavior",
        "volume": "22", "number": "3", "pages": "261--295",
        "doi": "10.1016/S0022-5371(83)90201-3",
    },
    "mccloskey1989": {
        "type": "incollection",
        "authors": [("McCloskey", "Michael"), ("Cohen", "Neal J.")],
        "year": 1989,
        "title": "Catastrophic interference in connectionist networks: "
                 "the sequential learning problem",
        "booktitle": "Psychology of Learning and Motivation, Volume 24",
        "pages": "109--165", "publisher": "Elsevier",
        "doi": "10.1016/S0079-7421(08)60536-8",
    },
    "kirkpatrick2017": {
        "type": "article",
        "authors": [("Kirkpatrick", "James"), ("Pascanu", "Razvan"),
                    ("Rabinowitz", "Neil"), ("Veness", "Joel"),
                    ("Desjardins", "Guillaume"), ("Rusu", "Andrei A."),
                    ("Milan", "Kieran"), ("Quan", "John"),
                    ("Ramalho", "Tiago"), ("Grabska-Barwinska", "A."),
                    ("Hassabis", "Demis"), ("Clopath", "Claudia"),
                    ("Kumaran", "Dharshan"), ("Hadsell", "Raia")],
        "year": 2017,
        "title": "Overcoming catastrophic forgetting in neural networks",
        "journal": "Proceedings of the National Academy of Sciences",
        "volume": "114", "number": "13", "pages": "3521--3526",
        "doi": "10.1073/pnas.1611835114",
    },
    "tulving1985": {
        "type": "article",
        "authors": [("Tulving", "Endel")],
        "year": 1985,
        "title": "Memory and consciousness",
        "journal": "Canadian Psychology",
        "volume": "26", "number": "1", "pages": "1--12",
        "doi": "10.1037/h0080017",
    },
    "lin2026": {
        "type": "article",
        "authors": [("Lin", "Y. J."), ("Takahashi-Nakazato", "A."),
                    ("Tsutsumi", "K."), ("Takahashi", "T."),
                    ("Mercier", "D."), ("Ashitomi", "H.")],
        "etal": True,
        "year": 2026,
        "title": "Artificial hibernation reveals synaptic engram "
                 "architecture associated with memory retention",
        "journal": "Science",
        "volume": "393", "number": "6812",
        "doi": "10.1126/science.aee7004",
    },
    "packer2023": {
        "type": "preprint",
        "authors": [("Packer", "Charles"), ("Wooders", "Sarah"),
                    ("Lin", "Kevin"), ("Fang", "Vivian"),
                    ("Patil", "Shishir G."), ("Stoica", "Ion"),
                    ("Gonzalez", "Joseph E.")],
        "year": 2023,
        "title": "MemGPT: towards LLMs as operating systems",
        "eprint": "2310.08560", "archive": "arXiv",
        "posted": "12 October 2023",
    },
    "rasmussen2025": {
        "type": "preprint",
        "authors": [("Rasmussen", "Preston"), ("Paliychuk", "Pavlo"),
                    ("Beauvais", "Travis"), ("Ryan", "Jack"),
                    ("Chalef", "Daniel")],
        "year": 2025,
        "title": "Zep: a temporal knowledge graph architecture for "
                 "agent memory",
        "eprint": "2501.13956", "archive": "arXiv",
        "posted": "20 January 2025",
    },
    "wu2024": {
        "type": "preprint",
        "authors": [("Wu", "Di"), ("Wang", "Hongwei"), ("Yu", "Wenhao"),
                    ("Zhang", "Yuwei"), ("Chang", "Kai-Wei"),
                    ("Yu", "Dong")],
        "year": 2024,
        "title": "LongMemEval: benchmarking chat assistants on long-term "
                 "interactive memory",
        "eprint": "2410.10813", "archive": "arXiv",
        "posted": "14 October 2024",
    },
    "xu2025": {
        "type": "preprint",
        "authors": [("Xu", "Wujiang"), ("Liang", "Zujie"), ("Mei", "Kai"),
                    ("Gao", "Hang"), ("Tan", "Juntao"),
                    ("Zhang", "Yongfeng")],
        "year": 2025,
        "title": "A-MEM: agentic memory for LLM agents",
        "eprint": "2502.12110", "archive": "arXiv",
        "posted": "17 February 2025",
    },
    "chhikara2025": {
        "type": "preprint",
        "authors": [("Chhikara", "Prateek"), ("Khant", "Dev"),
                    ("Aryan", "Saket"), ("Singh", "Taranjeet"),
                    ("Yadav", "Deshraj")],
        "year": 2025,
        "title": "Mem0: building production-ready AI agents with scalable "
                 "long-term memory",
        "eprint": "2504.19413", "archive": "arXiv",
        "posted": "28 April 2025",
    },
}
