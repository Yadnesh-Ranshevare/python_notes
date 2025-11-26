# Content
1. [Introduction](#introduction)
2. [prerequisites](#prerequisites)
3. [Installation](#installation)

---

# Introduction
sklearn, also called scikit-learn, is a powerful machine learning library in Python.

It gives you ready-made tools to perform all the machine learning steps you need — from preparing data to training and evaluating models.

### Why sklearn is used?
Machine learning involves many steps:
1. Preparing data
2. Choosing an algorithm
3. Training the model
4. Testing the model
5. Evaluating performance

Instead of writing everything from scratch, sklearn provides clean, simple, and optimized functions for all these tasks.

### What sklearn contains?

1. **Preprocessing tools**\
These are tools used before training:
    - Scaling data (StandardScaler, MinMaxScaler)
    - Encoding categorical values (LabelEncoder, OneHotEncoder)
    - Handling missing values (Imputer)
    - Splitting data (train_test_split)
2. **Supervised learning algorithms**\
These algorithms learn from labeled data.
    - Classification: KNN, SVM, Decision Tree, Random Forest, Naive Bayes
    - Regression: Linear Regression, Polynomial Regression, Lasso, Ridge
3. **Unsupervised learning algorithms**\
These work without labels.
    - K-Means
    - Hierarchical Clustering
    - PCA (Dimensionality Reduction)
4. **Model selection tools**\
Helps you choose the best model.
    - train_test_split
    - cross-validation
    - GridSearchCV (for tuning parameters)
5. **Model evaluation tools**\
Used to measure how good your model is.
    - accuracy
    - precision, recall
    - confusion matrix
    - mean squared error (MSE)


[Go To Top](#content)

---
# Prerequisites
Here are the prerequisites for learning and using sklearn

### 1. Basic Python
You must know:
- variables
- lists
- functions
- loops
- basic OOP idea (classes & objects)

### 2. NumPy (basic understanding)
Because sklearn works internally with arrays, not normal Python lists.

You should know:
- arrays (NumPy array)
- basic operations (reshape, indexing)
- math ops (mean, sum)

### 3. Pandas (basic understanding)
Because datasets are usually stored in:
- DataFrames
- CSV files
- Excel files

You should know:
- reading data
- selecting columns
- filtering rows

### 4. Basic Math for ML

Not too deep, just basics:
- mean, median
- standard deviation
- distance between points
- probability basics
- linear equations

### 5. Basic Machine Learning Concepts

Before using sklearn, you should know what you are trying to do:
- Classification → predict categories
- Regression → predict numbers
- Clustering → group similar items
- Training/Test Split → how to evaluate models


[Go To Top](#content)

---
# Installation

### Using uv
step 1. initiate uv environment
```bash
uv init
```
step 2. install necessary packages
```bash
uv add scikit-learn numpy pandas matplotlib jupyterlab
```
Step 3: Activate the Virtual Environment
```bash
.env\Scripts\activate  # windows
source .env/bin/activate   # macOS / Linux
```
step 4: launch the jupiter lab
```bash
jupyter lab
```

### Using pip or python
Step 1: Create a Virtual Environment
```bash
python -m venv myenv    # for windows
python3 -m venv myenv   # for macOS / Linux
```
Step 2: Activate the Virtual Environment
```bash
myenv\Scripts\activate  # windows
source myenv/bin/activate   # macOS / Linux
```
Step 3: Install necessary packages
```bash
pip install scikit-learn numpy pandas matplotlib jupyterlab
```
step 4: launch the jupiter lab
```bash
jupyter lab
```

[Go To Top](#content)

---