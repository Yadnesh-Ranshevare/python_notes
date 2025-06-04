# Content
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Read files](#read-external-files)
4. [save file](#save-file)
5. [Info & Describe](#info--describe)
6. [Access Row](#accessing-rows)
7. [Row Slicing](#row-slicing)
8. [Access Column](#accessing-columns)
9. [Column Slicing](#column-slicing)
10. [Filtering the rows](#filtering-the-rows)
11. [How to add a new column?](#how-to-add-new-column)
12. [Updating the data](#updating-data)
13. [Removing the Columns](#removing-column)
14. [How to detect the missing value using .isnull()](#how-to-detect-the-missing-value-using-isnull)
15. [Handling the missing data using .dropna(), .fillna() and .interpolate()](#handling-the-missing-data)
16. [How to sort the data](#how-to-sort-the-dataset)
17. [Aggregation Functions](#aggregation-functions)
18. [Grouping in Pandas](#grouping-in-pandas)

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

df_json = pb.read_json('./Dataset/sample_Data.json') # coed run without mentioning any method 

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
    - **#:** column index (starts from 0)
    - **Column:** name of the particular column
    - **Non-Null Count:** number of not null entries (number of 
    not null value for that single column)
    - **Dtype:** what type of data is present in that column
- **dtypes:** how many datatype we have use in our dataset, you can see each data type and how many columns have use that datatype
- **memory usage:** amount of memory needed for that dataset



### .describe()
The `.describe()` function in Pandas is used to quickly generate summary statistics for `numeric column` in our DataFrame 

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


# Accessing Rows

### `.iloc`

1. **Accessing single rows**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[1])
```
**Output:**
```
Name       sham
Age          21
City       None
salary    20000
Name: 1, dtype: object
```
2. **Accessing multiple rows**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[[1,2,3]])     # provide the list of all the index in lists
```
**output:**
```
    Name  Age    City  salary
1   sham   21    None   20000
2   yash   22  mumbai   30000
3  rohan   25    pune   40000
```

### `.loc`
1. **Accessing single rows**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[1])
```
**Output:**
```
Name       sham
Age          21
City       None
salary    20000
Name: 1, dtype: object
```
2. **Accessing multiple rows**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[[1,2,3]])  # provide the list of all the index in lists
```
**output:**
```
    Name  Age    City  salary
1   sham   21    None   20000
2   yash   22  mumbai   30000
3  rohan   25    pune   40000
```


### `Accessing all rows`
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

print("using loc \n")
print(df.loc[:])

print("\nusing iloc \n")
print(df.iloc[:])
```
**Output:**
```
using loc 

    Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   20000
2   yash   22    mumbai   30000
3  rohan   25      pune   40000
4  aditi   26    nagpur   50000
5  rohit   23  banglore   60000

using iloc

    Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   20000
2   yash   22    mumbai   30000
3  rohan   25      pune   40000
4  aditi   26    nagpur   50000
5  rohit   23  banglore   60000
```
- **Note: `.loc[]` and `.iloc[]` this two method wee also use while accessing the column, although this two method works similarly for accessing the row their implementation changes as you try to access the columns**

[Go To Top](#content)

---
# Row slicing

### Using iloc
- **`.iloc[2:4]`**: rows from index 2 to 4, where 4 is `excluded`
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[2:4])
```
**Output:**
```
    Name  Age    City  salary
2   yash   22  mumbai   30000
3  rohan   25    pune   40000
```

- **`.iloc[0:5:2]`**: rows from 0 to 5 where 5 is `excluded` with step size of 2
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[0:5:2])
```
**Output:**
```
    Name  Age    City  salary
0    ram   20  kalyan   10000
2   yash   22  mumbai   30000
4  aditi   26  nagpur   50000
```
### Using loc
- **`.loc[2:4]`**: rows from index 2 to 4, where 4 in `included`
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[2:4])
```
**Output:**
```
    Name  Age    City  salary
2   yash   22  mumbai   30000
3  rohan   25    pune   40000
4  aditi   26  nagpur   50000
```

- **`.loc[0:5:2]`**: rows from 0 to 5 where 5 is `included` with step size of 2
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[0:5:2])
```
**Output:**
```
    Name  Age    City  salary
0    ram   20  kalyan   10000
2   yash   22  mumbai   30000
4  aditi   26  nagpur   50000
```

#### Note: in `.iloc` last index is `excluded` wheres in `.loc` las index is `included`


[Go To Top](#content)

---



# Accessing Columns

### For single column

1. **using column name**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df['Name'])
```
**Output:**
```
0      ram
1     sham
2     yash
3    rohan
4    aditi
5    rohit
Name: Name, dtype: object
```


2. **using iloc (use index)**\
 **`.iloc[:, 0]`:** All rows from column 0

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[:, 0])    # column at index 0
```
**Output:**
```
0      ram
1     sham
2     yash
3    rohan
4    aditi
5    rohit
Name: Name, dtype: object
```


3. **using loc (use name)**\
**`.loc[:, ["Age"]]`**: All the rows from column Age

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[:, ["Age"]])
```
**Output:**
```
   Age
0   20
1   21
2   22
3   25
4   26
5   23
```






### For multiple column
1. **using column name** 
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df[["Name", "City", "salary"]]) # use nested lists
```
**Output:**
```
    Name      City  salary
0    ram    kalyan   10000
1   sham      None   20000
2   yash    mumbai   30000
3  rohan      pune   40000
4  aditi    nagpur   50000
5  rohit  banglore   60000
```

2. **Using iloc (using index)**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[:, [0, 2, 3]])    # provide the list of all the index in lists
```
**Output:**
```
    Name      City  salary
0    ram    kalyan   10000
1   sham      None   20000
2   yash    mumbai   30000
3  rohan      pune   40000
4  aditi    nagpur   50000
5  rohit  banglore   60000
```
3. **Using loc (using names)**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[:, ["Age","salary","Name"]])   # provide the list of all the names of column in lists
```
**Output:**
```
   Age  salary   Name
0   20   10000    ram
1   21   20000   sham
2   22   30000   yash
3   25   40000  rohan
4   26   50000  aditi
5   23   60000  rohit
```

### Note
**you can access column and row at the same time by using both `iloc` and `loc`**
1. using `iloc`
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[[0,2,4],[0,2]])
```
**Output:**
```
    Name    City
0    ram  kalyan
2   yash  mumbai
4  aditi  nagpur
```
2. using `loc`
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[[0,2,4],["Name","City"]])
```
**Output:**
```
    Name    City
0    ram  kalyan
2   yash  mumbai
4  aditi  nagpur
```



[Go To Top](#content)

---




# Column slicing

### Using iloc
- **`.iloc[:, 0:3]`**: All the rows from cloumn 0 to 3, where 3 is `excluded`
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[:, 0:3])  # column from index 0 to 3 where 3 is excluded
```
**Output:**
```
    Name  Age      City
0    ram   20    kalyan
1   sham   21      None
2   yash   22    mumbai
3  rohan   25      pune
4  aditi   26    nagpur
5  rohit   23  banglore
```
- **`.iloc[:,0:4:2]`**: All the rows from cloumn 0 to 4, where 4 is `excluded` and step size is 2

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[:,0:4:2])
```
- `Note:` you can also apply the row sllicing along with the column
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[0:4,0:3])
```
**Output:**
```
    Name  Age    City
0    ram   20  kalyan
1   sham   21    None
2   yash   22  mumbai
3  rohan   25    pune
```
### Using loc
- **`.loc[:,"Name":"City"]`**: all the rows from cloumns 'Name' to 'City'
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[:,"Name":"City"])
```
**Output:**
```
    Name  Age      City
0    ram   20    kalyan
1   sham   21      None
2   yash   22    mumbai
3  rohan   25      pune
4  aditi   26    nagpur
5  rohit   23  banglore
```
- **`.loc[:,"Name":"salary":2]`**: All the rows from cloumn 'Name'  to 'salary' , with step size is 2
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[:,"Name":"salary":2])
```
**Output:**
```
    Name      City
0    ram    kalyan
1   sham      None
2   yash    mumbai
3  rohan      pune
4  aditi    nagpur
5  rohit  banglore
```
- `Note:` you can also apply the row sllicing along with the column
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.loc[0:4,"Name":"City"])
```
**Output:**
```
    Name  Age    City
0    ram   20  kalyan
1   sham   21    None
2   yash   22  mumbai
3  rohan   25    pune
4  aditi   26  nagpur
```
#### Note: in `.iloc` last index is `excluded` wheres in `.loc` las index is `included`

[Go To Top](#content)

---

# Filtering the rows


create the new data frame that contains the all the entries which produce result as true for given condition

### for single condition
condition: salary greater that 30000
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

high_salary = df[df["salary"] > 30000]
print(high_salary)
```
**Output:**
```
    Name  Age      City  salary
3  rohan   25      pune   40000
4  aditi   26    nagpur   50000
5  rohit   23  banglore   60000
```

### For multiple condition
condition: salary between 30000 and 40000

Note: use round bracket inside the list to use muliple condition\
& -> and\
| -> or
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

filtered = df[(df["salary"] >= 30000) & (df["salary"] <= 40000)]
print(filtered)
```
**output:**
```
    Name  Age    City  salary
2   yash   22  mumbai   30000
3  rohan   25    pune   40000
```


[Go To Top](#content)

---
# How to add new column?


### Direct Assigenment

1. **Adding the new data into seprate column**

lets assume you have a data of employee where each column represent the Name, Age, City, salary and now you want to add each employeis performace score
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df["score"] = [20,45,78,87,67,8]    # ading the performance score into the original dala
print(df)
```
**Output:**
```
    Name  Age      City  salary  score
0    ram   20    kalyan   10000     20
1   sham   21      None   20000     45
2   yash   22    mumbai   30000     78
3  rohan   25      pune   40000     87
4  aditi   26    nagpur   50000     67
5  rohit   23  banglore   60000      8
```
**Note: make sure that you provide the data for each entry**

2. **Use one column to compute the new column**

lets assume you have a data of employee where each column represent the Name, Age, City, salary and now you have to find out the future salary of each employee after 10% increment in there original salary. Therefor add new column name future_salary to display the future salary

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df["future_salary"] = df['salary'] + df['salary'] * 0.1
print(df)
```
**Output:**
```
    Name  Age      City  salary  future_salary
0    ram   20    kalyan   10000        11000.0
1   sham   21      None   20000        22000.0
2   yash   22    mumbai   30000        33000.0
3  rohan   25      pune   40000        44000.0
4  aditi   26    nagpur   50000        55000.0
5  rohit   23  banglore   60000        66000.0
```

**Using direct assigenment we can only add the column at the last position that is we dont have any control over the position of new column. Therefor to solve this issue we have insert method** 

**Anothe problem with direct assigenment is that if you use allready existing column name then insted of creating new column it will overwrite the existing column**

### Insert method
syntax:

```py
df.insert('col_index', 'col_name', 'col_data')
```

**Example 1:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary and now you want to add each employeis performace score just after the 'Name' and before the 'Age' column
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.insert(1, "score", [45, 67, 63, 37, 98, 60])       
print(df)
```
**Output:**
```
    Name  score  Age      City  salary
0    ram     45   20    kalyan   10000
1   sham     67   21      None   20000
2   yash     63   22    mumbai   30000
3  rohan     37   25      pune   40000
4  aditi     98   26    nagpur   50000
5  rohit     60   23  banglore   60000
```

**Example 2:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary and now you have to find out the specific score of each employee based on their 'salary', lets say the sore is equal to the 50% of their original salary. Therefor add new column name sore just after the 'Name' and before the 'Age' to display the score of each empolyee
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.insert(1, "score", df['salary'] * 0.5)       
print(df)
```
**Output:**
```
    Name    score  Age      City  salary
0    ram   5000.0   20    kalyan   10000
1   sham  10000.0   21      None   20000
2   yash  15000.0   22    mumbai   30000
3  rohan  20000.0   25      pune   40000
4  aditi  25000.0   26    nagpur   50000
5  rohit  30000.0   23  banglore   60000
```

[Go To Top](#content)

---

# Updating Data

**Befor you learn about any of the updating method you must know about the column accessing methods and column sclicing as to update any column you first need to access that column**\
[Clikc here to learn about column Accessing](#accessing-columns)\
[Clikc here to learn about column Sclicing](#column-slicing)


### Data Overwriting

**in this method you completely overwrite the original data of specific column with new data**

**Example:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary now update the salary of each employee with 10% increment in their original salary

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df['salary'] = df['salary'] + df['salary'] * 0.1
print(df)
```


**Output:**
```
    Name  Age      City   salary
0    ram   20    kalyan  11000.0
1   sham   21      None  22000.0
2   yash   22    mumbai  33000.0
3  rohan   25      pune  44000.0
4  aditi   26    nagpur  55000.0
5  rohit   23  banglore  66000.0
```

**Note: if provided column name is not there in the dataset then this will create the new column with the name you mention in left side**


### Using `.loc`
**in this method you change the required  data of specific column with new data**

**Example 1:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary. There is a employee with name yash who just had a promotion and has his salary increases by 10%, therefor update the dataset for yash with his new salary

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.loc[2, "salary" ] = df.loc[2, "salary"] + df.loc[2, "salary"] * 0.1
print(df)
```
**Output:**
```
    Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   20000
2   yash   22    mumbai   33000
3  rohan   25      pune   40000
4  aditi   26    nagpur   50000
5  rohit   23  banglore   60000
```

**Example 2:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary. There are few employeis with index `1 to 4` who just had a promotion and had their salary increases by 10%, therefor update the dataset for those employeis with their new salary
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.loc[1:4, "salary" ] = df.loc[1:4, "salary"] + df.loc[1:4, "salary"] * 0.1
print(df)
```
**Output:**
```
    Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   22000
2   yash   22    mumbai   33000
3  rohan   25      pune   44000
4  aditi   26    nagpur   55000
5  rohit   23  banglore   60000
```


**Example 3:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary. There are few employeis with index `1 to 4` who has just shifted form there original Cities to new city, and now they live in a same city as that of employee with index `3` lives in, therefor update the data set for thos employee with there new city

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.loc[1:4, "City" ] = df.loc[3, "City"] 
print(df)
```
**Output:**
```
    Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      pune   20000
2   yash   22      pune   30000
3  rohan   25      pune   40000
4  aditi   26      pune   50000
5  rohit   23  banglore   60000
```


### Using `.iloc`
**this is works similar to `.loc` but you just have to check for indexing**

**Note: in case of slicing in `.loc` last index is `included` whereas in `.iloc` las index is `excluded`**

**Example :**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary. There are few employeis with index `1 to 4` who just had a promotion and had their salary increases by 10%, therefor update the dataset for those employeis with their new salary
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.iloc[1:5, 3 ] = df.iloc[1:5, 3] + df.iloc[1:5, 3] * 0.1 # 5 is excluded and column 'salary' is at index 3
print(df)
```
**Output:**
```
    Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   22000
2   yash   22    mumbai   33000
3  rohan   25      pune   44000
4  aditi   26    nagpur   55000
5  rohit   23  banglore   60000
```



[Go To Top](#content)

---

# Removing column

- we use `.drope` method to remove the column which accepst the two parameter i.e, columns and inplace
- **`columns:`** list of column you want to remove
- **`inplace:`** a boolean flage to specify whether to change the original dataset or not
    -  `inplace = True`: change the original dataset without returning anything
    -  `inplace = False`: does not change the original dataset, insted return the new dataset
    - by defult it is set to False
- Syntax: `.drop(columns = ['col_1', 'col_2', ...], inplace = True/False)`


### Example: remove city column

1. **without inplace**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

new_Dataset = df.drop(columns=['City']) # by defult inplace is set to False     

print("new dataset\n",new_Dataset)
print("\n original dataset\n",df)
```
**Output:**
```
new dataset
     Name  Age  salary
0    ram   20   10000
1   sham   21   20000
2   yash   22   30000
3  rohan   25   40000
4  aditi   26   50000
5  rohit   23   60000

 original dataset
     Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   20000
2   yash   22    mumbai   30000
3  rohan   25      pune   40000
4  aditi   26    nagpur   50000
5  rohit   23  banglore   60000
```

2. **inplace = False**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

new_Dataset = df.drop(columns=['City'], inplace = False)    # return modified dataset without changing the original

print("new dataset\n",new_Dataset)
print("\n original dataset\n",df)
```
**Output:**
```
new dataset
     Name  Age  salary
0    ram   20   10000
1   sham   21   20000
2   yash   22   30000
3  rohan   25   40000
4  aditi   26   50000
5  rohit   23   60000

 original dataset
     Name  Age      City  salary
0    ram   20    kalyan   10000
1   sham   21      None   20000
2   yash   22    mumbai   30000
3  rohan   25      pune   40000
4  aditi   26    nagpur   50000
5  rohit   23  banglore   60000
```
3. **inplace = True**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

new_Dataset = df.drop(columns=['City'], inplace = True) # doesn't return anything

print("new dataset\n",new_Dataset)
print("\n original dataset\n",df)
```
**Output:**
```
new dataset
 None

 original dataset
     Name  Age  salary
0    ram   20   10000
1   sham   21   20000
2   yash   22   30000
3  rohan   25   40000
4  aditi   26   50000
5  rohit   23   60000
```
### Removing multiple columns
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

new_Dataset = df.drop(columns=['City', 'Age'], inplace = True)

print("new dataset\n",new_Dataset)
print("\n original dataset\n",df)
```
**Output:**
```
new dataset
 None

 original dataset
     Name  salary
0    ram   10000
1   sham   20000
2   yash   30000
3  rohan   40000
4  aditi   50000
5  rohit   60000
```


[Go To Top](#content)

---

# How to detect the missing value using .isnull()

- **`.isnull()`**: return true if value is missing and uf value is present then return false

```py
data = {
    "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, None, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

print(df.isnull())
```
**Output:**
```
    Name    Age   City  salary
0  False  False  False   False
1   True   True   True    True
2  False  False  False   False
3  False  False  False   False
4  False  False  False   False
5  False  False  False   False
```

- **`.isnull().sum()`**: return the total number of missing values in each column

```py
data = {
    "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, None, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

print(df.isnull().sum())
```
**Output:**
```
Name      1
Age       1
City      1
salary    1
dtype: int64
```


[Go To Top](#content)

---
# Handling the missing data

## .dropna()
- it remove the missing data
- accept two parameter i.e, axis & inplace
- axis:- 
    - `axis = 1`: will remove the column who has missing data
    - `axis = 0`: will remove the row who has missing data
    - by default axis is set to 0
- inplace:-
    -  `inplace = True`: change the original dataset without returning anything
    -  `inplace = False`: does not change the original dataset, insted return the new dataset
    - by defult it is set to False
    - [to learn more about inplace click here](#removing-column)

1. without axis
```py
data = {
    "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, None, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.dropna(inplace=True) # by default axis is set to 0
print(df)
```
**Output:**
```
    Name   Age      City   salary
0    ram  20.0    kalyan  10000.0
2   yash  22.0    mumbai  30000.0
3  rohan  25.0      pune  40000.0
4  aditi  26.0    nagpur  50000.0
5  rohit  23.0  banglore  60000.0
```
2. axis = 0 (remove row)
```py
data = {
    "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, None, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.dropna(inplace=True, axis=0)
print(df)
```
**Output:**
```
    Name   Age      City   salary
0    ram  20.0    kalyan  10000.0
2   yash  22.0    mumbai  30000.0
3  rohan  25.0      pune  40000.0
4  aditi  26.0    nagpur  50000.0
5  rohit  23.0  banglore  60000.0
```
3. axis = 1 (remove column)
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.dropna(inplace=True, axis=1)
print(df)
```
**Output:**
```
    Name  Age
0    ram   20
1   sham   21
2   yash   22
3  rohan   25
4  aditi   26
5  rohit   23
```
## .fillna()
- fill the default inpace of null
- it taks two parameter i.e, value and inplace
- value: default value you want to replace instead of null
- inplace:-
    -  `inplace = True`: change the original dataset without returning anything
    -  `inplace = False`: does not change the original dataset, insted return the new dataset
    - by defult it is set to False
    - [to learn more about inplace click here](#removing-column)
- syntax: `df.fillna(value, inplace = true/false)`

**Example 1: direcct replacement**
```py
data = {
    "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, None, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.fillna(0, inplace=True)
print(df)
```
**Output:**
```
    Name   Age      City   salary
0    ram  20.0    kalyan  10000.0
1      0   0.0         0      0.0
2   yash  22.0    mumbai  30000.0
3  rohan  25.0      pune  40000.0
4  aditi  26.0    nagpur  50000.0
5  rohit  23.0  banglore  60000.0
```

**Example 2: perticulat value for perticular column**\
fill the missing Age and salary with avarage Age and avarage salary
```py
data = {
    "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, None, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, None, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df['Age'].fillna(df['Age'].mean() , inplace=True)
df['salary'].fillna(df['salary'].mean() , inplace=True)
print(df)
```
**Output:**
```
    Name   Age      City   salary
0    ram  20.0    kalyan  10000.0
1   None  23.2      None  38000.0
2   yash  22.0    mumbai  30000.0
3  rohan  25.0      pune  40000.0
4  aditi  26.0    nagpur  50000.0
5  rohit  23.0  banglore  60000.0
```
## .interpolate()
The `.interpolate()` method in Pandas is used to fill missing values (`NaN`) in a DataFrame or Series by **estimating** them from existing data.

Example: lets assume you have dataFrame like:
```py
data = {
    "Time":[1, 2, 3, 4, 5],
    "Value":[10, None, 30, None, 50]
}

df = pb.DataFrame(data)
```
- in above dataframe you can see that value column has some missing data, 
- but you can see the trend(10, 20, 30, 40, 50) in the data pattern of 'Value' column, if you follow this trend then you can estimate the missing data of the 'Value' column, 
- by filling thos estimaated column you will get the 'Value' column as follow: `[10, 20, 30, 40, 50]`
- `.interpolate()` method can estimate those missing value
- it take one parameter as input i.e, `method`
- `method`: there are various method on the basis of which you can estimate the missing value

**Code:**

```py
data = {
    "Time":[1, 2, 3, 4, 5],
    "Value":[10, None, 30, None, 50]
}

df = pb.DataFrame(data)

df['Value'] = df['Value'].interpolate(method='linear')
print(df)
```
**Output:**
```
   Time  Value
0     1   10.0
1     2   20.0
2     3   30.0
3     4   40.0
4     5   50.0
```

**Some methods you can learn on your own**


| Method                   | Meaning                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| `'linear'`               | Default. Fills missing values by drawing a straight line between known values.                        |
| `'time'`                 | Works with time-indexed data. Interpolates based on time differences.                                 |
| `'index'`                | Uses the numeric index values to interpolate. Similar to linear but based on index.                   |
| `'pad'` / `'ffill'`      | Fill missing values with the **previous** known value (forward fill).                                 |
| `'backfill'` / `'bfill'` | Fill missing values with the **next** known value (backward fill).                                    |
| `'polynomial'`           | Fit a polynomial function to known values and estimate missing ones. You need to provide the `order`. |
| `'spline'`               | Similar to polynomial but smoother; uses spline functions.                                            |
| `'barycentric'`          | Uses barycentric interpolation. Works well for small datasets.                                        |
| `'nearest'`              | Fills with the nearest known value (left or right).                                                   |



[Go To Top](#content)

---

# How to sort the dataset
- we use `.sort_values()` method to sort the columns, ehich takes three parameter i.e, by, ascending, inplace
- `by`: on the basus of which column you want to sort the dataset
- `ascending`: accept a boolean value and decide in which order to sort the dataset
    - `ascending = True`: sort the dataset from low to high
    - `ascending = False`:dort the dataset from high to low
    - default value of ascending if True
- inplace:-
    -  `inplace = True`: change the original dataset without returning anything
    -  `inplace = False`: does not change the original dataset, insted return the new dataset
    - by defult it is set to False
    - [to learn more about inplace click here](#removing-column)

**Example:**
sort the given dataset of employee on the basis of employeis age
1. ascending = True : from low to high
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 32, 25, 19, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.sort_values(by='Age', inplace=True, ascending=True)
print(df)
```
**Output:**
```
    Name  Age      City  salary
4  aditi   19    nagpur   50000
0    ram   20    kalyan   10000
1   sham   21      None   20000
5  rohit   23  banglore   60000
3  rohan   25      pune   40000
2   yash   32    mumbai   30000
```
2. without ascending: by default ascending is set to True(case 1)
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 32, 25, 19, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.sort_values(by='Age', inplace=True)
print(df)
```
**Output:**
```
    Name  Age      City  salary
4  aditi   19    nagpur   50000
0    ram   20    kalyan   10000
1   sham   21      None   20000
5  rohit   23  banglore   60000
3  rohan   25      pune   40000
2   yash   32    mumbai   30000
```
3. ascending = False : from high to low
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 32, 25, 19, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.sort_values(by='Age', inplace=True, ascending=False)
print(df)
```
**Output:**
```
    Name  Age      City  salary
2   yash   32    mumbai   30000
3  rohan   25      pune   40000
5  rohit   23  banglore   60000
1   sham   21      None   20000
0    ram   20    kalyan   10000
4  aditi   19    nagpur   50000
```

- you can also apply the sorting in multiple column at the same time
- to do that you just nees to provide the list of column in by parameter
- similarly for ascending parameter you will provide a list for that respective columns

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 32, 25, 19, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.sort_values(by=['Age','salary'], inplace=True, ascending=[False, True])  # first False for 'Age' column and second True is for 'salary' cloumn
print(df)
```
**Output:**
```
    Name  Age      City  salary
2   yash   32    mumbai   30000
3  rohan   25      pune   40000
5  rohit   23  banglore   60000
1   sham   21      None   20000
0    ram   20    kalyan   10000
4  aditi   19    nagpur   50000
```





[Go To Top](#content)

---
# Aggregation Functions
In Pandas, aggregation functions are used to summarize or combine multiple values into a single value — usually when working with groups of data or when applying operations on DataFrames/Series


### Common Aggregation Functions in Pandas

| Function    | Description                     | Example Result on `[1, 2, 3, 4, 5]` |
| ----------- | ------------------------------- | ----------------------------------- |
| `sum()`     | Sum of all values               | `15`                                |
| `mean()`    | Average (arithmetic mean)       | `3.0`                               |
| `median()`  | Middle value                    | `3`                                 |
| `min()`     | Smallest value                  | `1`                                 |
| `max()`     | Largest value                   | `5`                                 |
| `count()`   | Number of non-null values       | `5`                                 |
| `std()`     | Standard deviation              | `1.58` (approx)                     |
| `var()`     | Variance                        | `2.5`                               |
| `prod()`    | Product of all values           | `120`                               |
| `nunique()` | lisy of unique values         | `[1 2 3 4 5]`                                 |

**Code:**
```py
data = {
    "Value":[1, 2, 3, 4, 5, 5]
}

df = pb.DataFrame(data)

print(df['Value'].sum())
print(df['Value'].mean())
print(df['Value'].median())
print(df['Value'].min())
print(df['Value'].max())
print(df['Value'].count())
print(df['Value'].std())
print(df['Value'].var())
print(df['Value'].prod())
print(df['Value'].unique())
```
**Output:**
```
20
3.3333333333333335
3.5
1
5
6
1.632993161855452
2.666666666666667
600
[1 2 3 4 5]
```


[Go To Top](#content)

---
# Grouping in Pandas
Grouping in pandas means splitting data into groups based on some criteria, then applying a function (like sum, mean, count, etc.) to each group.

- consider a dataset as follow
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}
```
- if you focus on age column then you can see that there are multiple people with same age, in pamdas you can group those people with similar age by using `goroupby` method
- it return a list like structure (`<class 'pandas.core.groupby.generic.SeriesGroupBy'>`) that containg list of tuples and each tuple consist of two things i.e, 
    1. **value:** on the basis of whih we are making the group, in our example its 'Age'
    2. **data:** grouped data of that value
- Output syntax: `[(value, data), (value, data), ....]`


## Grouping all the column

lets assume you have a data of employee where each column represent the Name, Age, City, salary. Group the given data according to the Age of the employee


**Code:**
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

grouped = df.groupby('Age')

for group in grouped:
    print(group)
```
**Output:**
```
(20,   Name  Age    City  salary
    0  ram   20  kalyan   10000)
(21,     Name  Age  City  salary
    1   sham   21  None   20000
    3  rohan   21  pune   40000)
(22,     Name  Age      City  salary
    2   yash   22    mumbai   30000
    5  rohit   22  banglore   60000)
(23,     Name  Age    City  salary
    4  aditi   23  nagpur   50000)
```
- in above example we can see that there is only one person (ram) with age 20, two persons (sham & rohan) with age 21, two persons (yash & rohit) with age 22 and one person (aditi) with age 23



## Grouping single column
- if we want to group the specific column then we can also do that my mentioning the name of that column

- **Example:**\
find name of all employee with their respective age group

```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

grouped = df.groupby('Age')["Name"]     # mention the name of the column

for group in grouped:
    print(group)
```

**Output:**
```
(20, 0    ram
Name: Name, dtype: object)
(21, 1     sham
     3    rohan
Name: Name, dtype: object)
(22, 2     yash
     5    rohit
Name: Name, dtype: object)
(23, 4    aditi
Name: Name, dtype: object)
```
Here `Name` represent the name of that column on which we have performed group

## Groupin the multiple columns
- Use nested list to provide the multiple column name
- **Example:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary. Group the given data according to the Age of the employee and find the salary of each employee for each group
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

grouped = df.groupby('Age')[["Name", "salary"]] # provie the name of multiple column inside the nested list

for group in grouped:
    print(group)
```
**Output:**
```
(20,   Name  salary
    0  ram   10000)
(21,     Name  salary
    1   sham   20000
    3  rohan   40000)
(22,     Name  salary
    2   yash   30000
    5  rohit   60000)
(23,     Name  salary
    4  aditi   50000)
```

## How to add Aggregation Functions along with groupby
- you can only apply the Aggregation function on a numeric column\
[to learn about Aggregation Functions](#aggregation-functions)
- **Example:**\
lets assume you have a data of employee where each column represent the Name, Age, City, salary. Group the given data according to the Age of the employee and find the total salary of each group
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

grouped = df.groupby('Age')[[ "salary"]].sum()

print(list(grouped.items()))
``` 
**Output:**
```
[('salary', Age
20    10000
21    60000
22    90000
23    50000
Name: salary, dtype: int64)]
```

## Grouping multiple columns
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[30000, 20000, 10000, 20000, 50000, 10000]
}

df = pb.DataFrame(data)

grouped = df.groupby(['Age','salary'])
for group in grouped:
    print(group)
```
**Outpput:**
```
((np.int64(20), np.int64(30000)),   Name  Age    City  salary
                                  0  ram   20  kalyan   30000)
((np.int64(21), np.int64(20000)),     Name  Age  City  salary
                                  1   sham   21  None   20000
                                  3  rohan   21  pune   20000)
((np.int64(22), np.int64(10000)),     Name  Age      City  salary
                                  2   yash   22    mumbai   10000
                                  5  rohit   22  banglore   10000)
((np.int64(23), np.int64(50000)),     Name  Age    City  salary
                                  4  aditi   23  nagpur   50000)
```

## How to print the result
to print this we have two differnt ways as follow:

1. `list(grouped_dataset):` 
    - for genral grouped dataset **without Aggregation**
    - aggregation function return the single tuple
    - Therefor with aggregation it only print the list contaning the result of that aggregation function and not in key  value format
    - This does not work if you apply aggregation on multiple coulmn at same time and insted of returning the value it return the column name
    - even if you have one column in the nested list it will still provide the column name as a output
    - therefor we can say that this method **does not work when we have nested lists** that is styntax for multiple column
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

grouped_by_aggregation = df.groupby('Age')["salary"].sum()
grouped_by_aggregation_Group_of_column = df.groupby('Age')[["salary"]].sum()
grouped_by = df.groupby('Age')[[ "salary"]]

print(list(grouped_by_aggregation)) # onlly provide the vallues
print("\n\n")
print(list(grouped_by))
print("\n\n")
print(list(grouped_by_aggregation_Group_of_column))     # only provide the list contaning the column name
```
**Output**
```
[10000, 60000, 90000, 50000]



[(20,    salary
     0   10000), 
 (21,    salary
     1   20000
     3   40000), 
 (22,    salary
     2   30000
     5   60000), 
 (23,    salary
     4   50000)]


['salary']
```
2. `list(grouped_dataset.items()):` 
    - when you have performed Aggregation function on grouped dataset and want to perform the print operation to print the result in key value format
    - this method does not work on normal groupedby function (without aggregation)
```py
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 21, 23, 22],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

grouped_by_aggregation = df.groupby('Age')["salary"].sum()
grouped_by_aggregation_Group_of_column = df.groupby('Age')[["salary"]].sum()
grouped_by = df.groupby('Age')[[ "salary"]]

print(list(grouped_by_aggregation.items()))
print("\n\n")
print(list(grouped_by_aggregation_Group_of_column.items()))
print("\n\n")
print(list(grouped_by.items())) # will through error
```
**Output:**
```
[(20, 10000), (21, 60000), (22, 90000), (23, 50000)]



[('salary', Age
            20    10000
            21    60000
            22    90000
            23    50000
Name: salary, dtype: int64)]


Traceback (most recent call last):
  File "E:\yadnesh2024\code\PYTHON\Pandas\PandasPartTwo.py", line 153, in <module>
    print(list(grouped_by.items()))
               ^^^^^^^^^^^^^^^^
  File "E:\yadnesh2024\code\PYTHON\Pandas\.venv\Lib\site-packages\pandas\core\groupby\groupby.py", line 1363, in __getattr__
    raise AttributeError(
AttributeError: 'DataFrameGroupBy' object has no attribute 'items'
```
3. **using for loop**
     - as you know groupby function return the list we apply for loop to print the output 
     - just make sure on which list you are applying the loop
     - for loop will automatically type cast the result into the list on the basis of which syntax you have use i.e, `grouped_dataset` or `grouped_dataset.items()` 



[Go To Top](#content)

---