# Content
1. [Introduction](#introduction)
2. [Installation](#installation)


# Introduction

Pandas is a popular Python library build on **NumPy**, used for **data analysis and manipulation**. Think of it like a very powerful Excel inside Python, but with code.

### Why use pandas
- **high performance:** handle million of rows efficiently
- **Ease of use:** beginner friendly syntax
- **Integration:** works with libraries like **matplotlib**(visualization) ans **scikit-learn** (machine learning)

### Use case
Pandas makes it easy to:
- Load data (from CSV, Excel, SQL, etc.)
- Clean and prepare data
- Analyze and summarize data
- Visualize data (combined with libraries like Matplotlib or Seaborn)


| Field        | Use Case                              |
| ------------ | ------------------------------------- |
| Data Science | Data cleaning, EDA, ML preprocessing  |
|  Machine learning | preparing the dataset for training the machine learning model |
|Data analytic | cleaning the data, generating the insight 
| Finance      | Stock analysis, financial modeling    |
| Web Dev      | User data handling, Excel/CSV parsing |
| Marketing    | Campaign/sales analysis               |
| Healthcare   | Patient data analysis                 |
| Research     | Survey/experiment data analysis       |
| IoT          | Time-series sensor data analysis      |


### Data Manipulation
Data manipulation is the process of changing, organizing, or analyzing data to make it more useful or understandable.

- **It includes:**
    - Cleaning messy data
    - Filtering only useful rows
    - Changing values (e.g., converting strings to numbers)
    - Rearranging data
    - Summarizing or aggregating
    
- **Simple Real-life Analogy:**\
You get a list of student names with marks and missing values. Before calculating averages or making a rank list:

    - You fill in missing marks
    - Remove duplicate entries
    - Sort students by score
    - Convert names to proper case
    
This is **data manipulation**.


### Data Analysis
**Data Analysis** is the process of **inspecting, organizing, and interpreting data** to find useful information, draw conclusions, and support decision-making.

- **Goal of Data Analysis**
    - Understand what's happening in the data
    - Identify patterns, relationships, and trends
    - Make data-driven decisions

- **Simple Real-life Analogy:**

You get a list of student names with marks

Now you ask meaningful questions from the cleaned list, like:

✅ ***1. "What is the average score of the class?"***
- You add up all the marks and divide by number of students.

✅ ***2. "Who got the highest mark?"***
- You scan the list to find the top scorer.

✅ ***3. "How many students scored above 80?"***
- You count how many students got more than 80 — maybe that’s your benchmark for excellence.

This is **data analysis**



### Key difference between data manipulation and data analysis
| Feature              | **Data Manipulation**                         | **Data Analysis**                                  |
| -------------------- | --------------------------------------------- | -------------------------------------------------- |
| **Purpose**          | To clean, organize, and prepare the data      | To understand and extract insights from data       |
| **Goal**             | Make data usable and structured               | Answer questions or support decision-making        |
| **Example Question** | “Are there any missing or duplicate entries?” | “Who scored the highest?” or “What’s the average?” |
| **What You Do**      | Fix errors, fill missing values, sort data    | Calculate stats, find patterns, group data         |
| **When Used**        | Before analysis                               | After data is ready                                |
| **Output**           | Cleaned, corrected dataset                    | Insights, summaries, or visualizations             |
| **Analogy**          | Cleaning ingredients before cooking           | Actually cooking and serving the meal              |


### Key concept

1. **series:**
    - **series** is a **one dimensional array** that can hold any data type: Integer, float, string, or even python object. 
    - Each element in series has a unique label called **index** 
    - often use to track the changes or pattern over time
2. **Data Frame:**
    - **Data frame** is a **two dimensional labeled data structure** in pandas, similar to table in a database, excel, sql, etc.
    - it contain of **rows** and **column** where:
        - Rows have index
        - column have name

[Go To Top](#content)

---

# Installation
1. create the virtual environment
```bash
python -m venv .venv
```
2. activate the virtual environment
```bash
venv\scripts\activate       # for window
source env/bin/activate   # on Mac/Linux
``` 
3. install pandas
```bash
pip install pandas # using pip (python package installer)
conda install pandas # using conda (Anaconda)
```

4. import pandas
```py
import pandas as pb
```


[Go To Top](#content)

---
# Read external files

we have to create the DataFrame to read the specific file

**Syntax:**
```py
df = pb_function("file path")
```

by simply using this syntax we might encounter a error related to encoding methods because Pandas is trying to read the file using the wrong character encoding, and some characters in the file can't be interpreted properly.

to solve this error we mention encoding method in our syntax
**Syntax:**
```py
df = pb_function("file path", encoding="your encoding method")
```
there are two different encoding methods i.e,
1. utf-8
2. latin1

**Note: encoding method changes from device to device, that is one method work on one device but not on other, sometime you might not even need to use any encoding method**
### Example code
```py
import pandas as pb

# read data from csv file into dataframe
df_csv = pb.read_csv('./Dataset/sales_data_sample.csv', encoding='latin1')  # in my device utf-8 doesn't work but latin1 work

df_json = pb.read_json('./Dataset/sample_Data.json') # coe run without mentioning any method 

print(df_csv)
print(df_json)
```

you can read more files by using:
| File Type | Pandas Function   | 
| --------- | ----------------- | 
| CSV       | `.read_csv()`   | 
| Excel     | `.read_excel()` |
| JSON      | `.read_json()`  |
| SQL       | `.read_sql()`   | 


[Go To Top](#content)

---