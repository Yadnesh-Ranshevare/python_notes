# Content

1. [Problem Statement](#problem-statement)
2. [Basic Setup](#basic-setup)
3. [Get the Basic information about the dataset](#get-the-basic-information-about-the-dataset)
4. [Delete some feature](#delete-some-feature)
5. [Converting Categorical data ito numeric data](#converting-categorical-data-ito-numeric-data)
    - [gender: one hot encoding using .map to updated](#convert-gender-from-categorical-to-numeric)
    - [Age: ordinal encoding](#convert-age-from-categorical-to-numeric)
    - [City_Category: one hot encoding by replacing the columns](#convert-city_category-from-categorical-to-numeric)
6. [Handling missing Values](#handling-missing-values)
7. [Change the datatype - fom object/string to integer](#change-the-datatype---fom-objectstring-to-integer)

> After performing all of the above steps your dataset will be ready for machine learning and to solve the given [problem statement](#problem-statement) 

---

# Problem Statement

A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month.
The data set also contains customer demographics (age, gender, marital status, city_type, stay_in_current_city), product details (product_id and product category) and Total purchase_amount from last month.

Now, they want to build a model to predict the purchase amount of customer against various products which will help them to create personalized offer for customers against different products.

[Go To Top](#content)

---

# Basic Setup

> Make sure you download the dataset from https://www.kaggle.com/sdolezel/black-friday?select=train.csv it will give two files i.e train.csv and test.csv

### 1. Import the necessary packages

```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```

### 2. read the train Dataset

```py
df_train=pd.read_csv('blackFriday_train.csv')
df_train.head()
```

### 3. read the test dataset

```py
df_test=pd.read_csv('blackFriday_test.csv')
df_test.head()
```

### Merge both of the dataset

```py
df=df_train.append(df_test)
df.head()
```

[Go To Top](#content)

---

# Get the Basic information about the dataset

### 1. get the basic info about the column

```py
df.info()
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 783667 entries, 0 to 233598
Data columns (total 12 columns):
 #   Column                      Non-Null Count   Dtype
---  ------                      --------------   -----
 0   User_ID                     783667 non-null  int64
 1   Product_ID                  783667 non-null  object
 2   Gender                      783667 non-null  object
 3   Age                         783667 non-null  object
 4   Occupation                  783667 non-null  int64
 5   City_Category               783667 non-null  object
 6   Stay_In_Current_City_Years  783667 non-null  object
 7   Marital_Status              783667 non-null  int64
 8   Product_Category_1          783667 non-null  int64
 9   Product_Category_2          537685 non-null  float64
 10  Product_Category_3          237858 non-null  float64
 11  Purchase                    550068 non-null  float64
dtypes: float64(3), int64(4), object(5)
memory usage: 77.7+ MB
```

### 2. get the info about the numerical data

```py
df.describe()
```

**Output:**

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Occupation</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7.836670e+05</td>
      <td>783667.000000</td>
      <td>783667.000000</td>
      <td>783667.000000</td>
      <td>537685.000000</td>
      <td>237858.000000</td>
      <td>550068.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.003029e+06</td>
      <td>8.079300</td>
      <td>0.409777</td>
      <td>5.366196</td>
      <td>9.844506</td>
      <td>12.668605</td>
      <td>9263.968713</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.727267e+03</td>
      <td>6.522206</td>
      <td>0.491793</td>
      <td>3.878160</td>
      <td>5.089093</td>
      <td>4.125510</td>
      <td>5023.065394</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000001e+06</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.001519e+06</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>9.000000</td>
      <td>5823.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.003075e+06</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>5.000000</td>
      <td>9.000000</td>
      <td>14.000000</td>
      <td>8047.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.004478e+06</td>
      <td>14.000000</td>
      <td>1.000000</td>
      <td>8.000000</td>
      <td>15.000000</td>
      <td>16.000000</td>
      <td>12054.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.006040e+06</td>
      <td>20.000000</td>
      <td>1.000000</td>
      <td>20.000000</td>
      <td>18.000000</td>
      <td>18.000000</td>
      <td>23961.000000</td>
    </tr>
  </tbody>
</table>
</div>

[Go To Top](#content)

---

# Delete some feature
In the dataset there is a column name `User_ID` which has no use in EDA part it is just a unique identifier and is not getting use in further analysis, therefor we can delete it 
```py
df.drop(['User_ID'],axis=1,inplace=True)
df.head()
```
**Output:**
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>P00069042</td>
      <td>F</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8370.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>P00248942</td>
      <td>F</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>6.0</td>
      <td>14.0</td>
      <td>15200.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>P00087842</td>
      <td>F</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1422.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>P00085442</td>
      <td>F</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1057.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>P00285442</td>
      <td>M</td>
      <td>55+</td>
      <td>16</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7969.0</td>
    </tr>
  </tbody>
</table>
</div>

[Go To Top](#content)

---
# Converting Categorical data ito numeric data

1. [gender](#convert-gender-from-categorical-to-numeric)
2. [Age](#convert-age-from-categorical-to-numeric)
3. [City_Category](#convert-city_category-from-categorical-to-numeric)


### Convert gender from categorical to numeric
- for `M` -> 0
- for `F` -> 1

#### Approach 1: delete the original gender column and replace it with new one
- `get_dummies()` :- converts categorical data (text labels) into numeric columns — called dummy variables or one-hot encoding.
- it is uses [one-Hot encoding](https://github.com/Yadnesh-Ranshevare/python_notes/blob/main/EDA/readdme.md#feature-encoding) which is a type of encoding perform in feature engineering
- we first delete the original gender column then create the new one and then add the new column into the dataset 
```py
df['Gender']=pd.get_dummies(df['Gender'],drop_first=1)
```

#### Approach 2: just change the value without deleting the original column
- we use `.map` loop to traverse over the complete dataset and update the value of gender during each iteration
```py
df['Gender']=df['Gender'].map({'F':0,'M':1})
df.head()
```
**Output:**
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>P00069042</td>
      <td>0</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8370.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>P00248942</td>
      <td>0</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>6.0</td>
      <td>14.0</td>
      <td>15200.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>P00087842</td>
      <td>0</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1422.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>P00085442</td>
      <td>0</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1057.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>P00285442</td>
      <td>1</td>
      <td>55+</td>
      <td>16</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7969.0</td>
    </tr>
  </tbody>
</table>
</div>


### Convert Age from categorical to numeric


#### Step 1: find all the unique value of ages
```py
df['Age'].unique()
```
**Output:**
```
array(['0-17', '55+', '26-35', '46-50', '51-55', '36-45', '18-25'],
      dtype=object)
```

#### step 2: encoding

**Ordinal Encoding**: converts categories into integer numbers, keeping their order or rank (if one exists).
- from above data we can say that
    - `'0-17'` -> rank 1
    - `'18-25'` -> rank 2
    - `'26-35'` -> rank 3
    -  `'36-45'` -> rank 4
    - `'46-50'` -> rank 5
    - `'51-55'` -> rank 6
    - `'55+'` -> rank 7


**Syntax 1: using .map**
```py
df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-35':3,'36-45':4,'46-50':5,'51-55':6,'55+':7})
```
**Syntax 2: using sklearn**
```py
##second technqiue
from sklearn import preprocessing
 
# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
 
# Encode labels in column 'species'.
df['Age']= label_encoder.fit_transform(df['Age'])
 
df['Age'].unique()
```

**Final dataset:**
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>P00069042</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8370.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>P00248942</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>6.0</td>
      <td>14.0</td>
      <td>15200.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>P00087842</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1422.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>P00085442</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1057.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>P00285442</td>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7969.0</td>
    </tr>
  </tbody>
</table>
</div>


### Convert City_Category from categorical to numeric 

will be using one-hot encoding to convert this categorical data into integral and to do that 
1. create the new columns for each category with data as follow
    - `1` -> belong to this category
    - `0` -> does not belong to this category
2. delete the original column 
3. append the new columns into the dataset

**Example:**
| Name  | Category |
| ----- | -------- |
| Aditi | A        |
| Rahul | B        |
| Sneha | A        |
| Kiran | C        |

**for this the final output dataset will be:**
| Name  | A | B | C |
| ----- | - | - | - |
| Aditi | 1 | 0 | 0 |
| Rahul | 0 | 1 | 0 |
| Sneha | 1 | 0 | 0 |
| Kiran | 0 | 0 | 1 |


#### Using code:
```py
# create the new columns
df_city=pd.get_dummies(df['City_Category'],drop_first=True)

# append them into the original dataset
df=pd.concat([df,df_city],axis=1)

# remove the original City_Category column from the dataset
df.drop('City_Category',axis=1,inplace=True)

print(df.head())
```

**Output:**
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>P00069042</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8370.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>P00248942</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>6.0</td>
      <td>14.0</td>
      <td>15200.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>P00087842</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1422.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>P00085442</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1057.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>P00285442</td>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>4+</td>
      <td>0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7969.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

[Go To Top](#content)

---
# Handling missing Values


### Step 1: Find how many null/missing values are there in the dataset
```py
df.isnull().sum()
```
**Output:**
```
Product_ID                         0
Gender                             0
Age                                0
Occupation                         0
Stay_In_Current_City_Years         0
Marital_Status                     0
Product_Category_1                 0
Product_Category_2            245982
Product_Category_3            545809
Purchase                      233599
B                                  0
C                                  0
dtype: int64
```
Here, we can see that:
- `Product_Category_2` has `245982` missing values
- `Product_Category_3` has `545809` missing values
- `Purchase` has `233599` missing values

### Step 2: check what type of data is present in the respective column

```py
df['Product_Category_2'].unique()
```
**Output:**
```
array([nan,  6., 14.,  2.,  8., 15., 16., 11.,  5.,  3.,  4., 12.,  9.,
       10., 17., 13.,  7., 18.])
```
- `.unique` return the set(no duplicates) of data present into the respective column
- with this we know what kind of data is present in this respective column
- from our observation we can see that `Product_Category_2` contains discrete, not continuous numbers.

### Step 3: understand the distribution of present value
```py
df['Product_Category_2'].value_counts()
```
**Output:**
```
8.0     91317
14.0    78834
2.0     70498
16.0    61687
15.0    54114
5.0     37165
4.0     36705
6.0     23575
11.0    20230
17.0    19104
13.0    15054
9.0      8177
12.0     7801
10.0     4420
3.0      4123
18.0     4027
7.0       854
Name: Product_Category_2, dtype: int64
```
- now we know how each unique value is distributed in the given dataset

### Step 4: choose which value to fill 
since our column contain the discrete data we cannot fill mean or median, reason:
- A discrete variable takes specific distinct values — usually counts or categories.
- The mean might not be a valid discrete value.

solution:
- **mode**: the number (or category) that appears most often in your data.\
**Example**
    ```
    1, 2, 2, 3, 3, 3, 4
    ```
    - 1 appears → 1 time
    - 2 appears → 2 times
    - 3 appears → 3 times
    - 4 appears → 1 time

    Mode = 3 (because 3 appears the most)
- in pandas there is a inbuilt function called `mode()` that helps you find the mode on any dataset
    ```py
    df['Product_Category_2'].mode()[0]  # output -> 8.0
    ```
    - `.mode()` can return more than one mode if multiple values appear equally often.
    - `[0]` is uses so that pandas can find the most common (mode) value in the column Product_Category_2, and take the first one if there are multiple.
- once we fins the value of mode fill that value in place os missing values

### Step 5: fill the missing values
we use `fillna()` function of pandas to fill all of the missing values 
```py
df['Product_Category_2'] = df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])

print(df['Product_Category_2'].isnull().sum())  # to check whether any column is remain or not
```
**Output:**
```
0
```

> we perform same steps to handle the missing values of the `Product_Category_3` column as well

```py
df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])

print(df.head())
```
**Output:**
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Product_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>P00069042</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>8.0</td>
      <td>16.0</td>
      <td>8370.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>P00248942</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>6.0</td>
      <td>14.0</td>
      <td>15200.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>P00087842</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>8.0</td>
      <td>16.0</td>
      <td>1422.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>P00085442</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>14.0</td>
      <td>16.0</td>
      <td>1057.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>P00285442</td>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>4+</td>
      <td>0</td>
      <td>8</td>
      <td>8.0</td>
      <td>16.0</td>
      <td>7969.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

[Go To Top](#content)

---
# Change the datatype - fom object/string to integer

```py
df.info()
```
**Output:**
```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 783667 entries, 0 to 233598
Data columns (total 12 columns):
 #   Column                      Non-Null Count   Dtype  
---  ------                      --------------   -----  
 0   Product_ID                  783667 non-null  object 
 1   Gender                      783667 non-null  int64  
 2   Age                         783667 non-null  int64  
 3   Occupation                  783667 non-null  int64  
 4   Stay_In_Current_City_Years  783667 non-null  object 
 5   Marital_Status              783667 non-null  int64  
 6   Product_Category_1          783667 non-null  int64  
 7   Product_Category_2          783667 non-null  float64
 8   Product_Category_3          783667 non-null  float64
 9   Purchase                    550068 non-null  float64
 10  B                           783667 non-null  uint8  
 11  C                           783667 non-null  uint8  
dtypes: float64(3), int64(5), object(2), uint8(2)
memory usage: 67.3+ MB
```
from the above code output we get the general idea about the current state of our dataset along with the datatype of each column 
- we can see that almost every column has the int64 datatype
- only `Stay_In_Current_City_Years` has the datatype of object 
- in pandas string are generally define as objects
- therefor we need to change its datatype from object to int64

### understand the data
```py
df['Stay_In_Current_City_Years'].unique()
```
**Output:**
```
array(['2', '4+', '3', '1', '0'], dtype=object)
```
Here:
- `dtype=object`: means datatype is object
- we can also see that almost every value (`0`, `1`, `2`, `3`) in a specific number except `4+` which is a string
- hence if we able to convert the `4+` to only `4` we can say that, now our whole column hold the numbers ranging from `0` to `4`
- but just changing the value of `4+` to `4` will never change its datatype automatically, therefor we have tho change the datatype manually after changing `4+` 

```py
# changing 4+ -> 4
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+','')

# changing the datatype from object to string
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)

print(df.info())
```
**Output:**
```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 783667 entries, 0 to 233598
Data columns (total 12 columns):
 #   Column                      Non-Null Count   Dtype  
---  ------                      --------------   -----  
 0   Product_ID                  783667 non-null  object 
 1   Gender                      783667 non-null  int64  
 2   Age                         783667 non-null  int64  
 3   Occupation                  783667 non-null  int64  
 4   Stay_In_Current_City_Years  783667 non-null  int32  
 5   Marital_Status              783667 non-null  int64  
 6   Product_Category_1          783667 non-null  int64  
 7   Product_Category_2          783667 non-null  float64
 8   Product_Category_3          783667 non-null  float64
 9   Purchase                    550068 non-null  float64
 10  B                           783667 non-null  uint8  
 11  C                           783667 non-null  uint8  
dtypes: float64(3), int32(1), int64(5), object(1), uint8(2)
memory usage: 64.3+ MB
```
Now you can see our whole dataset is of same datatype i.e, numerical data

[Go To Top](#content)

---
