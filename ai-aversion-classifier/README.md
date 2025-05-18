# AI Aversion Classifier – Predicting Negative Attitudes Toward Artificial Intelligence

This project required me to investigate whether it is feasible to identify individuals who are averse to AI without directly asking them about their attitudes toward AI.

The scenario assumed I had been approached by the UK government, which planned to run focus groups with individuals who hold negative views of AI. The government wished to avoid asking questions about AI directly in order to reduce bias or overly specific associations (e.g., with companies like OpenAI or technologies like ChatGPT). Instead, I was tasked with developing a predictive model using existing survey data.

### Task Overview

- I used the **2019 and 2017 Oxford Internet Survey (OxIS)** dataset, which contains extensive information on individuals' online behaviours, internet attitudes, and demographic features.
- My goal was to predict AI aversion based on indirect indicators available in the survey.
- The report answers the central question:  
  > “Is it feasible to identify AI-averse individuals, without directly asking about their attitudes to this technology?”

### Approach

- Explored and cleaned the OxIS 2019 dataset.
- Selected features relevant to digital behaviour, trust, privacy concerns, and tech attitudes.
- Trained a machine learning model (Decision Trees) to classify individuals as potentially AI-averse.
- Evaluated performance using accuracy, precision, and recall, while considering fairness and interpretability.

### Submission Format

- The final output was submitted as an **HTML report**

### Technologies Used

- **R** for data analysis and modeling
- **RMarkdown** for report generation
- **tidymodels**, **ggplot2**, and **dplyr** for modeling and visualization

---

