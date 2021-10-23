# Kaggle ML/DS Survey

### Data Overview
* [Exploratory Data Analysis](notebooks/exploratory-data-analysis.md)
* Data Dictionary: Response Table
  - Duration in seconds
  - TODO: Fill in rest

* Column Types: Questions table
  - Regular question/response (e.g. Q25 "What is your current yearly compensation (approximate $USD)?")
  - Multiple Response (e.g. Q7_Part_N: "What programming languages do you use on a regular basis? (Select all that apply) - Selected Choice - {response here}")
  - TODO: clean this up

### Research Questions
* Do some clustering to find different types of use cases
* Figure out what kinds of machine learning people reported (cluster into groups)
* Q42: Which media sources have which types of above categories? (are there any differences?)
* TODO: Brainstorm some more

### Project Organization
(realize this is overkill for this kind of analysis, but practicing my personal discipline of data science / analytics project organization)

* data
  - raw: original, immutable data files
  - interim: intermediate data that has been transformed
  - processed
* models
* notebooks
* reference
* reports
* src
  - contents within a language folder
    - data: scripts to download or generate data
    - features: scripts to turn raw data into features for modeling
    - models: scripts to train models and then use trained models to make predictions
    - visualization: scripts to create exploratory and results-oriented visualizations
  - language-specific folder (practicing translating between all 3, so there may be some duplication)
    - R
    - Python
    - SQL

### Overview
Kaggle Competition: [2021 Kaggle Machine Learning & Data Science Survey](https://www.kaggle.com/c/kaggle-survey-2021/overview)

> In our fifth year running this survey, we were once again awed by the global, diverse, and dynamic nature of the data science and machine learning industry. This survey data EDA provides an overview of the industry on an aggregate scale, but it also leaves us wanting to know more about the many specific communities comprised within the survey. For that reason, we’re inviting the Kaggle community to dive deep into the survey datasets and help us tell the diverse stories of data scientists from around the world.

> The challenge objective: tell a data story about a subset of the data science community represented in this survey, through a combination of both narrative text and data exploration. A “story” could be defined any number of ways, and that’s deliberate. The challenge is to deeply explore (through data) the impact, priorities, or concerns of a specific group of data science and machine learning practitioners. That group can be defined in the macro (for example: anyone who does most of their coding in Python) or the micro (for example: female data science students studying machine learning in masters programs). This is an opportunity to be creative and tell the story of a community you identify with or are passionate about!
