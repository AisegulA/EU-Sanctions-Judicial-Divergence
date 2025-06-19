# EU-Sanctions-Judicial-Divergence
## 📂 Dataset Access

The full dataset (37 PDF court decisions coded in this study) is publicly available here:

🔗 [Download Dataset on Google Drive]([https://drive.google.com/your-dataset-link-here](https://drive.google.com/file/d/1nairb-awAwHWnudowWA5qiDzOQqVFZpe/view?usp=sharing))

The dataset includes:
- 15 decisions from the Court of Justice of the European Union (CJEU)
- 22 decisions from four Member States: France, Germany, Italy, and the Netherlands

Each judgment has been manually annotated based on four core legal principles:
- **Proportionality** (Explicit / Shallow / Absent)
- **Judicial Review** (Strong / Weak / Absent)
- **CJEU Reference** (Positive / Distinguish / Absent)
- **National Doctrine** (Active / Passive / Not Invoked)

├── data/
│   ├── CJEU/                      # 15 Court of Justice of the EU (CJEU) decisions in PDF format
│   ├── France/                    # French national court decisions
│   ├── Germany/                   # German national court decisions
│   ├── Italy/                     # Italian national court decisions
│   └── Netherlands/               # Dutch national court decisions
│
├── coding/
│   ├── coding_scheme.csv          # Legal principle coding categories (Figure 1)
│   ├── final_coding_matrix.csv    # All 37 decisions with coded legal features
│   └── case_list.xlsx             # Metadata for each case (court, date, country, etc.)
│
├── scripts/
│   ├── text_processing.py         # Natural Language Processing (NLP) pipeline using SpaCy
│   └── plot_figures.py            # Python code to generate figures (heatmaps, line plots, bar charts)
│
├── figures/
│   ├── figure1_coding_scheme.png
│   ├── figure2_heatmap.png
│   ├── figure3_country_density.png
│   └── figure4_term_frequency.png
│
├── LICENSE
└── README.md

📂 Explore the dataset and figures: [Data Branch](https://github.com/AisegulA/EU-Sanctions-Judicial-Divergence/tree/Data)

