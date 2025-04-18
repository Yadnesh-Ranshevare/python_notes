# Content
1. [Introduction](#introduction) 
2. [Installation](#installation)
3. [NumPy Array ](#numpy-array)
4. [Array function](#array-function)
5. [Array operation](#array-operation)

# Introduction

### What is NumPy?
**NumPy** (short for **Numerical Python**) is a powerful Python library used for numerical and scientific computing.
### 🧠 Why use NumPy?
If you're working with numbers, especially in **arrays**, **matrices**, or need to do math operations quickly, NumPy is perfect. It’s way faster and more efficient than using Python lists.


### Scalar vs vector vs Matrix vs Tensor
| Name | Description | Example (Shape)|
|------|-------|-----|
| Scalar | Single number | 5 → shape ()|
| Vector | 1D array | [1, 2, 3] → shape (3,)|
| Matrix | 2D array (rows × columns) | [[1, 2], [3, 4]] → shape (2, 2)|
| Tensor | nD array (3D, 4D, ...) | [ [ [1] , [2] ] , [ [3] , [4] ] ] → shape (2, 2, 1)|

### 🔧 C Language Backend
- NumPy is written in C and Python.

- The heavy number-crunching part (array operations) is done in C, which makes it super fast compared to plain Python lists.

- Python just provides a user-friendly interface.


### Popular Libraries Built on NumPy
**NumPy is the base, and all these libraries use NumPy arrays** internally to process and analyze data efficiently.
Framework | Purpose
---|---
**SciPy** | Scientific computing (math, physics, engineering)
**Pandas** | Data analysis using DataFrames (like Excel in code)
**Matplotlib** | Plotting and visualization (graphs, charts)
**Seaborn** | Advanced statistical plots (built on Matplotlib)
**Scikit-learn** | Machine learning (classification, clustering, etc.)
**TensorFlow / PyTorch** | Deep learning using tensor operations (NumPy-like)
**OpenCV** | Computer vision (images as NumPy arrays)


[Go to Top](#content)

---

# Installation
**Note: Although we can write Numpy code in plain python file, we generally learn Numpy in jupyter notebook for simplicity**\
[Click here to learn about jupyter notebook](../readme.md)
1. create the virtual environment
```bash
python -m venv venv
```
2. activate the virtual environment
```bash
venv\scripts\activate       # for window
source env/bin/activate   # on Mac/Linux
``` 
3. install Numpy
```bash
pip install numpy
```

[Go to Top](#content)

---


# NumPy Array 

1. import numpy
```py
import numpy as np
```
2. use `np.array()` to initialize the array 
```py
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],[4,5,6]])
``` 
**note: np.array() always accept the single list ( this single list can contain the multiple lists which represent the multiple demission )**


## array vs list
lets assume we want to perform a simple multiplication on the 2D matrix given as 
```
 [[1,2,3,4,5],[6,7,8,9,10]]
```
#### 1. list

by using normal python list
```py
list = [[1,2,3,4,5],[6,7,8,9,10]]
print("list multiplication", list*2)
```
**output:**
```bash
list multiplication [[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]
```
**In Python, when you use the * operator on a list, it replicates the entire list (or sublists) a specified number of times. This is not element-wise multiplication, but rather a repetition of the list.**\
**Although it is possible to perform the element wise multiplication in basic python but the process is time consuming and get complex as dimension of the matrix increases**\
eg., for 1D array
```py
list = [1,2,3,4,5]
new_list = [i*2 for i in list]
print("new list",new_list)
```
**output:**
```bash
new list [2, 4, 6, 8, 10]
```

#### 2. Array

 by using numpy array
```py
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("array multiplication", arr*2)
```
**output:**
```bash
array multiplication [[ 2  4  6]
 [ 8 10 12]]
```
**To perform element-wise multiplication of lists (or arrays) in Python, you need to use something that supports element-wise operations, such as NumPy.**

**`broadcast:` when we perform any mathematical operation ( +, -, /, * ) between vector ( 1D array ) and scalar this operation will be executed on each element of that vector**

#### Time Comparison
```py
import time

start_time = time.time() # current time in seconds 

list = [i for i in range(1000000)] # creating a list with 1000000 element

new_list = [i*2 for i in list]
print('time require to to perform the list multiplication',time.time() - start_time)


start_time = time.time()  # current time in seconds 

arr = np.array(list)
new_arr = arr*2
print('time require to to perform the array multiplication',time.time() - start_time)
```

**output:**
```bash
time require to to perform the list multiplication 0.11458492279052734
time require to to perform the array multiplication 0.0391087532043457
```
**note: this time can be vary because of various reason but in most of the cases array perform the multiplication in less time than that of list**

[Go to Top](#content)

---

# Array function
### 1. `.arange(start,stop,step):`
 create the array which start from `start` ends at `stop` and increases with each `step` size
```py
a = np.arange(0,20,2)
print(a)
```
**output:**
```bash
[ 0  2  4  6  8 10 12 14 16 18]
```
**Note: last digit ( 20 ) of stop is not included**
### 2. `.zeros((row,column)):` 
create the array of row x column contain all values as 0
```py
zero = np.zeros((2,3))
print(zero)
````
**output:**
```bash
[[0. 0. 0.]
 [0. 0. 0.]]
```


### 3. `.ones((row,column)):`
create the array of row x column contain all values as 1
```py
ones = np.ones((2,3))
print(ones)
```
**output:**
```bash
[[1. 1. 1.]
 [1. 1. 1.]]
```

### 4. `.full((row,column),element):`
create the array of row x column contain all values as given element
```py
full = np.full((2,3),5)
print(full)
```
**output:**
```bash
[[5 5 5]
 [5 5 5]]
```
### 5. `.random.random((row,column)):`
create the array of row x column contain random numbers between 1 & 0
```py
random = np.random.random((2,3))
print(random)
```
**output:**
```bash
[[0.29485735 0.31656954 0.66649625]
 [0.09152994 0.42496229 0.1134094 ]]
```
### 6. `.shape:` 
returns the number of rows and column of the array
```py
arr = np.array([[1,2,3],[4,5,6]])
print("shape",arr.shape)
```
**output:**
```
shape (2, 3)
```
### 7. `.ndim:` 
returns the number of dimension of the array
```py
arr = np.array([[1,2,3],[4,5,6]])
print("dimension",arr.ndim)
```
**output:**
```
dimension 2
```
### 8. `.size:` 
returns the total number of element of the array
```py
arr = np.array([[1,2,3],[4,5,6]])
print("size",arr.size)
```
**output:**
```
size 6
```
### 9. `.dtype:` 
returns the data type of the array
```py
arr = np.array([[1,2,3],[4,5,6]])
print("data type",arr.dtype)
```
**output:**
```
data type int64
```
### 10. `.reshape(row,column):` 
convert the provided array into given row x column format
```py
arr = np.arange(12)
print("original array",arr)

reshaped = arr.reshape(3,4)
print("3 x 4 reshaped array \n",reshaped)

reshaped = arr.reshape(4,3)
print("4 x 3 reshaped array \n",reshaped)
```
**output:**
```
original array [ 0  1  2  3  4  5  6  7  8  9 10 11]
3 x 4 reshaped array 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
4 x 3 reshaped array 
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
```
**Note: make sure that provided reshape is valid for the array if its  not then the code will through error cannot reshape array**
```py
arr = np.arange(12)
print("original array",arr)

reshaped = arr.reshape(4,4) # this will through an error as we cannot have 4 x 4 array with just 12 element
print("4 x 4 reshaped array \n",reshaped)
```

### 11. `.flatten():` 
convert the n dimension array into 1D array
```py
arr = np.array([[1,2,3],[4,5,6]])
print("original array\n",arr)

arr = arr.flatten()
print("flattened array",arr)
```
**output:**
```
original array
 [[1 2 3]
 [4 5 6]]
flattened array [1 2 3 4 5 6]
```
**Note:**
- **Returns a copy of the original array.**

- **The original array is not affected if you change the flattened one.**
```py
a = np.array([[1, 2], [3, 4]])
b = a.flatten()

b[0] = 100
print("Original array:\n", a)  # a is not changed
print("\nFlattened copy:\n", b)
```
**output:**
```bash
Original array:
 [[1 2]
 [3 4]]

Flattened copy:
 [100   2   3   4]
```

### 12. `.ravel():` 
convert the n dimension array into 1D array
```py
arr = np.array([[1,2,3],[4,5,6]])
print("original array\n",arr)

arr = arr.ravel()
print("ravel array",arr)
```
**output:**
```
original array
 [[1 2 3]
 [4 5 6]]
ravel array [1 2 3 4 5 6]
```
**Note:**
- **Returns a view (when possible) of the original array.**

- **If you modify the result, the original array may change too (if it's a view).**
- **Faster because it avoids copying when possible.**
- **doesn’t always return a view. If the array is not contiguous in memory, it will return a copy instead.**
```py
a = np.array([[1, 2], [3, 4]])
b = a.ravel()

b[0] = 100
print("Original array:\n", a)  # a *may* change if b is a view
print("\nRaveled view:\n", b)
```
**output:**
```bash
Original array:
 [[100   2]
 [  3   4]]

Raveled view:
 [100   2   3   4]
```

### 13. `.T:`
return the transpose of the given array
```py
arr = np.arange(12)

reshaped = arr.reshape(3,4)
print("3 x 4 reshaped array \n",reshaped)

transpose = reshaped.T
print("\ntransposed array\n",transpose)
```
**output:**
```
3 x 4 reshaped array 
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

transposed array
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
```

### 14. `np.sum():`
- use to calculate the sum of the row or column of an array
- it return the array having sum of each column or row init
1. **1D array:**
```py
# data structure: [ 2021, 2022, 2023, 2024]
sales_data = np.array([ 100, 200, 300, 400])


# final = total_sales.sum()
final = np.sum(sales_data)
print("\ntotal sales per restaurant:\n", final)
```
**output:**
```
total sales per restaurant:
 1000
```
2. **2D array**\
**axis = 0:** column wise adding\
**axis = 1:** row wise adding
```py
# data structure: [ 2021, 2022, 2023, 2024]
sales_data = np.array([
    [ 100, 200, 300, 400], # shop 1
    [ 150, 250, 350, 450], # shop 2
    [ 200, 300, 400, 500], # shop 3
    [ 250, 350, 450, 550], # shop 4
    [ 300, 400, 500, 600]  # shop 5
])

# total scales per year

# total_sales = sales_data.sum(axis=0)
total_sales = np.sum(sales_data, axis=0)
print("\ntotal sales per year:\n", total_sales)
```
**output:**
```
total sales per year:
 [1000 1500 2000 2500]
```

### 15. `np.min() vs np.max() vs np.mean():`
- `np.min():` return the minimum value either from row or column
- `np.max():` return the maximum value either from row or column
- `np.mean():` return the average value of the row or the column
1. **1D array**
```py
# data structure: [ 2021, 2022, 2023, 2024]
sales_data = np.array([ 100, 200, 300, 400])

# minimum sales per shop
min_sales = np.min(sales_data)
print("\nminimum sales per shop:\n", min_sales)

# maximum sales per year
max_sales = np.max(sales_data)
print("\nmaximum sales per year:\n", max_sales)

# avg sales pre shop
avg_sales = np.mean(sales_data)
print("\navg sales per shop:\n", avg_sales)
```
**output:**
```
minimum sales per shop:
 100

maximum sales per year:
 400

avg sales per shop:
 250.0
```
2. **2D array**\
**axis = 0:** column wise operation\
**axis = 1:** row wise operation
```py
# data structure: [ 2021, 2022, 2023, 2024]
sales_data = np.array([
    [ 100, 200, 300, 400], # shop 1
    [ 150, 250, 350, 450], # shop 2
    [ 200, 300, 400, 500], # shop 3
    [ 250, 350, 450, 550], # shop 4
    [ 300, 400, 500, 600]  # shop 5
])

# minimum sales per shop
min_sales = np.min(sales_data, axis=1)
print("\nminimum sales per shop:\n", min_sales)

# maximum sales per year
max_sales = np.max(sales_data, axis=0)
print("\nmaximum sales per year:\n", max_sales)

# avg sales pre shop
avg_sales = np.mean(sales_data, axis=1)
print("\navg sales per shop:\n", avg_sales)
```
**output:**
```
minimum sales per shop:
 [100 150 200 250 300]

maximum sales per year:
 [300 400 500 600]

avg sales per shop:
 [250. 300. 350. 400. 450.]
```
### 15. `np.cumsum():`
used to perform the cumulative sum ( adds each element to the sum of all previous elements )\
eg.,\
Suppose you have a list of numbers:
```py
a = np.array([10, 20, 30, 40])
```
If you do:
```py
np.cumsum(a)
```
You get:
```py
array([10, 30, 60, 100])
```
Here's what happens:

- 10 → just the first number
- 10 + 20 = 30
- 30 + 30 = 60
- 60 + 40 = 100

**For 2D array**\
**axis = 0:** column wise operation\
**axis = 1:** row wise operation
```py
# data structure: [ 2021, 2022, 2023, 2024]
sales_data = np.array([
    [ 100, 200, 300, 400], # shop 1
    [ 150, 250, 350, 450], # shop 2
    [ 200, 300, 400, 500], # shop 3
    [ 250, 350, 450, 550], # shop 4
    [ 300, 400, 500, 600]  # shop 5
])

# cumulative sum
cumulative_sum = np.cumsum(sales_data, axis=1)
print("\ncumulative sum:\n", cumulative_sum)
```
**output:**
```
cumulative sum:
 [[ 100  300  600 1000]
 [ 150  400  750 1200]
 [ 200  500  900 1400]
 [ 250  600 1050 1600]
 [ 300  700 1200 1800]]
```

### 16. `np.vectorize():`
- used to create the custom vector methods which on applying on array performs an operation on every element of that array
- `np.vectorize()` accept any python code and later on execute that code on every element of array
```py
shops = ["shop1", "shop2", "shop3", "shop4", "shop5"]

vectorize_upper = np.vectorize(str.upper)

shops = vectorize_upper(shops)
print(shops)
```
**output:**
```
['SHOP1' 'SHOP2' 'SHOP3' 'SHOP4' 'SHOP5']
```


[Go to Top](#content)

---

# Array Operation

## Array slicing
```py
arr = np.arange(12)
print("original array",arr)
print("basics slicing",arr[2:7])  # 7 excluded
print("with step slicing",arr[2:10:2])
print("negative indexing",arr[-3])
```
**output**
```
original array [ 0  1  2  3  4  5  6  7  8  9 10 11]
basics slicing [2 3 4 5 6]
with step slicing [2 4 6 8]
negative indexing 9
```

## Element access
```py
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("original array\n",arr)
print("specific element",arr[1,2])  # row_index x column_index
print("entire row",arr[1])  # to access the row at 1st index
print("entire column",arr[:,1]) # to access the column at 1st index
```
**output:**
```
original array
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
specific element 6
entire row [4 5 6]
entire column [2 5 8]
```
**Note: indexing start from zero for both row and columns**


## Array sorting
1. basics sorting using `.sort` method
```py
unsortedArr = np.array([4,2,6,1,3,5])
sortedArr = np.sort(unsortedArr)

print("unsorted array",unsortedArr)
print("sorted array",sortedArr)
```
**output:**
```
unsorted array [4 2 6 1 3 5]
sorted array [1 2 3 4 5 6]
```

2. 2D array sorting

**axis = 0:** column wise sorting\
**axis = 1:** row wise sorting
```py
unsortedArr_2d = np.array([[4,2,6],[1,3,5],[9,8,7]])

row_sortedArr_2d = np.sort(unsortedArr_2d,axis=1)
col_sortedArr_2d = np.sort(unsortedArr_2d,axis=0)

print("unsorted 2d array\n",unsortedArr_2d)

print("\nrow wise sorted 2d array\n",row_sortedArr_2d)
print("\ncolumn wise sorted 2d array\n",col_sortedArr_2d)
```
**output:**
```
unsorted 2d array
 [[4 2 6]
 [1 3 5]
 [9 8 7]]

row wise sorted 2d array
 [[2 4 6]
 [1 3 5]
 [7 8 9]]

column wise sorted 2d array
 [[1 2 5]
 [4 3 6]
 [9 8 7]]
```


## Filtration

### Normal Filtrating

```py
arr = np.arange(12)
print("original array",arr)

even_arr = arr[arr%2==0]    # need to use same name inside the square bracket
print("even number array",even_arr)
```

**output:**
```
original array [ 0  1  2  3  4  5  6  7  8  9 10 11]
even number array [ 0  2  4  6  8 10]
```

 ### Mask:
 
creates a array of True and false on the basic of condition which then pass as a prop for filtering the array
```py
arr = np.arange(12)
print("original array",arr)

mask = arr%2==0

print("mask array",mask)
print("filtered array",arr[mask])
```
**output:**
```
original array [ 0  1  2  3  4  5  6  7  8  9 10 11]
mask array [ True False  True False  True False  True False  True False  True False]
filtered array [ 0  2  4  6  8 10]
```
### np.where()

returns the array containing the index where condition becomes true
```py
arr = np.arange(12)
print("original array\n",arr)

where_result = np.where(arr%2==0)

print("where result\n",where_result)
print("selected element\n",arr[where_result])
```
**output:**
```
original array
 [ 0  1  2  3  4  5  6  7  8  9 10 11]
where result
 (array([ 0,  2,  4,  6,  8, 10]),)
selected element
 [ 0  2  4  6  8 10]
```
**you can also manipulate the where_result array by passing the x and y parameter**
```py
arr = np.arange(12)
print("original array\n",arr)

where_result = np.where(arr%2==0,"x","Y")
print("where result\n",where_result)
```
**If `arr%2==0` condition becomes true then it will return the "X" and if the condition becomes false it will return the "Y" this syntax works similar to if-else statements**

**output:**
```
original array
 [ 0  1  2  3  4  5  6  7  8  9 10 11]
where result
 ['x' 'Y' 'x' 'Y' 'x' 'Y' 'x' 'Y' 'x' 'Y' 'x' 'Y']
``` 
**Note: you have to provide both x and y parameter or nighter of them, it doesn't work with only one parameter**\
**In case, if you want to give only one parameter you can pass original array as another parameter**
```py
arr = np.arange(12)
print("original array\n",arr)

where_result = np.where(arr%2==0,'X',arr)   # passing the original array as I want to provide only x parameter
print("where result\n",where_result)
```
**If condition becomes true it will return the 'X' else it return the original value**
**output:**
```
original array
 [ 0  1  2  3  4  5  6  7  8  9 10 11]
where result
 ['X' '1' 'X' '3' 'X' '5' 'X' '7' 'X' '9' 'X' '11']
```
**Note: numPy is efficient for dealing with similar datatype so if you provide the different datatype it tries to convert them into similar datatype**


## Indexing

```py
arr = np.arange(1,20,2)
print("original array\n",arr)

idx = [1,4,6,8]
print("index array\n",idx)

print("selected element\n",arr[idx])
```
**output:**
```
original array
 [ 1  3  5  7  9 11 13 15 17 19]
index array
 [1, 4, 6, 8]
selected element
 [ 3  9 13 17]
```
prints the array containing the element present at index mention in idx array


## Adding new element

1. **1D array**\
you can not use + operator to concatenate the two array as it will perform the basic array addition instead of concatenating the two 1D array\
`.concatenate():`
```py
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("adding two array",arr1+arr2)  # array addition
print("concatenated array",np.concatenate((arr1,arr2)))
``` 
**output:**
```
adding two array [5 7 9]
concatenated array [1 2 3 4 5 6]
```
2. **2D array**\
we can either perform the row addition or column addition

`.vstack():` used to add new row in original array
```py
arr_2d = np.array([[1,2,3],[4,5,6]])
new_row = np.array([7,8,9])

with_new_row = np.vstack((arr_2d,new_row))

print("original array\n",arr_2d)
print("with new row\n",with_new_row)
```
**output:**
```
original array
 [[1 2 3]
 [4 5 6]]
with new row
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
```
`.hstack():` used to add new column in original array
```py
arr_2d = np.array([[1,2,3],[4,5,6]])
new_column = np.array([[7],[8]])


with_new_column = np.hstack((arr_2d,new_column))

print("original array\n",arr_2d)
print("with new column\n",with_new_column)
```
**output:**
```
original array
 [[1 2 3]
 [4 5 6]]
with new column
 [[1 2 3 7]
 [4 5 6 8]]
```
**Note: in both the .vstack() and .hstack() make sure the added row or column is marinating the respective dimension of the original array i.e, if you are adding the new row make sure new row has same number of element as that of the row of original array same goes for column**

## Removing / np.delete()
1. **1D array**\
pass the array and the index of the element to delete that element for the array 
```py
arr = np.array([[1,2,3, 4,5,6]])

deleted_arr = np.delete(arr,1)

print("deleted column\n",deleted_arr)
```
**output:**
```
deleted column
 [1 3 4 5 6]
```


2. **2D array**\
pass an axis extra argument along with array and index\
`axis=0:` index refers to the row\
`axis=1:` index refers to the column

**Note: index will be of the row index or column index**
```py
arr = np.array([[1,2,3],[4,5,6]])
print("original array\n",arr)

deleted = np.delete(arr,1,axis=0)
print("deleted row\n",deleted)

deleted = np.delete(arr,1,axis=1)
print("deleted column\n",deleted)
```
**output:**
```
original array
 [[1 2 3]
 [4 5 6]]
deleted row
 [[1 2 3]]
deleted column
 [[1 3]
 [4 6]]
```

Note: you can pass index in the form of array to delete the multiple element for the array
--
```py
arr_1D = np.array([[1,2,3, 4,5,6]])

deleted_arr = np.delete(arr_1D,[1,3])  # delete the element st the 1st and 3rd index of arr_1D

print("original 1D array\n",arr_1D)
print("deleted column\n",deleted_arr)


arr_2D = np.array([[1,2,3],[4,5,6]])

deleted = np.delete(arr_2d,[1,2],axis=1) #delete the column at index 1 and 2 from arr_2D

print("\noriginal 2D array\n",arr_2D)
print("deleted column\n",deleted)
```
**output:**
```
original 1D array
 [[1 2 3 4 5 6]]
deleted column
 [1 3 5 6]

original 2D array
 [[1 2 3]
 [4 5 6]]
deleted column
 [[1]
 [4]]
```

[Go to Top](#content)

---
 