# content
1. [Introduction](#introduction)
2. [Data Analytic/Science process flow](#data-analyticscience-process-flow)
3. [Visualization](#visualization)
4. [Data Cleaning](#data-cleaning-1)
    - [How to handle missing values?](#handling-missing-values)
    - [Feature Scaling](#feature-scaling)
    - [feature scaling techniques](#feature-scaling-techniques)
    - [Outlier Treatment](#outlier-treatment)
    - [handling invalid Values](#handling-invalid-values)
5. Type of Analysis
    - [Univariate Analysis](#univariate-analysis)

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
# Visualization

**Visualization is the presentation of the data in a graphical or visual form to understand the data more clearly.**


### Advantages of Visualization
- Helps understand data easily
- Shows patterns and trends clearly
- Detects outliers and unusual values
- Reveals relationships between variables
- Helps find missing or wrong data
- Aids in feature selection (choosing useful columns)
- Makes results easy to explain and present
- Guides next analysis steps based on insights


### Common Visualization Types in EDA


| Visualization Type | Use Case                                         | Example (Python code with `matplotlib` / `seaborn`)  |
| ------------------ | ------------------------------------------------ | ---------------------------------------------------- |
| **Histogram**      | See how a single numeric variable is distributed | `sns.histplot(data['age'], bins=10)`                 |
| **Box Plot**       | Identify outliers and data spread                | `sns.boxplot(x=data['salary'])`                      |
| **Scatter Plot**   | Check relationship between two numeric variables | `sns.scatterplot(x='height', y='weight', data=data)` |
| **Bar Plot**       | Compare categories                               | `sns.barplot(x='gender', y='income', data=data)`     |
| **Heatmap**        | Visualize correlation between multiple variables | `sns.heatmap(data.corr(), annot=True)`               |
| **Pair Plot**      | View all pairwise relationships                  | `sns.pairplot(data)`                                 |




[Got To Top](#content)

---

# Data Cleaning
- data cleaning means that you get rid of only information that doesn't need to be there
- it generally perform to improve the quality of the data for future data analysis operation and building a machine learning model  
- the benefit of data cleaning is that all the incorrect and irrelevant data is gone, and we get the good quality of data which will help in improving the accuracy of our machine learning model

### major steps of data cleaning
- **Remove Duplicates:** Delete repeated or identical rows from the dataset.
- **Handle Missing Values:** Fill missing data with mean, median, or mode, or remove rows/columns with too many missing values.
- **Fix Data Types:** Convert columns to correct data types (e.g., integer, float, date).
- **Detect and Handle Outliers:** Identify and remove or adjust extreme or unusual values.
- **Standardize Data Formats:** Make sure formats are consistent (e.g., “Yes/No” instead of “Y/N”).
- **Correct Inconsistent or Invalid Data:** Fix spelling mistakes, invalid entries, or incorrect labels.
- **Remove Irrelevant Data:** Drop unnecessary or unhelpful columns and rows.
- **Normalize or Scale Data:** Adjust numeric values to a common scale to improve model performance.

### Handling Missing Values

> This will be a theory part and for learning how to implement this using python please check the following pages: 
>1. [detecting missing values using pandas](https://github.com/Yadnesh-Ranshevare/python_notes/blob/main/Pandas/readme.md#how-to-detect-the-missing-value-using-isnull)
>
>2. [handling missing values using pandas](https://github.com/Yadnesh-Ranshevare/python_notes/blob/main/Pandas/readme.md#handling-the-missing-data)

 

1. **Delete row / column:**
    - **Remove rows with missing values**\
Delete rows that contain missing values if they are few and random, so you don’t lose much information.\
Example: `data.dropna()`
    - **Remove columns with too many missing values**\
Drop a column if most of its data is missing, since it may not be useful.

2. **Fill another Value:**
    - **Fill numeric values with mean, median, or mode**\
Replace missing numeric data with the average, median, or most frequent value to maintain dataset size.\
Example: `data['age'].fillna(data['age'].mean())`
    - **Fill categorical values with mode or a constant**\
Replace missing categorical values with the most frequent category or a placeholder like `"Unknown"`.\
Example: `data['gender'].fillna("Unknown")`
    - **Forward fill / Backward fill**\
Fill missing values using previous or next row values, useful in time series data.\
Example: `data.fillna(method='ffill')`

3. **Interpreted:**
    - **Interpolation**\
Estimate missing values based on surrounding data points, useful for continuous variables.\
Example: `data['sales'].interpolate(method='linear')`
    - **Advanced imputation methods**\
Use machine learning or statistical models (like KNN Imputer or regression) to predict missing values based on other columns.

### Feature Scaling 
Feature Scaling is a process where we adjust the values of features (columns) so they are on a similar scale.

This is important because:
- Many machine learning algorithms work better or converge faster when features are on the same scale (e.g., algorithms using distances like KNN, SVM, or gradient descent methods).
- Without scaling, features with large values can dominate those with small values.

**Example**\
Imagine you have a dataset with two features:
| Height (cm) | Weight (kg) |
| ----------- | ----------- |
| 170         | 65          |
| 180         | 75          |
| 160         | 55          |

Here:
- Height values: 160–180 cm → numbers in the range of about hundreds
- Weight values: 55–75 kg → numbers in the range of tens

That means the scale of the two features is very different.

Some algorithms treat larger numbers as more important. So we scale them to a similar range.

Therefor we transform the features so they are on similar scales.

Using Min-Max Scaling

Formula:

$$
X' = \frac{X - X_{min}}{X_{max} - X_{min}}
$$

For Height:
- Min = 160, Max = 180
- Row 1:

$$
X' = \frac{170 - 160}{180 - 160} = \frac{10}{20} = 0.5
$$

- Row 2:

$$
X' = \frac{180 - 160}{180 - 160} = \frac{20}{20} = 1
$$

- Row 3:

$$
X' = \frac{160 - 160}{180 - 10} = 0
$$

For Weight:
- Min = 55, Max = 75
- Row 1:

$$
X' = \frac{65 - 55}{75 - 55} = \frac{10}{20} = 0.5
$$

- Row 2:

$$
X' = \frac{75 - 55}{75 - 55} = \frac{10}{20} = 1
$$

- Row 3:

$$
X' = \frac{55 - 55}{75 - 55} = \frac{10}{20} = 1
$$

Scaled Dataset
| Height_scaled | Weight_scaled |
| ------------- | ------------- |
| 0.5           | 0.5           |
| 1.0           | 1.0           |
| 0.0           | 0.0           |

Now both features are on the same scale 0–1. This ensures no single feature dominates the model’s decisions.


### feature scaling techniques
1. **Min-Max Scaling (Normalization)**
    - Formula:

    $$
    X' = \frac{X - X_{min}}{X_{max} - X_{min}}
    $$

    - Scales data to a fixed range (usually 0 to 1).
    - Use case: Useful when you want bounded data and your model needs normalized values (e.g., neural networks).
    - Downside: Sensitive to outliers.

2. **Standardization (Z-score Normalization)**

    - Formula:
    $$
    X' = \frac{X - \mu}{\sigma}
    $$

    where μ = mean, σ = standard deviation.
    - Scales data so it has a mean of 0 and standard deviation of 1.
    - Use case: Works well for most machine learning algorithms.
    - Downside: Doesn’t bound values to a specific range.

3. **Robust Scaling**
    - Formula:
    $$
    X' = \frac{X - median}{IQR}
    $$

    where IQR = Interquartile Range (Q3 − Q1).
    - Uses medians and IQR instead of mean and standard deviation.
    - Use case: Good for datasets with many outliers.
    - Downside: Doesn’t bound values.

4. **Max Abs Scaling**
    - Formula:

    $$
    X' = \frac{X}{|X_{max}|}
    $$
    - Scales data to [-1, 1] without shifting/centering.
    - Use case: Useful when your data is already centered at zero.
    - Downside: Sensitive to outliers.
5. **Unit Vector Scaling (Normalization by norm)**
    - Formula:

    $$
    X' = \frac{X}{||X||}
    $$

    where ∥X∥ is the vector norm (often L2 norm).
    - Scales data so that the length of the vector is 1.
    - Use case: Useful in text classification and clustering.
    - Downside: Doesn’t preserve original distribution.


### Outlier Treatment

- An outlier is a data point that is significantly different from the other values in a dataset — it either lies much higher or much lower than the rest.

**Example:**\
Data:\
`10, 12, 11, 13, 500`\
🔍 Here, `500` is an outlier because it’s far away from the other values.
 

 - An outlier can pull the mean toward itself, especially if the dataset is small.


**How outlier affect mean**\
**Example:**\
Data without outlier:\
`10, 12, 14, 16, 18`

**Mean = (10 + 12 + 14 + 16 + 18) / 5 = 70 / 5 = `14`**

Now add an outlier → 100:\
`10, 12, 14, 16, 18, 100`

**Mean = (10 + 12 + 14 + 16 + 18 + 100) / 6 = 170 / 6 ≈ `28.3`**

👉 The mean jumped from **14 to 28.3** — just because of one outlier!

**Methods to Detect Outliers**
- Z-Score Method: Calculates how many standard deviations a data point is from the mean. Data points with a Z-score greater than 3 (or less than -3) are typically considered outliers. Formula: 
$ Z = \frac{x - \mu}{\sigma} $, where  x = data point, μ = mean, σ = standard deviation\
[Click here to learn more about removing outlier using Z-score method](https://github.com/Yadnesh-Ranshevare/python_notes/blob/main/Statistics/Readme.md#detecting-and-removing-outlier)

- Interquartile Range (IQR) Method: Outliers are points that fall below $Q1 - 1.5 \times IQR$ or above $Q1 + 1.5 \times IQR$, where Q1 and Q3 are the 1st and 3rd quartiles, respectively, and $IQR = Q3 - Q1$

- Visualization Techniques: Box plots, histograms, and scatter plots help visually identify outliers as points far from the cluster of data. In box plots, data points outside the whiskers are potential outliers.

- Clustering and Density Methods: Techniques such as DBSCAN and Isolation Forest can detect outliers by analyzing data density and isolation in high-dimensional spaces.

- Other Statistical Tests: Sorting, Z-score, and IQR methods are often supported by statistical tests for more formal verification.

### handling invalid Values
In a dataset, invalid values are entries that don’t make logical sense or don’t fit the expected format/range.

Examples:
- A person’s age = -5 (invalid)
- A salary = "abc" when it should be numeric
- A date = 32/13/2025 (invalid date)
- Gender = "Dog" (not part of valid categories)

Invalid values can mislead your analysis, so handling them properly is essential.

**Steps to Handle Invalid Values in EDA**
1. Identify invalid values
    - Use `.info()`, `.describe()`, `.unique()`, or visualization to spot strange values.
    - Example: age = -5, salary = "abc", date = "32/13/2025".
2. Understand data context
    - Know what counts as valid or invalid.
    - Example: valid age range = 0–100, salary > 0.
    - Sometimes, “invalid” values carry meaning (like -1 for “unknown”).

3. Detect invalid values using conditions
```py
df[df['age'] < 0]
df[df['salary'] == 'abc']
```
4. Decide how to handle them
    - Remove invalid rows → when they’re few and clearly wrong.
    - Replace with NaN → when you’ll handle them later.
    - Impute (fill) → use mean/median/mode or domain knowledge.


[Got To Top](#content)

---
# Univariate Analysis

Univariate Analysis means analyzing one variable (column) at a time in your dataset.

- **“Uni”** = one
- **“Variate”** = variable

You do it to understand the distribution, patterns, and summary statistics of that single variable.

### Purpose
To understand:
- The central tendency (mean, median, mode)
- The spread (range, variance, standard deviation)
- The shape (skewness, outliers, distribution type)

### Types of Univariate Analysis
1. **For Numerical Data**
    - Use:
        - `mean`, `median`, `mode`
        - `min`, `max`, `std`, `quantiles`
    - Visualizations
        - Histogram
        - Box plot
        - Density plot
2. **For Categorical Data**
    - Use:
        - `value_counts()`
        - `countplot` (bar chart)

### Why It’s Important
Univariate analysis is the first step in EDA — it helps you:
- Detect outliers or invalid values
- Understand data distribution
- Choose suitable data transformations
- Prepare for bivariate or multivariate analysis


### Example Dataset
| Name  | Age | Gender |
| ----- | --- | ------ |
| Alex  | 22  | Male   |
| Priya | 25  | Female |
| John  | 30  | Male   |
| Aisha | 28  | Female |
| Ravi  | 22  | Male   |

#### Univariate Analysis on “Age” (Numerical Variable)

We analyze only the Age column.

- **Central tendency**:\
The average (mean) age is around 25 years.

- **Spread**:\
The minimum age is 22, and the maximum is 30 — so the data is not very spread out.

- **Distribution shape**:\
Most people are in their 20s, so the data is slightly concentrated around the mid-20s.

- **Outliers**:\
No extremely high or low ages — so no outliers.

**Conclusion:** The age data is fairly consistent and centered around 25.

#### Univariate Analysis on “Gender” (Categorical Variable)
We now look only at the Gender column.

- **Frequency**:\
There are 3 Males and 2 Females.

- **Pattern**:\
Males are slightly more common in this dataset.

**Conclusion**: The dataset has a higher number of males compared to females.

[Got To Top](#content)

---