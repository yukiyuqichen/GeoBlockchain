# GeoBlockchainResearch

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2409.00843-B31B1B.svg)](https://arxiv.org/abs/2409.00843)
[![KNIME Tutorial](https://img.shields.io/badge/KNIME-Tutorial-yellow)](https://github.com/Yifanli1103/Geospatial-Map---KNIME)


---

This repository provides complementary open data and code resources for the paper **"Global Public Sentiment on Decentralized Finance: A Spatiotemporal Analysis of Geo-tagged Tweets from 150 Countries"**, available on [arXiv](https://arxiv.org/abs/2409.00843). The resources in this repository are designed to assist researchers and practitioners in exploring the intersection of blockchain technology, geospatial data science, economic growth, global imbalances, and public sentiment analysis on social media.

In the digital era, decentralized technologies such as blockchain, cryptocurrencies, and NFTs have significantly reshaped global financial systems. However, understanding the spatiotemporal variations in public sentiment towards these innovations remains an underexplored area. This study addresses this gap by analyzing over 150 million geo-tagged tweets from 150 countries between 2012 and 2022. Key findings include:

- **Sentiment Analysis**: Sentiment scores were derived using a BERT-based multilingual sentiment model trained on 7.4 billion tweets.
- **Economic Factors**: Significant variations in sentiment were found to be influenced by national economic factors. More developed countries engage more in decentralized finance discussions, while less developed nations exhibit stronger sentiment levels.
- **Geographically Weighted Regression**: Analysis shows that the correlation between GDP and tweet engagement intensifies following Bitcoin price surges.
- **Topic Modeling**: Countries within similar economic clusters tend to share common themes in decentralized finance discussions, while different clusters focus on distinct topics.
- **Implications**: The study’s results have implications for poverty alleviation, cryptocurrency crime, and sustainable development.

This repository provides access to the dataset, code, and analysis used in the study, offering a rich foundation for further exploration into the role of decentralized finance in shaping global economic and regional trends.

--- 

## Overview

The materials in this repository are designed to replicate and expand upon the findings from the associated research paper. They include:

- **Open Data Sources**: Access to geo-tagged tweet data and other relevant datasets used to analyze global public sentiment on decentralized finance.
- **Code**: Scripts and Jupyter Notebooks for replicating key experiments and spatiotemporal analyses, including geospatial sentiment analysis, geographically weighted regression, and topic analysis.
- **Additional Resources**: Links to tools and tutorials for exploring non-code-based data science workflows, such as KNIME, to facilitate analysis for users from diverse technical backgrounds.


## Repository Structure

```
GeoBlockchainResearch/
│
├── data/                   # Datasets used in the research.
│   └── sample_data.csv      # Sample geospatial dataset.
│
├── notebooks/               # Jupyter Notebooks for experiments.
│   └── geo_blockchain.ipynb  # Main analysis notebook.
│
├── src/                     # Source code.
│   └── data_processing.py   # Data preprocessing scripts.
│
├── results/                 # Results generated from analysis.
│   └── blockchain_maps.png  # Geospatial maps with blockchain data overlay.
│
├── LICENSE                  # MIT License.
└── README.md                # This README file.
```

## How to Use

### Prerequisites

To replicate the results, you will need:

- Python 3.x
- Required Python libraries (install using `requirements.txt`)
- Access to the datasets provided in the `data/` folder or linked external resources.

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sunshineluyao/GeoBlockchainResearch.git
   cd GeoBlockchainResearch
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jupyter Notebooks:**
   Open the provided Jupyter Notebooks in the `notebooks/` directory for a step-by-step guide to the experiments.

4. **Explore Source Code:**
   The source code in the `src/` folder includes data processing and blockchain integration scripts that can be adapted for other datasets and geospatial use cases.

## Non-Code Workflow Tutorial

For those interested in a non-code approach to replicating the results, a detailed tutorial using **KNIME** is available [here](https://github.com/Yifanli1103/Geospatial-Map---KNIME). KNIME is a no-code data science platform that enables workflow-based geospatial analysis and data visualization.

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or collaborations, please contact the corresponding author via:lz183@duke.edu


```


![Public attention toward DeFi across countries](https://github.com/yukiyuqichen/GeoBlockchain/raw/main/figures/spatial/maps/proportion_of_tweets_containing_any_keyword.png)
<p align="center">Public attention toward DeFi across countries</p>
<br>
<br>

![Public sentiment toward DeFi across countries](https://github.com/yukiyuqichen/GeoBlockchain/raw/main/figures/spatial/maps/sentiment_score_of_tweets_with_any_keyword.png)
<p align="center">Public sentiment toward DeFi across countries</p>
