# ONGOING Masters Dissertation – Gendered Media Narratives: A Computational Analysis of Media and Public Discourse on Male and Female Musical Artists

This project investigates how gendered narratives in music journalism influence and are reflected in public discourse. The dissertation employs computational methods to analyse differences in the media portrayal of male and female music celebrities and examines how these narratives are received and reproduced by the public, particularly through Reddit discussions.

### Status
- This project is still ongoing and will be completed August 15,2025.
- Currently, I have run a topic model on data from the past year and am working on fine-tuning an LLM to categorise my texts.

### Project Summary

Research Questions:

- How do media portrayals of successful male and female music celebrities differ in language, tone, and framing?
- To what extent does public discourse on platforms like Reddit reflect, reinforce, or resist these narratives?
- Is there a directional relationship between media narratives and public sentiment?

### Methodology

- **Quantitative Analysis:** Topic modelling (LDA), sentiment analysis using BERT, and stance detection to identify gendered patterns in media and Reddit content.
- **Qualitative Analysis:** Manual discourse analysis of Reddit threads to validate and enrich computational findings.
- **Data Sources:** 
  - GDELT News API for news sources (e.g., Billboard, The Guardian, Rolling Stone)
  - Reddit threads discussing selected media headlines
- **Artist Sample:** 100 top male and female artists from the Billboard Top 100 (2021–2024)

### Technologies Used

- **Python** (with libraries such as `pandas`, `scikit-learn`, `transformers`, `gensim`)
- **Reddit API** for data scraping
- **BeautifulSoup** / **newspaper3k** for article scraping
- **BERT** for contextual sentiment analysis
- **LDA** for topic modelling
