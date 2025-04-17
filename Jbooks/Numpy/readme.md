# Content
1. [Introduction](#introduction) 
2. [Installation](#installation)


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