# content
1. [Introduction](#introduction)
2. [Data Analytic/Science process flow](#data-analyticscience-process-flow)
3. [Visualization](#visualization)
4. [Data Cleaning](#data-cleaning-1)
    - [How to handle missing values?](#handling-missing-values)
    - [Outlier Treatment](#outlier-treatment)
    - [handling invalid Values](#handling-invalid-values)
5. Type of Analysis
    - [Univariate Analysis](#univariate-analysis)
    - [Bivariate Analysis](#bivariate-analysis)
    - [Multivariate Analysis](#multivariate-analysis)
6. [Feature Engineering](#feature-engineering)
    - [Derived Matrix](#derived-matrix)
    - [Feature Binning](#feature-binning)
    - [Feature Scaling](#feature-scaling)
    - [Feature Transformation](#feature-transformation)
    - [Datetime Extraction](#datetime-extraction)
    - [Aggregation](#aggregation)
    - [Feature Interaction](#feature-interaction)
    - [Decomposition](#decomposition)
7. Implementation Of EDA
    - [Zomato Dataset](#implementation-of-eda-using-zomato-dataset)

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
# Bivariate Analysis 
Bivariate analysis means analyzing two variables together to understand the relationship between them.
- **“Bi”** → two
- **“Variate”** → variables

So basically, we’re exploring how one variable changes with respect to another.

It’s a key step in Exploratory Data Analysis (EDA) because it helps us go beyond individual variable descriptions (univariate analysis) and start exploring connections between variables.

It helps answer questions like:
- Does age affect income?
- Do males and females spend differently?
- Is there a link between education level and employment status?

### 3 Main Types

#### 1. Numerical vs Numerical
Both variables are numbers.\
We study whether they increase or decrease together — i.e., correlation.

**Example:**\
Let’s say we have this data:

| Person | Age | Salary (in ₹) |
| ------ | --- | ------------- |
| A      | 22  | 25,000        |
| B      | 25  | 30,000        |
| C      | 28  | 35,000        |
| D      | 35  | 60,000        |
| E      | 40  | 80,000        |

**Observation:**\
As age increases, salary also increases.\
→ This means there’s a positive correlation.

**Interpretation:**\
Older people tend to have more experience → higher salaries.\
Hence, Age and Salary are positively correlated.

In EDA, you’d visualize this with a scatter plot, where points form an upward trend.

#### 2. Categorical vs Numerical
One variable is category-based, the other is numeric.\
We study if the numeric values differ across categories.

**Example:**
| Gender | Monthly Spending (₹) |
| ------ | -------------------- |
| Male   | 3,000                |
| Male   | 3,500                |
| Female | 5,000                |
| Female | 4,800                |
| Female | 5,200                |

**Observation:**\
Average spending for females ≈ ₹5,000\
Average spending for males ≈ ₹3,250

**Interpretation:**\
Spending differs by gender → the categorical variable (Gender) influences the numerical variable (Spending).

In EDA, you’d show this with a box plot to compare the spending distribution between groups.


#### 3. Categorical vs Categorical
Both variables are categories.\
We check if they are dependent or independent.

**Example:**
| Gender | Purchased (Yes/No) |
| ------ | ------------------ |
| Male   | No                 |
| Female | Yes                |
| Female | Yes                |
| Male   | No                 |
| Female | Yes                |

**Observation (Counts):**
| Gender | Yes | No |
| ------ | --- | -- |
| Male   | 0   | 2  |
| Female | 3   | 0  |

**Interpretation:**\
Females purchased more than males → there’s a relationship between Gender and Purchase.

In EDA, you’d use a crosstab or stacked bar chart to show this.


### Objectives of Bivariate Analysis
1. **Identify Relationships:**\
To check if two variables are related (e.g., does height increase with weight?).
2. **Measure Strength and Direction:**\
If they are related, how strong is the relationship?\
And is it positive (both increase together) or negative (one increases, the other decreases)?
3. **Find Patterns or Trends:**\
Helps in spotting data patterns that can influence predictions or decisions.
4. **Detect Outliers or Anomalies:**\
Sometimes, the relationship reveals data points that don’t fit the general pattern.

[Got To Top](#content)

---
# Multivariate Analysis
Multivariate analysis means studying more than two variables at the same time to understand the relationships, interactions, and patterns among them.
- **“Multi”** → many
- **“Variate”** → variables

So while:
- Univariate analysis = 1 variable
- Bivariate analysis = 2 variables
- Multivariate analysis = 3 or more variables

### Why It’s Used in EDA
In real-world datasets, things are rarely controlled by just two factors.
For example:

- A person’s salary may depend on age, education level, and experience — not just one thing.
- A customer’s buying decision might depend on income, age, and gender.

Multivariate analysis helps us uncover these complex relationships that can’t be seen in simple pairwise comparisons.

### Goals of Multivariate Analysis
1. Understand interactions between multiple features.
2. Detect hidden patterns that appear only when multiple variables are considered together.
3. Reduce data dimensionality (i.e., summarize many variables into fewer key components).
4. Build predictive insights (which variable influences the outcome most).

### Example
Let’s say you have the following dataset:
| Person | Age | Education | Experience (Years) | Salary (₹) |
| ------ | --- | --------- | ------------------ | ---------- |
| A      | 22  | Graduate  | 1                  | 25,000     |
| B      | 25  | Graduate  | 3                  | 30,000     |
| C      | 28  | Postgrad  | 5                  | 35,000     |
| D      | 35  | Postgrad  | 8                  | 60,000     |
| E      | 40  | Doctorate | 12                 | 80,000     |

**What you can do:**
- **Univariate:** Look at salary distribution.
- **Bivariate:** Compare age vs salary.
- **Multivariate:** Study how age, education, and experience together affect salary.

**You might find:**
- Salary increases with both age and experience,
- But people with higher education earn more even with less experience.

That’s something you can only discover through multivariate analysis.


[Got To Top](#content)

---

# Feature Engineering
Feature Engineering means creating, transforming, or selecting features (columns) from raw data to make it more useful for analysis or machine learning models.

You can think of it as turning raw data into meaningful information that helps your model understand patterns better.

#### Why it’s needed
Raw data is often messy or not directly usable by ML models.
Feature Engineering helps by:
- Making the data more informative
- Reducing noise or irrelevant details
- Improving model accuracy and performance
#### Main Tasks in Feature Engineering
| Step                                            | Description                         | Example                                       |
| ----------------------------------------------- | ----------------------------------- | --------------------------------------------- |
| **1. Creating new features (Feature Creation)** | Combine or extract new columns      | `Total_Price = Quantity × Price`              |
| **2. Transforming features**                    | Apply math or logic transformations | `log(Salary)` to reduce skewness              |
| **3. Encoding categorical data**                | Convert text → numbers              | `City = {“Mumbai”, “Delhi”}` → One-Hot Encode |
| **4. Feature Scaling**                          | Normalize values to same range      | Use Min-Max or Standard scaling               |
| **5. Handling Outliers / Missing Data**         | Fix extreme or missing values       | Replace missing age with mean                 |
| **6. Feature Selection**                        | Keep only useful features           | Remove columns with low correlation           |

#### Simple Example

Suppose you have raw data:
| Name | Birth_Year | Height(cm) | Weight(kg) |
| ---- | ---------- | ---------- | ---------- |
| A    | 2000       | 170        | 60         |
| B    | 1995       | 180        | 85         |

After Feature Engineering, you could add:
| Age | BMI   |
| --- | ----- |
| 25  | 20.76 |
| 30  | 26.23 |

- Age = 2025 - Birth_Year
- BMI = Weight / (Height/100)^2

These new features (Age, BMI) help your model understand health patterns better.


**there are many other ways of doing Feature Engineering depending on your dataset type (numeric, categorical, text, or date).**

| **Category**        | **Example**                         | **What it Means (Simple)**                                           |
| ------------------- | ----------------------------------- | -------------------------------------------------------------------- |
| [Derived Matrix ](#derived-matrix)    | `BMI = Weight ÷ (Height × Height)`  | Make a new number from existing data that tells you something useful |
| [Feature Binning](#feature-binning)     | Ages → “Child”, “Adult”, “Senior”   | Group numbers into categories to make them easier to understand      |
| [Feature Encoding](#feature-encoding)            | “Male” → 0, “Female” → 1            | Change words into numbers so a computer can use them                 |
| [ Feature Scaling](#feature-scaling)             | Test scores 0–100 → 0–1             | Make numbers similar in size so one doesn’t overpower the others     |
| [Feature Transformation ](#feature-transformation)     | Use `log` or `sqrt`                 | Fix numbers that are too big or uneven to balance them               |
| [Datetime Extraction](#datetime-extraction) | “2025-10-11” → Month = 10, Day = 11 | Pull useful info like month or day from a date                       |
| [Aggregation](#aggregation)         | Average purchase per person         | Summarize many numbers into one to see overall patterns              |
| [Feature Interaction](#feature-interaction)         | `Total = Price × Quantity`          | Combine two numbers to show a relationship between them              |
| [Decomposition](#decomposition)       | PCA (reduce many columns to fewer)  | Make data smaller while keeping important info                       |
| Domain Features     | `Profit = Revenue − Cost`           | Use real-world rules to create numbers that make sense               |


[Got To Top](#content)

---

# Derived Matrix

A new matrix (or table of data) that is created by transforming or deriving new features/variables from an existing dataset.

A derived matrix is formed when you take your original dataset and add new columns or transform existing ones to create derived (calculated) variables.

So, it’s the “transformed” version of your data used for analysis or model building.

### Example
Let’s say you have this dataset (matrix):

| Age | Height (m) | Weight (kg) |
| --- | ---------- | ----------- |
| 20  | 1.75       | 70          |
| 25  | 1.68       | 60          |
| 30  | 1.80       | 90          |

Now, if you derive new features such as:
- BMI = Weight / Height²
- Age Group = "Young" if Age < 25 else "Adult"

You get this derived matrix:

| Age | Height | Weight | BMI  | Age Group |
| --- | ------ | ------ | ---- | --------- |
| 20  | 1.75   | 70     | 22.9 | Young     |
| 25  | 1.68   | 60     | 21.3 | Adult     |
| 30  | 1.80   | 90     | 27.8 | Adult     |

[Got To Top](#content)

---

# Feature Binning
Feature binning means dividing continuous numerical values into discrete intervals (bins) — basically grouping similar values together.

It helps simplify the data and reduce noise or outlier effects.

### Example
Say you have an Age column:
```
[15, 18, 22, 30, 35, 42, 50, 60, 70]
```
After binning, you could group it like this:
| Age | Age_Group           |
| --- | ------------------- |
| 15  | Teen (0–19)         |
| 18  | Teen (0–19)         |
| 22  | Young Adult (20–35) |
| 30  | Young Adult (20–35) |
| 42  | Adult (36–55)       |
| 60  | Senior (56–75)      |
| 70  | Senior (56–75)      |

Now instead of many distinct numeric values, you have fewer, meaningful categories.

### Why Do We Use Binning?
| Reason                       | Explanation                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| **Simplify Data**            | Makes continuous values easier to interpret                     |
| **Handle Noise**             | Small random fluctuations are absorbed into bins                |
| **Reduce Outlier Effect**    | Outliers don’t distort bins as much                             |
| **Improve Interpretability** | Easier for humans to understand (e.g., “Low”, “Medium”, “High”) |
| **Help Certain Models**      | Decision trees or Naive Bayes can benefit from categorical bins |

### Types of Binning
1. **Equal Width Binning**
    - Divide data into bins of equal size (range).
    - Example: If Age ranges from 0–100 and you want 5 bins → each bin = 20 years wide.
    ```
    [0–20), [20–40), [40–60), [60–80), [80–100)
    ```

2. **Equal Frequency Binning**
    - Each bin contains roughly the same number of observations.
    - Example: 1000 data points → 5 bins → each bin has 200 values.
    - This helps when data is skewed (unevenly distributed).
3. **Custom / Domain-based Binning**
    - Created using domain knowledge or business logic.
    - Example:
        - Income < 30K → “Low”
        - 30K–70K → “Medium”
        - 70K → “High”
    - This is the most meaningful type in real-world projects.


[Got To Top](#content)

---
# Feature Encoding

Feature Encoding is the process of converting categorical (non-numeric) data into numeric format so that machine learning models can understand it.
> Most ML models can’t work with text directly — they need numbers.\
> Feature Encoding is how we “translate” categories into numbers.

### Types of Feature Encoding
#### 1. Label Encoding
- Assigns a unique integer to each category.
- Useful for ordinal categories (where order matters).

**Example**:\
Imagine a dataset of fruits
| Fruit  | Color  |
| ------ | ------ |
| Apple  | Red    |
| Banana | Yellow |
| Orange | Orange |
| Apple  | Red    |


We just assign numbers:
- **Color**: Red = 0, Yellow = 1, Orange = 2
- **Fruit**: Apple = 0, Banana = 1, Orange = 2    

Now the table becomes:
| Fruit | Color |
| ----- | ----- |
| 0     | 0     |
| 1     | 1     |
| 2     | 2     |
| 0     | 0     |

#### 2. One-Hot Encoding
- Creates binary columns for each category.
- Used for nominal categories (no order).

**Example**:\
Imagine a dataset of fruits
| Fruit  | Color  |
| ------ | ------ |
| Apple  | Red    |
| Banana | Yellow |
| Orange | Orange |
| Apple  | Red    |

We create a column for each category and put 1 if it’s that category, 0 otherwise:
| Fruit_Apple | Fruit_Banana | Fruit_Orange | Color_Red | Color_Yellow | Color_Orange |
| ----------- | ------------ | ------------ | --------- | ------------ | ------------ |
| 1           | 0            | 0            | 1         | 0            | 0            |
| 0           | 1            | 0            | 0         | 1            | 0            |
| 0           | 0            | 1            | 0         | 0            | 1            |
| 1           | 0            | 0            | 1         | 0            | 0            |

#### 3. Ordinal Encoding
- Similar to Label Encoding, but you specifically define the order.

**Example**:\
Imagine a dataset of customer satisfaction survey:
| Customer | Satisfaction |
| -------- | ------------ |
| A        | Poor         |
| B        | Average      |
| C        | Excellent    |
| D        | Good         |
| E        | Poor         |

Satisfaction has a natural order:
`Poor < Average < Good < Excellent`

Therefor we assign numbers to reflect the order:
| Customer | Satisfaction | Ordinal Encoded |
| -------- | ------------ | --------------- |
| A        | Poor         | 0               |
| B        | Average      | 1               |
| D        | Good         | 2               |
| C        | Excellent    | 3               |
| E        | Poor         | 0               |


#### 4. Binary / Base-N Encoding (Optional Advanced)
- Converts categories to binary digits (like 0s and 1s).
- Useful when you have high-cardinality categorical data (many unique values).

**Example**:\
Imagine a fruit Category list
| Fruit  |
| ------ |
| Apple  |
| Banana |
| Orange |
| Mango  |

First, assign a number to each category:
| Fruit  | Number |
| ------ | ------ |
| Apple  | 0      |
| Banana | 1      |
| Orange | 2      |
| Mango  | 3      |

Then convert numbers to binary:
| Fruit  | Number | Binary (2-bit) |
| ------ | ------ | -------------- |
| Apple  | 0      | 00             |
| Banana | 1      | 01             |
| Orange | 2      | 10             |
| Mango  | 3      | 11             |

#### 5. Target / Mean Encoding (Advanced)
- Replace categories with average of target variable for that category.
- Useful for predictive models, especially categorical variables with many levels.

**Example**:\
 Predicting Loan Approval
 | Customer | Bank  | Loan Approved (Target) |
| -------- | ----- | ---------------------- |
| A        | SBI   | 1                      |
| B        | HDFC  | 0                      |
| C        | SBI   | 1                      |
| D        | ICICI | 0                      |
| E        | HDFC  | 1                      |

Target = Loan Approved (1 = Yes, 0 = No)

**Step 1: Compute mean target per category**
| Bank  | Avg Loan Approved |
| ----- | ----------------- |
| SBI   | (1+1)/2 = 1.0     |
| HDFC  | (0+1)/2 = 0.5     |
| ICICI | 0/1 = 0.0         |

**Step 2: Replace Bank column with mean target**

| Customer | Bank_Encoded | Loan Approved |
| -------- | ------------ | ------------- |
| A        | 1.0          | 1             |
| B        | 0.5          | 0             |
| C        | 1.0          | 1             |
| D        | 0.0          | 0             |
| E        | 0.5          | 1             |

Now the categorical column is numeric and contains information about the target, which can help the model predict better.

[Got To Top](#content)

---
# Feature Scaling 
Feature Scaling is a process where we adjust the values of features (columns) so they are on a similar scale.

This is important because:
- Many machine learning algorithms work better or converge faster when features are on the same scale (e.g., algorithms using distances like KNN, SVM, or gradient descent methods).
- Without scaling, features with large values can dominate those with small values.

### Example
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

Therefor we transform the features so they are on similar scales using Min-Max Scaling

### Formula:

$$
X' = \frac{X - X_{min}}{X_{max} - X_{min}}
$$

### For Height:
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

### For Weight:
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

### Scaled Dataset
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

    where $||X||$ is the vector norm (often L2 norm).
    - Scales data so that the length of the vector is 1.
    - Use case: Useful in text classification and clustering.
    - Downside: Doesn’t preserve original distribution.



[Got To Top](#content)

---

# Feature Transformation
Feature Transformation means changing the scale, shape, or distribution of your data features to make them more useful for a machine learning model.

It’s like “reshaping” the data so that algorithms can understand it better.

### Why do we use it?
- Some models (like Linear Regression, KNN, SVM) perform better when features are on the same scale
- Some features have skewed data, and transformation helps to make it normal-like
- It helps models learn patterns faster and more accurately

### Main Types of Feature Transformation
| Type                                     | Description                                                                                                                                            | Easy Example                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **1. Log Transformation**                | Used when numbers vary a lot (like income, sales). Makes large numbers smaller and easier to compare.                                                  | Suppose you have incomes: `[10,000, 100,000, 1,000,000]` → After `log(x)` → `[4, 5, 6]`                    |
| **2. Square Root / Cube Root**           | Works well for small positive numbers or count data. Reduces the gap between small and large numbers.                                                  | Visitors per day: `[1, 4, 9, 16]` → After `sqrt(x)` → `[1, 2, 3, 4]`                                       |
| **3. Box-Cox / Yeo-Johnson**             | Used when data is not normal (too skewed). These methods automatically find the best power (log, sqrt, etc.) to make it look more like a normal curve. | Suppose exam scores `[5, 10, 50, 90]` are uneven → After Box-Cox → `[1.2, 2.0, 4.5, 6.0]` (balanced range) |
| **4. Normalization (Min-Max Scaling)**   | Compresses all values into a 0–1 range. Keeps shape but changes scale.                                                                                 | Heights `[150, 160, 170, 180]` → After normalization → `[0.0, 0.33, 0.67, 1.0]`                            |
| **5. Standardization (Z-score Scaling)** | Centers data around mean 0 and standard deviation 1, useful when units differ.                                                                         | Test scores `[40, 50, 60]` → Mean = 50, Std = 10 → After scaling → `[-1, 0, 1]`                            |
| **6. Power Transformation**              | Raises numbers to a power (e.g. square or square root) to stabilize variance or highlight patterns.                                                    | Prices `[2, 3, 4]` → `x²` → `[4, 9, 16]` or `x⁰·⁵` → `[1.41, 1.73, 2.0]`                                   |


### Example
Suppose you have an “Income” column:
| Person | Income  |
| ------ | ------- |
| A      | 20,000  |
| B      | 60,000  |
| C      | 500,000 |

After Log Transformation:
| Person | log(Income) |
| ------ | ----------- |
| A      | 4.3         |
| B      | 4.8         |
| C      | 5.7         |

Now the differences between large and small values are reduced, making patterns easier for the model to learn.

### Feature Scaling vs Feature Transformation
These two terms are closely related, but not exactly the same.\
You can think of feature scaling as a part of feature transformation.

#### Feature Scaling
It’s about changing the scale or range of numeric data — nothing else.

**Goal:**\
Make sure all features are on a similar numeric range, so one doesn’t dominate the others.

**Common scaling methods:**
- Normalization (Min–Max scaling) → range [0,1]
- Standardization (Z-score scaling) → mean = 0, std = 1

**Example:**
| Feature     | Original      | After Scaling |
| ----------- | ------------- | ------------- |
| Height (cm) | 160, 170, 180 | 0.0, 0.5, 1.0 |

#### Feature Transformation
It’s a broader concept — includes scaling, but also covers methods that change data distribution or make patterns more visible to models.

**Goal:**\
Make data more useful for analysis or modeling.

**Includes:**
- Feature Scaling (Normalization, Standardization)
- Log / Sqrt / Cube root transformation
- Box-Cox, Yeo-Johnson transformation
- Polynomial transformation
- Encoding categorical features (sometimes also called transformation)


[Got To Top](#content)

---

# Datetime Extraction
Datetime extraction means taking useful parts (features) out of a date or time column — like year, month, day, hour, weekday, etc.

It helps the model understand time-related patterns that raw timestamps can’t show.

### Example Dataset

| Order_ID | Order_Date          |
| -------- | ------------------- |
| 101      | 2024-07-15 14:35:00 |
| 102      | 2024-07-16 09:12:00 |
| 103      | 2024-08-01 20:45:00 |

#### Step 1: Extract date parts
| Order_ID | Year | Month | Day | Hour | Weekday  |
| -------- | ---- | ----- | --- | ---- | -------- |
| 101      | 2024 | 7     | 15  | 14   | Monday   |
| 102      | 2024 | 7     | 16  | 9    | Tuesday  |
| 103      | 2024 | 8     | 1   | 20   | Thursday |

Now, you’ve turned one column into multiple features that the model can use!

### How it help in analysis?
| Extracted Feature        | How It Helps                                          |
| ------------------------ | ----------------------------------------------------- |
| **Year**                 | Detect trends over time (e.g., yearly sales growth)   |
| **Month**                | Find seasonal patterns (e.g., more sales in December) |
| **Day**                  | See daily activity patterns                           |
| **Hour**                 | Analyze busy hours (e.g., 9 AM peak orders)           |
| **Weekday / Weekend**    | Understand customer behavior (weekend vs weekday)     |
| **Is_Holiday / Quarter** | Capture special events or fiscal periods              |


### Python Example
```py
import pandas as pd

# Example data
df = pd.DataFrame({
    'Order_Date': ['2024-07-15 14:35:00', '2024-07-16 09:12:00', '2024-08-01 20:45:00']
})

# Convert to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Extract datetime features
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Day'] = df['Order_Date'].dt.day
df['Hour'] = df['Order_Date'].dt.hour
df['Weekday'] = df['Order_Date'].dt.day_name()

print(df)
```
**Output:**
| Order_Date          | Year | Month | Day | Hour | Weekday  |
| ------------------- | ---- | ----- | --- | ---- | -------- |
| 2024-07-15 14:35:00 | 2024 | 7     | 15  | 14   | Monday   |
| 2024-07-16 09:12:00 | 2024 | 7     | 16  | 9    | Tuesday  |
| 2024-08-01 20:45:00 | 2024 | 8     | 1   | 20   | Thursday |


[Got To Top](#content)

---
# Aggregation
Aggregation means combining multiple rows of data into a single value to create a new feature — usually by applying operations like:
- `sum()`
- `mean()`
- `count()`
- `max()`
- `min()`
- `std()` (standard deviation)

In simple terms:\
You summarize detailed data to get useful insights or features.

### Real-Life Example: E-commerce Orders
Suppose you have a dataset of customer orders:
| Customer_ID | Order_ID | Amount |
| ----------- | -------- | ------ |
| 101         | O1       | 200    |
| 101         | O2       | 300    |
| 102         | O3       | 150    |
| 102         | O4       | 100    |
| 103         | O5       | 400    |

#### Step 1: Aggregate by Customer
We can group by `Customer_ID` and calculate useful stats:
| Customer_ID | Total_Spent | Avg_Order_Value | Order_Count |
| ----------- | ----------- | --------------- | ----------- |
| 101         | 500         | 250             | 2           |
| 102         | 250         | 125             | 2           |
| 103         | 400         | 400             | 1           |

Now you’ve created new features that represent each customer’s behavior.

### Why It’s Useful

- Models can now understand how valuable or active a customer is.
- Reduces large, repetitive data (many rows → 1 summary row per entity).
- Often used for customer analytics, sales forecasting, fraud detection, etc.


[Got To Top](#content)

---
# Feature Interaction
Feature Interaction means combining two or more existing features to create a new feature that captures their relationship or combined effect on the target variable.

In short:\
You create a new column that represents how two features work together.


### Why It’s Useful

Sometimes, two features individually might not affect the output much —
but together they have a strong influence.

**Example:**

- “Salary” alone and “Age” alone may not predict spending habits accurately,
- But “Salary × Age” might show that older people with higher salaries spend more.

### Types of Feature Interaction

#### 1. Mathematical Combination
Combine numeric features using arithmetic operations:

- Addition (+)
- Subtraction (−)
- Multiplication (×)
- Division (÷)

**Example:**
| Height (cm) | Weight (kg) | BMI = Weight / (Height/100)² |
| ----------- | ----------- | ---------------------------- |
| 160         | 50          | 19.5                         |
| 170         | 65          | 22.5                         |
| 180         | 80          | 24.7                         |

Here, BMI is a feature interaction created from height & weight.

#### 2. Categorical Combination
Combine categories to form new hybrid features.
| City   | Product | Combined_Feature |
| ------ | ------- | ---------------- |
| Mumbai | Shoes   | Mumbai_Shoes     |
| Delhi  | Shoes   | Delhi_Shoes      |
| Mumbai | Watch   | Mumbai_Watch     |

This helps models learn city-specific product patterns.

#### 3. Polynomial Features (Advanced)
Polynomial Features are new features created by raising existing features to powers or multiplying them together to capture non-linear relationships between variables.

**Example:**\
Let’s say you have one feature:
```
x = [1, 2, 3]
```
If you apply polynomial features of degree 2, it will create:
```
x^1 = [1, 2, 3]
x^2 = [1, 4, 9]
```
So now your dataset becomes:
| x | x² |
| - | -- |
| 1 | 1  |
| 2 | 4  |
| 3 | 9  |

**Why?**\
Because maybe the relation between your target (say, price) and feature (size) isn’t straight-line but curved — polynomial features help the model learn that curve.


[Got To Top](#content)

---
# Decomposition
Decomposition means breaking down complex data (especially time-series or high-dimensional data) into simpler, more meaningful components.

Think of it like taking apart a machine to understand how each piece works individually.

### Two Main Types of Decomposition

#### 1. Time-Series Decomposition
Used when your data changes over time (like sales, temperature, traffic, etc.)

**Example:**\
Let’s say you have monthly sales data for a shop for 2 years:
| Month    | Sales |
| -------- | ----- |
| Jan 2023 | 100   |
| Feb 2023 | 120   |
| Mar 2023 | 150   |
| Apr 2023 | 130   |
| May 2023 | 170   |
| Jun 2023 | 160   |
| Jul 2023 | 180   |
| Aug 2023 | 190   |
| Sep 2023 | 210   |
| Oct 2023 | 230   |
| Nov 2023 | 260   |
| Dec 2023 | 300   |
| ...      | ...   |

**Step 1 — Trend**

- Sales are gradually increasing over months — that’s your trend.\
➡️ Example: A smooth line going up from 100 → 300
- Trend feature:\
`trend = [100, 110, 120, 130, 150, ... 300]`

**Step 2 — Seasonality**
- Maybe every December sales spike because of festive shopping.\
➡️ That repeating pattern each year = seasonality
- Seasonal feature:\
`seasonality = [−20, −10, +15, ... , +40]`

**Step 3 — Residual / Noise**
- Small, random fluctuations (like a sudden dip due to bad weather or a one-day sale)\
➡️ These are the residuals
- Residual feature:\
`residual = [5, −10, +7, ...]`

**And we can even create new columns like:**
| Month    | Trend | Seasonality | Residual |
| -------- | ----- | ----------- | -------- |
| Jan 2023 | 100   | −20         | 5        |
| Feb 2023 | 110   | −10         | −10      |
| ...      | ...   | ...         | ...      |

These new features can help an ML model predict future sales more accurately.


#### 2. Feature Decomposition for High-Dimensional Data
Used when you have many correlated features, like in images, text, or sensors.

We use mathematical decomposition techniques such as:
| Technique                              | Purpose                                                                             | Example                               |
| -------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------- |
| **PCA (Principal Component Analysis)** | Reduce many correlated features into a few main ones while keeping most information | 100 features → 3 principal components |
| **SVD (Singular Value Decomposition)** | Similar to PCA, used in text (like NLP) and recommendation systems                  | Used in Netflix movie recommendation  |
| **LDA (Linear Discriminant Analysis)** | Finds combinations of features that separate classes well                           | Used in face recognition              |


**Example of Feature Decomposition (PCA Example)**\
Now imagine you have a dataset of students with these features:
| Student | Height (cm) | Weight (kg) | BMI  | Chest Size (cm) | Arm Size (cm) |
| ------- | ----------- | ----------- | ---- | --------------- | ------------- |
| A       | 160         | 60          | 23.4 | 85              | 28            |
| B       | 170         | 75          | 25.9 | 92              | 31            |
| C       | 180         | 90          | 27.8 | 98              | 34            |
| D       | 165         | 65          | 23.9 | 88              | 29            |

You can see — most features are correlated (taller → heavier → bigger chest).\
Too many similar features can confuse the model.

PCA compresses them into fewer, independent features — called Principal Components.

| Student | PC1 (Body Size) | PC2 (Proportion) |
| ------- | --------------- | ---------------- |
| A       | -1.2            | 0.3              |
| B       | 0.2             | -0.1             |
| C       | 1.4             | 0.5              |
| D       | -0.4            | -0.7             |

Now, instead of 5 features, you only have 2, but they capture 90–95% of the original info!

[Got To Top](#content)

---

# Implementation Of EDA using Zomato dataset

### 1. import the necessary Packages
```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```

### 2. Read the csv File
```py
df = pd.read_csv('/content/zomato.csv',encoding='latin-1')
df.head()
```
**Output:**

| Restaurant ID | Restaurant Name        | Country Code | City             | Address                                                  | Locality                                   | Locality Verbose                                             | Longitude  | Latitude  | Cuisines                         | Currency         | Has Table booking | Has Online delivery | Is delivering now | Switch to order menu | Price range | Aggregate rating | Rating color | Rating text | Votes |
| ------------- | ---------------------- | ------------ | ---------------- | -------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------ | ---------- | --------- | -------------------------------- | ---------------- | ----------------- | ------------------- | ----------------- | -------------------- | ----------- | ---------------- | ------------ | ----------- | ----- |
| 6317637       | Le Petit Souffle       | 162          | Makati City      | Third Floor, Century City Mall, Kalayaan Avenue...       | Century City Mall, Poblacion, Makati City  | Century City Mall, Poblacion, Makati City, Makati City       | 121.027535 | 14.565443 | French, Japanese, Desserts       | Botswana Pula(P) | Yes               | No                  | No                | No                   | 3           | 4.8              | Dark Green   | Excellent   | 314   |
| 6304287       | Izakaya Kikufuji       | 162          | Makati City      | Little Tokyo, 2277 Chino Roces Avenue, Legaspi...        | Little Tokyo, Legaspi Village, Makati City | Little Tokyo, Legaspi Village, Makati City, Makati City      | 121.014101 | 14.553708 | Japanese                         | Botswana Pula(P) | Yes               | No                  | No                | No                   | 3           | 4.5              | Dark Green   | Excellent   | 591   |
| 6300002       | Heat - Edsa Shangri-La | 162          | Mandaluyong City | Edsa Shangri-La, 1 Garden Way, Ortigas, Mandaluyong City | Edsa Shangri-La, Ortigas, Mandaluyong City | Edsa Shangri-La, Ortigas, Mandaluyong City, Mandaluyong City | 121.056831 | 14.581404 | Seafood, Asian, Filipino, Indian | Botswana Pula(P) | Yes               | No                  | No                | No                   | 4           | 4.4              | Green        | Very Good   | 270   |
| 6318506       | Ooma                   | 162          | Mandaluyong City | Third Floor, Mega Fashion Hall, SM Megamall, Ortigas...  | SM Megamall, Ortigas, Mandaluyong City     | SM Megamall, Ortigas, Mandaluyong City, Mandaluyong City     | 121.056475 | 14.585318 | Japanese, Sushi                  | Botswana Pula(P) | No                | No                  | No                | No                   | 4           | 4.9              | Dark Green   | Excellent   | 365   |
| 6314302       | Sambo Kojin            | 162          | Mandaluyong City | Third Floor, Mega Atrium, SM Megamall, Ortigas...        | SM Megamall, Ortigas, Mandaluyong City     | SM Megamall, Ortigas, Mandaluyong City, Mandaluyong City     | 121.057508 | 14.584450 | Japanese, Korean                 | Botswana Pula(P) | Yes               | No                  | No                | No                   | 4           | 4.8              | Dark Green   | Excellent   | 229   |

Shape: 5 rows × 21 columns


with this we can see:
- all available feature
- basic structure of our dataset
- Key columns and what they mean    

### 3. Retrieve all the columns
```py
df.columns
```
**Output:**
```
Index(['Restaurant ID', 'Restaurant Name', 'Country Code', 'City', 'Address',
       'Locality', 'Locality Verbose', 'Longitude', 'Latitude', 'Cuisines',
       'Average Cost for two', 'Currency', 'Has Table booking',
       'Has Online delivery', 'Is delivering now', 'Switch to order menu',
       'Price range', 'Aggregate rating', 'Rating color', 'Rating text',
       'Votes'],
      dtype='object')
```

### 4. Get quick summary of this Dataset
```py
df.info()
```
**Output:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9551 entries, 0 to 9550
Data columns (total 21 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Restaurant ID         9551 non-null   int64  
 1   Restaurant Name       9551 non-null   object 
 2   Country Code          9551 non-null   int64  
 3   City                  9551 non-null   object 
 4   Address               9551 non-null   object 
 5   Locality              9551 non-null   object 
 6   Locality Verbose      9551 non-null   object 
 7   Longitude             9551 non-null   float64
 8   Latitude              9551 non-null   float64
 9   Cuisines              9542 non-null   object 
 10  Average Cost for two  9551 non-null   int64  
 11  Currency              9551 non-null   object 
 12  Has Table booking     9551 non-null   object 
 13  Has Online delivery   9551 non-null   object 
 14  Is delivering now     9551 non-null   object 
 15  Switch to order menu  9551 non-null   object 
 16  Price range           9551 non-null   int64  
 17  Aggregate rating      9551 non-null   float64
 18  Rating color          9551 non-null   object 
 19  Rating text           9551 non-null   object 
 20  Votes                 9551 non-null   int64  
dtypes: float64(3), int64(5), object(13)
memory usage: 1.5+ MB
```
this tells us:
- Number of rows and columns (9551 rows X 21 columns)
- Column names
- Data types (int64, float64, object, etc.)
- Count of non-null (non-missing) values in each column
- Memory usage (1.5+ MB)

[Got To Top](#content)

---
