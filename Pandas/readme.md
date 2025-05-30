# Content
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Read files](#read-external-files)
4. [save file](#save-file)
5. [Info & Describe](#info--describe)
6. [Shape & Column](#shape-and-column)

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

**Syntax: 1**
```py
df = pb_function("file path")
```

by simply using this syntax we might encounter a error related to encoding methods because Pandas is trying to read the file using the wrong character encoding, and some characters in the file can't be interpreted properly.

to solve this error we mention encoding method in our syntax\
**Syntax: 2**
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


### head() vs tail()
this are the special method us to display the part (limited number of rows) of dataset

- **head(n):** will display the first `n` entries from the dataset
- **tail(n):** will display the last `n` entries from the dataset
- default value of `n` is `5` that is if we use only `head()` and `tail()` without mentioning the limit then it will only display first and last 5 entries from the dataset
- example:
```py
import pandas as pb

df_json = pb.read_json('./Dataset/sample_Data.json')

print(df_json.head())
```
this code will display the first 5 rows from the `sample_Data.json` dataset

[Go To Top](#content)

---

# Save file

1. **create the dictionary of the data you want to save**
```py
data = {
    "Name":["ram", 'sham', 'yash'],
    "Age":[20, 21, 22],
    "City":["kalyan", 'pune', 'mumbai']
}
```
2. **create the new dataFrame with this data**
```py
df = pb.DataFrame(data)
```
if try and print this `df` object the our output is as follow
```
   Name  Age    City
0   ram   20  kalyan
1  sham   21    pune
2  yash   22  mumbai
```
here you can see a extra felid in first column that represent the numbering of row

3. **save this dataFrame into any format you want**


```py
df.to_csv('./Dataset/new_data.csv') 
```
if you save file like this it may contain that extra numbering felid as well therefor to remove that extra felid we add `index = false`
```py
df.to_csv('./Dataset/new_data.csv', index=False)
```
this create the `new_data.csv` file in `Dataset` folder containing our data we mention in dictionary from step 1

| **File Type** | **Method**       | **File Extension** |
| ------------- | ---------------- | ------------------ |
| CSV           | `to_csv()`       | `.csv`             |
| Excel         | `to_excel()`     | `.xlsx`            |
| JSON          | `to_json()`      | `.json`            |
| HTML          | `to_html()`      | `.html`            |
| SQL           | `to_sql()`       | (SQL table)        |
| Pickle        | `to_pickle()`    | `.pkl`             |
| Parquet       | `to_parquet()`   | `.parquet`         |
| Stata         | `to_stata()`     | `.dta`             |
| Feather       | `to_feather()`   | `.feather`         |
| LaTeX         | `to_latex()`     | `.tex`             |
| Clipboard     | `to_clipboard()` | *(none)*           |
| Markdown      | `to_markdown()`  | *(none)*           |


**Note: while writing the name of the file make sure that you also mention the valid extension for respective file format in that name**

[Go To Top](#content)

---


# Info & Describe

### .info()
it will give you the overall summary of your dataset

```py
data = {
    "Name":["ram", 'sham', 'yash'],
    "Age":[20, 21, 22],
    "City":["kalyan", None, 'mumbai']   # None = null
}

df = pb.DataFrame(data)
print(df.info())
```

**Output:**
```
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      object
 1   Age     3 non-null      int64
 2   City    2 non-null      object
dtypes: int64(1), object(2)
memory usage: 204.0+ bytes
None
```

- **RangeIndex:** number of rows in the dataset
- **Data columns:** info about each column, in bracket you can see the number of column
    - **#:** column number (starts from 0)
    - **Column:** name of the particular column
    - **Non-Null Count:** number of not null entries (number of 
    not null value for that single column)
    - **Dtype:** what type of data is present in that column
- **dtypes:** how many datatype we have use in our dataset, you can see each data type and how many columns have use that datatype
- **memory usage:** amount of memory needed for that dataset



### .describe()
The `.describe()` function in Pandas is used to quickly generate summary statistics for numeric column in our DataFrame 

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23], # numeric column
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000] # numeric column
}

df = pb.DataFrame(data)
print(df.describe())
```

**Output:**
in output we only see summary of numeric column (age ans salary)
```
             Age        salary
count   6.000000      6.000000
mean   22.833333  35000.000000
std     2.316607  18708.286934
min    20.000000  10000.000000
25%    21.250000  22500.000000
50%    22.500000  35000.000000
75%    24.500000  47500.000000
max    26.000000  60000.000000
```

| **Statistic** | **Meaning**                         |
| ------------- | ----------------------------------- |
| `count`       | Number of non-null (not NaN) values |
| `mean`        | Average value                       |
| `std`         | Standard deviation ( how spread out the values in a dataset are from the mean (average).It tells you how much the data varies.) high std means difference in data is high and low std means difference in data is low                |
| `min`         | Minimum value                       |
| `25%`         | 1st quartile (mean of first 25th percentile in our dataset)      |
| `50%`         | Median (mean of data present from 25 to 50th percentile in our dataset)            |
| `75%`         | 3rd quartile (mean of data present from 50 to 75th percentile in our dataset)      |
| `max`         | Maximum value                       |


[Go To Top](#content)

---

# Shape and Column

### Shape
- Return the tuple name `shape` that gives the dimensions (rows, columns) of a DataFrame.
- syntax:
```
shape: (number_of_column, Number_of_rows)
```

### Column
- return the tuple name `index` that contain the two thing
    1. list of all column
    2. dtype: what kind of data is present in the list
- Syntax:
```
columns: Index(['col_1', 'col_2', ...], dtype='dtype_of_columns')
```


### Example code:
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')
```
### Output:
```
shape: (6, 4)
columns: Index(['Name', 'Age', 'City', 'salary'], dtype='object')
```




[Go To Top](#content)

---


