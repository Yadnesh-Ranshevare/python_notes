# content
1. [Introduction](#introduction)
2. [Data Analytic/Science process flow](#data-analyticscience-process-flow)

---

# Introduction

- EDA means Exploratory Data Analysis.

- EDA is an approach to analyze the datasets to summarize their main characteristic in form of visual methods

- EDA is nothing more than a data exploration technique to understand various aspect ot the data

- It is the process of analyzing and visualizing a dataset before applying any machine learning or statistical methods.

- The goal is to understand the data better, find patterns, detect mistakes, check assumptions, and decide the right approach for further analysis.

- EDA give a basic idea to understanding the data nd make sense of the data 
- EDA helps us to find error, mapping out data  structure, fining anomalies, etc 



- It usually includes:
    - Checking the shape of the dataset (rows, columns).
    - Looking at data types (numbers, text, dates).
    - Summarizing with mean, median, min, max.
    - Visualizing distributions (histogram, boxplot).
    - Checking relationships between variables (scatter plots, correlation heatmaps).
    - Finding missing values or outliers.

### Importance of EDA
1. **Understand your data**
    - EDA helps you know what kind of data you have (numbers, categories, missing values, outliers).
    - Example: You see that some students have exam_score = 0 because they were absent → important insight.
2. **Detect mistakes early**
    - Raw data often has errors (wrong values, duplicates, impossible entries).
    - Example: A student with 120% attendance → clearly a mistake, found during EDA.
3. **Choose the right model**
    - By checking distributions and relationships, you know whether the problem is regression, classification, or clustering.
    - Example: If target is Pass/Fail, you’ll use classification, not regression.
4. **Guide feature engineering**
    - EDA shows which features matter most.
    - Example: You find that hours_studied has a stronger correlation with exam_score than age.
5. **Better decision-making**
    - Helps explain insights to non-technical people through simple graphs.
    - Example: A scatter plot shows more study hours = higher marks → easy for teachers to understand.


[Got To Top](#content)

---

# Data Analytic/Science process flow
It shows the step-by-step journey of data from the real world to decision-making using data science techniques.

![Image](./Images/DataScienceProcess.png)

#### 1. Real World
- Data science starts with a real-world problem (e.g., predicting student performance, detecting fraud, or recommending products).

#### 2. Raw Data Collection
- Collect data from different sources (databases, sensors, websites, surveys, etc.).
- At this stage, the data is usually messy and unorganized.
#### 3. Data Processing
- Convert raw data into a usable format.
- Example: converting text to numbers, handling date-time formats, merging data from multiple sources

#### 4. Data Cleaning
- Fix or remove incorrect, incomplete, or duplicate data.
- Example: handling missing values, correcting errors, removing outliers.
#### 5. Exploratory Data Analysis (EDA)
- Analyze and visualize the cleaned data to understand patterns, distributions, correlations, and trends.
- Helps in deciding which features are important for the model.
#### 6. Modeling
- Apply machine learning or statistical models to the data.
- Example: training a regression model, classification, or clustering.
#### 7. Visualization and Reporting
- Present results with charts, graphs, and dashboards so decision-makers can understand.
- Example: sales growth trend visualization.

#### 8. Deployment
- Deploy the model into the real world (e.g., a website, app, or automated system).
- Example: a recommendation system in an e-commerce website.
#### 9. Decision Making
- Business or users take actions based on insights and predictions from the model.
- Example: adjusting marketing strategy based on customer prediction.
#### 10. Back to Real World
- Once deployed, the system continues to interact with the real world, collecting new data → process repeats.


[Got To Top](#content)

---