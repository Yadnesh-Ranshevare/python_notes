# Content
1. [Introduction](#introduction) 
2. [Installation](#installation)
3. [NumPy Array ](#numpy-array)
4. [Array function](#array-function)


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

 


 