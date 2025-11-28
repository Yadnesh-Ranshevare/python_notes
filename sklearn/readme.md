# Content
1. [Introduction](#introduction)
2. [prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Dataset](#dataset)
    - [Split Data into X and Y](#split-data-into-x-and-y)
    - [Use return_X_y](#use-return_x_y)
    - [Import dataset as pandas frame](#import-dataset-as-pandas-frame)
    - [Custom dataset using make_](#custom-dataset-using-make_)
5. [Data Splitting](#data-splitting)
    - [unbalanced Split](#unbalanced-split)
    - [StratifiedShuffleSplit](#stratifiedshufflesplit)
6. [Preprocessing](#preprocessing)

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
# Dataset
In sklearn, a dataset simply means the data you use to train and test a machine learning model.

### 1. Built-in datasets
These are small example datasets used for learning and testing ML algorithms.

**Examples:**
- Iris dataset → flower classification
- Digits dataset → handwritten numbers
- Wine dataset → wine quality classification
- Breast Cancer dataset → medical classification

Sklearn provides two kinds of built-in dataset functions:

#### 1. `load_` Datasets
These datasets are small, lightweight, and already included inside sklearn.
They do NOT require an internet connection and are available instantly.

Examples:
- `load_iris()`
- `load_digits()`
- `load_wine()`
- `load_breast_cancer()`

Characteristics:
- Stored locally inside the sklearn package
- Fast to access
- Small size (KB to few MB)


#### 2. `fetch_` Datasets
These datasets are large and not included inside sklearn by default.
They need to be downloaded from the internet the first time.

Examples:
- `fetch_20newsgroups()`
- `fetch_california_housing()`
- `fetch_openml()`

Characteristics:
- Downloaded from the internet
- Stored in your system’s cache folder
- Usually bigger datasets (MB to GB)
- Suitable for advanced, real-world ML tasks

### 2. Your own dataset
Sklearn can also work with datasets you bring, such as:
- CSV files
- Excel files
- SQL database data
- Pandas DataFrames


### How sklearn represents a dataset    
Most sklearn datasets are structured like this:
- data → features (inputs)
- target → labels (outputs)
- feature_names → column names
- DESCR → description of the dataset

#### Very Simple Illustration:
Imagine a dataset for predicting if a person buys a product:
| Age | Salary | Buys |
| --- | ------ | ---- |
| 22  | 25000  | No   |
| 30  | 50000  | Yes  |
| 28  | 45000  | Yes  |

it return the dictionary that contain:
- data = Age, Salary
- target = Buys
- feature_names = ["Age", "Salary"]
- DESCR = description of what this dataset is about


### Example

```py
from sklearn.datasets import load_breast_cancer # built in dataset

data = load_breast_cancer()
print(data)
```
Output:

```
{'data': array([[1.799e+01, 1.038e+01, 1.228e+02, ..., 2.654e-01, 4.601e-01,
         1.189e-01],
        [2.057e+01, 1.777e+01, 1.329e+02, ..., 1.860e-01, 2.750e-01,
         8.902e-02],
        [1.969e+01, 2.125e+01, 1.300e+02, ..., 2.430e-01, 3.613e-01,
         8.758e-02],
        ...,
        [1.660e+01, 2.808e+01, 1.083e+02, ..., 1.418e-01, 2.218e-01,
         7.820e-02],
        [2.060e+01, 2.933e+01, 1.401e+02, ..., 2.650e-01, 4.087e-01,
         1.240e-01],
        [7.760e+00, 2.454e+01, 4.792e+01, ..., 0.000e+00, 2.871e-01,
         7.039e-02]], shape=(569, 30)),
 'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0,
        1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0,
        1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1,
        1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0,
        0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1,
        1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0,
        1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1,
        1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0,
        1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1,
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1,
        1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
        1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1,
        1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1]),
 'frame': None,
 'target_names': array(['malignant', 'benign'], dtype='<U9'),
 'DESCR': '.. _breast_cancer_dataset:\n\nBreast cancer Wisconsin (diagnostic) dataset\n--------------------------------------------\n\n**Data Set Characteristics:**\n\n:Number of Instances: 569\n\n:Number of Attributes: 30 numeric, predictive attributes and the class\n\n:Attribute Information:\n    - radius (mean of distances from center to points on the perimeter)\n    - texture (standard deviation of gray-scale values)\n    - perimeter\n    - area\n    - smoothness (local variation in radius lengths)\n    - compactness (perimeter^2 / area - 1.0)\n    - concavity (severity of concave portions of the contour)\n    - concave points (number of concave portions of the contour)\n    - symmetry\n    - fractal dimension ("coastline approximation" - 1)\n\n    The mean, standard error, and "worst" or largest (mean of the three\n    worst/largest values) of these features were computed for each image,\n    resulting in 30 features.  For instance, field 0 is Mean Radius, field\n    10 is Radius SE, field 20 is Worst Radius.\n\n    - class:\n            - WDBC-Malignant\n            - WDBC-Benign\n\n:Summary Statistics:\n\n===================================== ====== ======\n                                        Min    Max\n===================================== ====== ======\nradius (mean):                        6.981  28.11\ntexture (mean):                       9.71   39.28\nperimeter (mean):                     43.79  188.5\narea (mean):                          143.5  2501.0\nsmoothness (mean):                    0.053  0.163\ncompactness (mean):                   0.019  0.345\nconcavity (mean):                     0.0    0.427\nconcave points (mean):                0.0    0.201\nsymmetry (mean):                      0.106  0.304\nfractal dimension (mean):             0.05   0.097\nradius (standard error):              0.112  2.873\ntexture (standard error):             0.36   4.885\nperimeter (standard error):           0.757  21.98\narea (standard error):                6.802  542.2\nsmoothness (standard error):          0.002  0.031\ncompactness (standard error):         0.002  0.135\nconcavity (standard error):           0.0    0.396\nconcave points (standard error):      0.0    0.053\nsymmetry (standard error):            0.008  0.079\nfractal dimension (standard error):   0.001  0.03\nradius (worst):                       7.93   36.04\ntexture (worst):                      12.02  49.54\nperimeter (worst):                    50.41  251.2\narea (worst):                         185.2  4254.0\nsmoothness (worst):                   0.071  0.223\ncompactness (worst):                  0.027  1.058\nconcavity (worst):                    0.0    1.252\nconcave points (worst):               0.0    0.291\nsymmetry (worst):                     0.156  0.664\nfractal dimension (worst):            0.055  0.208\n===================================== ====== ======\n\n:Missing Attribute Values: None\n\n:Class Distribution: 212 - Malignant, 357 - Benign\n\n:Creator:  Dr. William H. Wolberg, W. Nick Street, Olvi L. Mangasarian\n\n:Donor: Nick Street\n\n:Date: November, 1995\n\nThis is a copy of UCI ML Breast Cancer Wisconsin (Diagnostic) datasets.\nhttps://goo.gl/U2Uwz2\n\nFeatures are computed from a digitized image of a fine needle\naspirate (FNA) of a breast mass.  They describe\ncharacteristics of the cell nuclei present in the image.\n\nSeparating plane described above was obtained using\nMultisurface Method-Tree (MSM-T) [K. P. Bennett, "Decision Tree\nConstruction Via Linear Programming." Proceedings of the 4th\nMidwest Artificial Intelligence and Cognitive Science Society,\npp. 97-101, 1992], a classification method which uses linear\nprogramming to construct a decision tree.  Relevant features\nwere selected using an exhaustive search in the space of 1-4\nfeatures and 1-3 separating planes.\n\nThe actual linear program used to obtain the separating plane\nin the 3-dimensional space is that described in:\n[K. P. Bennett and O. L. Mangasarian: "Robust Linear\nProgramming Discrimination of Two Linearly Inseparable Sets",\nOptimization Methods and Software 1, 1992, 23-34].\n\nThis database is also available through the UW CS ftp server:\n\nftp ftp.cs.wisc.edu\ncd math-prog/cpo-dataset/machine-learn/WDBC/\n\n.. dropdown:: References\n\n  - W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction\n    for breast tumor diagnosis. IS&T/SPIE 1993 International Symposium on\n    Electronic Imaging: Science and Technology, volume 1905, pages 861-870,\n    San Jose, CA, 1993.\n  - O.L. Mangasarian, W.N. Street and W.H. Wolberg. Breast cancer diagnosis and\n    prognosis via linear programming. Operations Research, 43(4), pages 570-577,\n    July-August 1995.\n  - W.H. Wolberg, W.N. Street, and O.L. Mangasarian. Machine learning techniques\n    to diagnose breast cancer from fine-needle aspirates. Cancer Letters 77 (1994)\n    163-171.\n',
 'feature_names': array(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
        'mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry', 'mean fractal dimension',
        'radius error', 'texture error', 'perimeter error', 'area error',
        'smoothness error', 'compactness error', 'concavity error',
        'concave points error', 'symmetry error',
        'fractal dimension error', 'worst radius', 'worst texture',
        'worst perimeter', 'worst area', 'worst smoothness',
        'worst compactness', 'worst concavity', 'worst concave points',
        'worst symmetry', 'worst fractal dimension'], dtype='<U23'),
 'filename': 'breast_cancer.csv',
 'data_module': 'sklearn.datasets.data'}
 ```



### Split data into X and Y
if we consider:
- x = input 
- y = output

as we know in sklearn our dataset return 
- data → features (inputs)
- target → labels (outputs)

we assign:\
x -> data\
y -> target

#### Example:
```py
from sklearn.datasets import load_breast_cancer # built in dataset

data = load_breast_cancer()
x = data.data
y = data.target

print("x = ", x)
print("y = ", y)
```
Output:
```
x =  [[1.799e+01 1.038e+01 1.228e+02 ... 2.654e-01 4.601e-01 1.189e-01]
 [2.057e+01 1.777e+01 1.329e+02 ... 1.860e-01 2.750e-01 8.902e-02]
 [1.969e+01 2.125e+01 1.300e+02 ... 2.430e-01 3.613e-01 8.758e-02]
 ...
 [1.660e+01 2.808e+01 1.083e+02 ... 1.418e-01 2.218e-01 7.820e-02]
 [2.060e+01 2.933e+01 1.401e+02 ... 2.650e-01 4.087e-01 1.240e-01]
 [7.760e+00 2.454e+01 4.792e+01 ... 0.000e+00 2.871e-01 7.039e-02]]

y =  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 0 0 1 1 1 1 0 1 0 0
 1 0 1 0 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1
 1 1 1 1 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 1
 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0
 1 0 1 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1
 1 0 1 1 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1
 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1 1
 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0 0
 0 1 0 0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1
 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0 1 1
 0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 1
 1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0 1 0 0
 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 0 0 0 0 0 0 1]
```

### Use return_X_y
all the things we did in above step we can do it in single line using `return_X_y`


#### Example:
```py
from sklearn.datasets import load_breast_cancer # built in dataset

x,y = load_breast_cancer(return_X_y = True)

print("x = ", x)
print("y = ", y)
```
Output:
```
x =  [[1.799e+01 1.038e+01 1.228e+02 ... 2.654e-01 4.601e-01 1.189e-01]
 [2.057e+01 1.777e+01 1.329e+02 ... 1.860e-01 2.750e-01 8.902e-02]
 [1.969e+01 2.125e+01 1.300e+02 ... 2.430e-01 3.613e-01 8.758e-02]
 ...
 [1.660e+01 2.808e+01 1.083e+02 ... 1.418e-01 2.218e-01 7.820e-02]
 [2.060e+01 2.933e+01 1.401e+02 ... 2.650e-01 4.087e-01 1.240e-01]
 [7.760e+00 2.454e+01 4.792e+01 ... 0.000e+00 2.871e-01 7.039e-02]]

y =  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 0 0 1 1 1 1 0 1 0 0
 1 0 1 0 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1
 1 1 1 1 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 1
 1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0
 1 0 1 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1
 1 0 1 1 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1
 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1 1
 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0 0
 0 1 0 0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1
 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0 1 1
 0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 1
 1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0 1 0 0
 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 0 0 0 0 0 0 1]
```
### Import dataset as pandas frame

```py
from sklearn.datasets import load_breast_cancer

df = load_breast_cancer(as_frame=True).frame
```
Output:

| mean radius | mean texture | mean perimeter | mean area | mean smoothness | mean compactness | mean concavity | mean concave points | mean symmetry | mean fractal dimension | ... | worst texture | worst perimeter | worst area | worst smoothness | worst compactness | worst concavity | worst concave points | worst symmetry | worst fractal dimension | target |
|-------------|--------------|----------------|-----------|------------------|-------------------|----------------|----------------------|----------------|-------------------------|-----|---------------|------------------|-------------|--------------------|---------------------|------------------|------------------------|----------------|---------------------------|--------|
| 17.99 | 10.38 | 122.80 | 1001.0 | 0.11840 | 0.27760 | 0.30010 | 0.14710 | 0.2419 | 0.07871 | ... | 17.33 | 184.60 | 2019.0 | 0.16220 | 0.66560 | 0.7119 | 0.2654 | 0.4601 | 0.11890 | 0 |
| 20.57 | 17.77 | 132.90 | 1326.0 | 0.08474 | 0.07864 | 0.08690 | 0.07017 | 0.1812 | 0.05667 | ... | 23.41 | 158.80 | 1956.0 | 0.12380 | 0.18660 | 0.2416 | 0.1860 | 0.2750 | 0.08902 | 0 |
| 19.69 | 21.25 | 130.00 | 1203.0 | 0.10960 | 0.15990 | 0.19740 | 0.12790 | 0.2069 | 0.05999 | ... | 25.53 | 152.50 | 1709.0 | 0.14440 | 0.42450 | 0.4504 | 0.2430 | 0.3613 | 0.08758 | 0 |
| 11.42 | 20.38 | 77.58 | 386.1 | 0.14250 | 0.28390 | 0.24140 | 0.10520 | 0.2597 | 0.09744 | ... | 26.50 | 98.87 | 567.7 | 0.20980 | 0.86630 | 0.6869 | 0.2575 | 0.6638 | 0.17300 | 0 |
| 20.29 | 14.34 | 135.10 | 1297.0 | 0.10030 | 0.13280 | 0.19800 | 0.10430 | 0.1809 | 0.05883 | ... | 16.67 | 152.20 | 1575.0 | 0.13740 | 0.20500 | 0.4000 | 0.1625 | 0.2364 | 0.07678 | 0 |
  

Now you can use pandas method on this dataFrames
```py
df = load_breast_cancer(as_frame=True).frame
df.info()
df.isnull()
```

### Custom dataset using `make_`
In sklearn, `make_dataset` (actually functions that start with `make_`) are used to generate artificial/synthetic datasets.

It refers to a group of functions like:
- `make_classification()`
- `make_regression()`
- `make_blobs()`
- `make_circles()`
- `make_moons()`

These are used to create fake datasets for practicing machine learning algorithms.

| Function                | What kind of fake dataset it creates | Illustration                                    |
| ----------------------- | ------------------------------------ | ----------------------------------------------- |
| `make_classification()` | Classification data                  | Points divided into classes (e.g., Red vs Blue) |
| `make_regression()`     | Regression data                      | A straight-line pattern with some noise         |
| `make_blobs()`          | Clusters                             | Separate round clusters for K-Means             |
| `make_circles()`        | Circular pattern                     | Inner circle + outer circle                     |
| `make_moons()`          | Moon-shaped classes                  | Two curved moon shapes used for non-linear ML   |


#### Example
```py
from sklearn.datasets import make_blobs

# Create synthetic dataset
X, y = make_blobs(
    n_samples=10,       # total 10 data points
    centers=3,          # make 3 clusters
    random_state=42     # for reproducibility
)

print("Features (X):")
print(X)

print("\nLabels (y):")
print(y)
```
What this code does:
- Creates 10 fake data points
- Divides them into 3 clusters
- X = features (points)
- y = cluster label for each point (0, 1, or 2)

every time we execute make_ function it will create new random dataset which will be completely different from the previous datasets 

to keep dataset same every time we re-execute this function we use random_state which is used to control the randomness, It ensures that every time you run the code, you get the SAME output.

If you provide a low value in random_state, nothing special happens — you just get a different consistent random pattern.

**Example**

Imagine sklearn needs to shuffle numbers `[1,2,3,4,5]`.

random_state = 1
```
Shuffled → [3,1,5,2,4]
```
random_state = 3
```
Shuffled → [5,1,3,4,2]
```
random_state = 42
```
Shuffled → [4,2,1,3,5]
```
All values are allowed → just different patterns.

[Go To Top](#content)

---
# Data Splitting
Data splitting means dividing your dataset into separate parts so your ML model can learn properly and be tested fairly.

### Why do we split data?

To avoid a model that remembers the data instead of learning patterns.
Splitting helps check whether the model performs well on new unseen data.

it also:
- Helps check if the model generalizes to new data
- Prevents the model from memorizing (overfitting)
- Provides unseen data to evaluate performance
- Allows fair comparison between different models
- Lets you tune hyperparameters safely using a validation set
- Mimics real-world scenarios, where new data arrives after training

### Typical Splits
| Set            | Purpose                                 | Example % |
| -------------- | --------------------------------------- | --------- |
| **Training**   | Model learns patterns                   | 70–80%    |
| **Validation** | Tune hyperparameters, avoid overfitting | 10–15%    |
| **Test**       | Final evaluation                        | 10–15%    |


### Function Used
```py
train_test_split()
```
from:
```py
from sklearn.model_selection import train_test_split
```
#### `train_test_split()` gives 4 outputs (most common case)

When you pass features (X) and labels (y):
```py
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```
Here’s what each part means:
| Return Value | Meaning           | What it Contains                               |
| ------------ | ----------------- | ---------------------------------------------- |
| **X_train**  | Training features | Part of your dataset used to *train* the model |
| **X_test**   | Testing features  | Used to *test/evaluate* the trained model      |
| **y_train**  | Training labels   | Target values for X_train                      |
| **y_test**   | Testing labels    | Target values for X_test                       |

#### order matters a LOT in `train_test_split()`

| Input Order                 | Output Order                                        |
| --------------------------- | --------------------------------------------------- |
| `train_test_split(X, y)`    | `X_train, X_test, y_train, y_test`                  |
| `train_test_split(A, B, C)` | `A_train, A_test, B_train, B_test, C_train, C_test` |
| ❌ Wrong capture order       | Results in incorrect assignments                    |



### Example
```py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

x,y = load_iris(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)    # 20% data for testing

print(len(x))   # total 150 
print(len(x_train)) # 80% of 150 = 120
print(len(x_test))  # 20% of 150 = 30
```

Output:
```
150
120
30
```

### Important Parameters
| Parameter      | Meaning                                          |
| -------------- | ------------------------------------------------ |
| `test_size`    | How much data goes into testing (0.2 = 20%)      |
| `train_size`   | Optional (if you want to manually say 80%, etc.) |
| `random_state` | Ensures same split every run                     |
| `shuffle=True` | Data gets shuffled before splitting (default)    |


### unbalanced Split
A split is unbalanced when:\
The number of samples of each class in train/test does NOT match the original data’s ratio.

#### Example
Original data:
- Class 0 → 8 samples
- Class 1 → 2 samples\
(so ratio = 80% : 20%)

After splitting (unbalanced case):

Train:\
7 samples of class 0, 1 sample of class 1 (87.5% : 12.5%)

Test:\
1 sample of class 0, 1 sample of class 1 (50% : 50%)

The ratios changed → unbalanced.

#### Balanced split means
Train and test should have the same ratio as the original dataset (80% : 20%).


### StratifiedShuffleSplit

`train_test_split()` does NOT guarantee balanced splitting by default.

By default:
- It randomly splits the data
- It tries to preserve the pairing (X with y)
- But it does NOT balance the class distribution

#### How to make a balanced split?

We use stratification:
```py
train_test_split(X, y, test_size=0.2, stratify=y)
```
It ensures train and test have the same class ratio as the original dataset.

#### Another way of doing balanced split is to use `StratifiedShuffleSplit`
StratifiedShuffleSplit creates shuffled train-test splits while keeping class proportions exactly the same as the original data, and can generate many such splits.

| Feature          | train_test_split(stratify=y) | StratifiedShuffleSplit            |
| ---------------- | ---------------------------- | --------------------------------- |
| Number of splits | Only 1                       | Can make many                     |
| Shuffling        | Automatic                    | You can control it                |
| Output style     | Direct arrays                | Gives train and test **indexes**  |
| Use cases        | Simple split                 | CV, multiple splits, more control |


#### How to use it?
```py
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2) # n_splits = number of split
```
Now we can use this split object to make our balanced train test split

```py
split.split(X, y)
```
`split.split(X, y)`  does NOT return the actual data.

It returns a generator that gives you:
```
(train_index, test_index)
```
> A generator is something that gives you values one at a time, instead of giving everything at once.

Both are arrays of indexes
- train_index = positions of samples that go into training
- test_index = positions of samples that go into testing


#### Simple Illustration
Suppose:\
`X has 10 samples`

`split.split(X, y)` will give something like:
```
train_index = [0, 3, 4, 6, 8, 9]
test_index  = [1, 2, 5, 7]
```
Now you use them like:
```
X_train = X[train_index]
X_test  = X[test_index]
```

### Example:
```py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

x,y = load_iris(return_X_y=True)

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)

for train_idx, test_idx in split.split(x, y):
    x_train = x[train_idx]
    x_test = x[test_id]
    y_train = y[train_idx]
    y_test = y[test_id]
```



[Go To Top](#content)

---
# Preprocessing
Preprocessing means preparing raw data so that a machine learning model can understand it.

ML models can’t work directly on messy, text, missing-value, or uneven data —
so preprocessing makes the data clean, numeric, scaled, and model-ready.

### Why do we need preprocessing?
Because raw data usually has:
- Missing values
- Different scales
- Irrelevant columns
- Text instead of numbers
- Noise and outliers
- Categorical values (labels)

Without preprocessing, models become:
- inaccurate
- slow
- unstable
- impossible to train

### Common tool for preprocessing in sklearn
- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler):\
 Standardize features by removing the mean and scaling to unit variance.
- [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler):\
Transform features by scaling each feature to a given range.
- [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder):\
Encode categorical features as a one-hot numeric array.
- LabelEncoder
- SimpleImputer
- RobustScaler

> this are the operation that we mostly perform at the time of [feature engineering](https://github.com/Yadnesh-Ranshevare/python_notes/blob/main/EDA/readdme.md#feature-engineering)

> to learn more about how each function work visit the [official documentation of sklearn](https://scikit-learn.org/stable/api/sklearn.preprocessing.html)

### Example:
```py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x,y = load_iris(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

scalar = StandardScaler()

x_train_scale = scalar.fit_transform(x_train)
x_test_scale = scalar.transform(x_test)
```

### difference between fit_transform() and transform()

#### 1. fit_transform() → Learn + Apply
It does two things:

fit → learns the scaling values
- mean
- standard deviation
- min/max (for MinMaxScaler)

transform → applies the scaling using those learned values

#### 2. transform() → Only Apply
It does NOT learn anything.

It only uses the values learned earlier from training data.

You use this on:

- test data
- validation data
- new incoming data

Because you should never learn (fit) from test data.

[Go To Top](#content)

---