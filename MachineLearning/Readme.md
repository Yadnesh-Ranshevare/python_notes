# Content

1. [AI vs ML vs DL vs DS](#ai-vs-ml-vs-dl-vs-ds)
2. [Type of ML Algorithm](#type-of-ml-algorithm)
3. [Regression and Classification](#regression-and-classification)
4. [Clustering And Dimensionality Reduction](#clustering-and-dimensionality-reduction)
5. [Clustering vs Classification](#clustering-vs-classification)
6. [Liner Regression](#liner-regression)
7. [Cost Function](#cost-function)
8. Gradient Decent Algorithm
    - [Gradient Decent](#gradient-descent)
    - [Convergence Equation](#convergence-equation)
9. [Gradient Decent Algorithm For Liner Regression](#gradient-decent-algorithm-for-liner-regression)
10. [Performance Matrix](#performance-matrix)
    - [R² Score](#score)
11. [Underfitting & Overfitting](#underfitting--overfitting)
12. [Ridge Regression](#ridge-regression)
13. [Lasso Regression](#lasso-regression)
14. [Why Not To Use Liner Regression for classification?](#why-not-to-use-liner-regression-for-classification)
15. [Logistic Regression](#logistic-regression)
16. [Sigmoidal Function](#sigmoidal-function)
17. [Cost Function For Logistic Regression](#cost-function-for-logistic-regression)
18. [Performance Matrix](#performance-matrix)
    - [Confusion Matrix](#confusion-matrix)
    - [Accuracy](#calculate-accuracy-from-the-confusion-matrix)
    - [Precision, Recall, and F1 (F-Beta)](#precision-recall-and-f1-f-beta)
19. [Naïve Bayes Algorithm](#naïve-bayes-algorithm)
20. [KNN Algorithm](#knn-algorithm)
21. [Decision Tree](#decision-tree)
    - [Entropy](#entropy)
    - [Gini Coefficient](#gini-coefficient)
    - [Information Gain](#information-gain)
    - [Decision Tree for Classification](#decision-tree-for-classification)
    - [Decision Tree for Regression](#decision-tree-for-regression)
    - [Decision Trees Overfit](#decision-trees-overfit)
22. [Ensemble Techniques](#ensemble-techniques)
    - [Random Forest](#random-forest)
    - [AdaBoost](#adaboost)
23. [K-Means Clustering](#k-means-clustering)
24. [Hierarchal Clustering](#hierarchal-clustering)
25. [Silhouette Score](#silhouette-score)
26. [Dimensionality Reduction](#dimensionality-reduction)
    - [Curse of Dimensionality](#curse-of-dimensionality)
    - [Feature selection, Covariance & Corelation](#feature-selection)
    - [Feature Extraction](#feature-extraction)
    - [PCA (Principal Component Analysis)](#pca-principal-component-analysis)
    - [Math intuition behind the PAC Algorithm](#math-intuition-behind-the-pac-algorithm)

---

# AI vs ML vs DL vs DS

### 1. Artificial Intelligence (AI)

**Definition:**\
AI is the broad field that focuses on making machines think and act like humans — reasoning, learning, and decision-making.

**Goal**: Create systems that can perform tasks requiring human intelligence (e.g., speech, vision, planning).

**Example:**

-   Siri or Alexa understanding your voice and responding.
-   Self-driving cars making driving decisions.

### 2. Machine Learning (ML)

**Definition:**\
ML is a subset of AI that teaches computers to learn from data without being explicitly programmed.

**Goal**: Make predictions or decisions using data patterns.

**Example:**

-   Netflix recommending movies based on your watch history.
-   Spam filter learning what emails are spam.

### 3. Data Science (DS)

**Definition:**\
Data Science focuses on collecting, cleaning, analyzing, and visualizing data to extract insights and help in decision-making.

**Goal**: Turn raw data into useful information and models.

**Example:**

-   Analyzing user data to find which products sell best.
-   Visualizing COVID-19 trends using graphs.
    > Data Science often uses AI/ML techniques to draw conclusions from data.

### 4. Deep Learning (DL)

**Definition:**\
DL is a subset of Machine Learning that uses neural networks with many layers to learn complex patterns — similar to how the human brain works.

**Goal**: Handle large and complex data (like images, audio, or natural language).

**Example:**

-   Face recognition in phones.
-   ChatGPT (it uses deep learning models).

### For Visual Understanding

![Image](./images/Data-Science-VS-Machine-Learning-VS-Artificial-Intelligence-vs-Deep-Learning-Studyopedia-1024x432.png)

### Comparison Table

| Field  | Focus                         | Example                 | Type                 |
| ------ | ----------------------------- | ----------------------- | -------------------- |
| **AI** | Simulating human intelligence | Self-driving car        | Broad field          |
| **ML** | Learning from data            | Netflix recommendations | Subset of AI         |
| **DL** | Neural networks & big data    | Face recognition        | Subset of ML         |
| **DS** | Data analysis & insights      | Business data reports   | Separate but related |

[Go To Top](#content)

---

# Type Of ML Algorithm

Machine Learning algorithms are mainly divided into 4 types, based on how they learn from data.
Here’s a clear breakdown with simple explanations and examples

### 1. Supervised Learning

-   The model learns from labeled data — meaning both input and correct output are known.
-   **Goal:** Predict outcomes for new, unseen data.
-   **Example:** If you have a dataset of house prices with features like area, location, and price — the model learns the pattern and predicts price for a new house.

**Types:**
| Type | Description | Example Algorithms |
| ------------------ | -------------------------- | -------------------------------------------- |
| **Regression** | Predicts continuous values | Linear Regression, Decision Tree Regressor |
| **Classification** | Predicts discrete labels | Logistic Regression, Random Forest, SVM, KNN |

> Input and Output variable are also know as dependent and independent variables
>
> **Independent variable** -> inputs\
> **Dependent variable** -> output

### 2. Unsupervised Learning

-   The model learns from unlabeled data — only inputs, no known outputs.
-   **Goal:** Discover groups, similarities, or patterns without knowing the output.
-   **Example:** Grouping customers with similar buying behavior (Clustering).

**Types:**
| Type | Description | Example Algorithms |
| --------------- | ------------------------------------- | ---------------------------------------- |
| **Clustering** | Groups similar data points | K-Means, Hierarchical Clustering, DBSCAN |
| **Dimensionality Reduction** | Reducing dataset features while preserving key information. | PCA (Principal Component Analysis), |

### 3. Semi-Supervised Learning

-   Uses a mix of labeled and unlabeled data — labeled data helps guide learning for unlabeled data.
-   **Goal:** Improve accuracy when labeling all data is expensive or time-consuming.
-   **Example:** Email spam detection — a few emails are labeled as spam or not, rest are learned automatically.
-   Algorithms:
    -   Self-training models
    -   Graph-based models
    -   Semi-supervised SVM

### 4. Reinforcement Learning (RL)

-   The model learns by interacting with an environment and receiving rewards or penalties for actions.
-   **Goal:** Learn the best sequence of actions to maximize rewards.
-   **Example:**
    -   A robot learning to walk.
    -   A game-playing AI (like AlphaGo) improving with each match.
-   **Algorithms:**
    -   Q-Learning
    -   Deep Q-Network (DQN)
    -   SARSA
    -   Policy Gradient Methods

### Summary Table

| Type                | Data Type         | Goal                            | Example Use Case      |
| ------------------- | ----------------- | ------------------------------- | --------------------- |
| **Supervised**      | Labeled           | Predict output                  | Predict house prices  |
| **Unsupervised**    | Unlabeled         | Find patterns/groups            | Customer segmentation |
| **Semi-Supervised** | Partially labeled | Better learning with less data  | Spam filtering        |
| **Reinforcement**   | Reward-based      | Learn actions via trial & error | Game bots, robots     |

[Go To Top](#content)

---

# Regression and Classification

## Regression

Regression is a type of Supervised Learning used when you want to predict a continuous numeric value (not categories).

In short:\
Regression finds a relationship between input (X) and output (Y) and tries to draw the best-fit line through the data points.

#### Example: House Price Prediction

Let’s say you have a dataset like this
| Area (sq ft) | Price (₹ in lakhs) |
| ------------ | ------------------ |
| 1000 | 40 |
| 1200 | 50 |
| 1500 | 65 |
| 1800 | 80 |

You want to predict the price of a house that’s 1600 sq ft.

**How it works:**

1. Input (X) = Area of house
2. Output (Y) = Price of house
3. The regression algorithm tries to find a line (or curve) that best fits all data points.

This line can be represented as: `Y = mX + c`

**Where:**

-   Y → Predicted value (price)
-   X → Input feature (area)
-   m → Slope (how much price changes per sq ft)
-   c → Intercept (base price)

<img src="./images/regration_example.png" style="width:600px">

from this graph we can predict the housing price for 1600 sq ft.

-   for above graph calculated slope is `m = 0.04`
-   Therefor, `Price = 0.04 * Area + 0`
-   `Price = 0.04 * 1600` = `₹64 lakhs`

#### Common Types of Regression

| Type                           | Description                      | Example Use                          |
| ------------------------------ | -------------------------------- | ------------------------------------ |
| **Linear Regression**          | Straight line relation           | House price vs area                  |
| **Multiple Linear Regression** | Many inputs                      | Price based on area, rooms, location |
| **Polynomial Regression**      | Curved relation                  | Growth trends, population over years |
| **Ridge/Lasso Regression**     | Regularized versions             | Prevent overfitting                  |
| **Logistic Regression**        | Used for classification (yes/no) | Spam email detection                 |

## Classification

Classification is another type of Supervised Learning — but instead of predicting numbers (like regression), it predicts categories or labels.

**In short:**\
Classification answers “Which class does this data belong to?”

#### Example: Email Spam Detection

You have a dataset like:
| Email text | Label |
| ------------------------------ | -------- |
| “You won a lottery!” | Spam |
| “Meeting at 10 AM” | Not Spam |
| “Get rich fast!” | Spam |
| “Your project is due tomorrow” | Not Spam |

The algorithm learns the patterns:

-   Words like “lottery”, “win”, “offer” → Spam
-   Words like “meeting”, “project” → Not spam

Then when a new email comes in, the model predicts whether it’s spam or not.

### To visually understand how classification works

![Image](./images/classification-algorithm-in-machine-learning.png)

#### Types of Classification

| Type                           | Description                              | Example                            |
| ------------------------------ | ---------------------------------------- | ---------------------------------- |
| **Binary Classification**      | Two possible outcomes                    | Spam / Not Spam, Male / Female     |
| **Multi-Class Classification** | More than two categories                 | Cat / Dog / Rabbit                 |
| **Multi-Label Classification** | Each item can belong to multiple classes | News tagged as [Politics, Economy] |

#### Popular Classification Algorithms

| Algorithm                        | Description                                  |
| -------------------------------- | -------------------------------------------- |
| **Logistic Regression**          | Linear model for binary outcomes             |
| **Decision Tree**                | Splits data using conditions                 |
| **Random Forest**                | Multiple trees for better accuracy           |
| **KNN (K-Nearest Neighbors)**    | Classifies based on nearest data points      |
| **SVM (Support Vector Machine)** | Finds the best boundary line between classes |
| **Naive Bayes**                  | Based on probability and Bayes’ theorem      |

[Go To Top](#content)

---

# Clustering And Dimensionality Reduction

## Clustering

Clustering is a type of Unsupervised Learning, where the algorithm groups similar data points together — without knowing any labels in advance.

**It answers:**\
“Which data points are similar to each other?”

#### Example: Customer Segmentation

Imagine you have shopping data from customers:
| Customer | Age | Spending Score |
| -------- | --- | -------------- |
| A | 18 | 80 |
| B | 22 | 75 |
| C | 45 | 30 |
| D | 48 | 25 |
| E | 28 | 85 |
| F | 50 | 20 |

You don’t know who’s which type of customer,

but clustering algorithms can group them like:

-   **Cluster 1**: Young customers who spend more (A, B, E)
-   **Cluster 2**: Older customers who spend less (C, D, F)

So now, a marketing team can create different strategies for each cluster!

#### How it works

1. The algorithm calculates similarity between data points
2. Then it groups the closest points together.
3. Each group = one cluster.

#### Understand Visually

<img src="./images/Clustering.png" style="width:600px">

### Common Clustering Algorithms

| Algorithm                   | Description                                      | Example Use           |
| --------------------------- | ------------------------------------------------ | --------------------- |
| **K-Means**                 | Divides data into K clusters based on similarity | Customer segmentation |
| **Hierarchical Clustering** | Builds tree-like clusters (dendrogram)           | Gene classification   |
| **DBSCAN**                  | Groups dense regions and ignores noise           | Detecting outliers    |
| **Mean Shift**              | Moves points toward cluster centers dynamically  | Image segmentation    |

## Dimensionality Reduction

Dimensionality Reduction means reducing the number of input features (columns) in your dataset while keeping the important information.

The algorithm only looks at the input features to find patterns, correlations, or redundancies.

The goal is to simplify the data structure, not predict an output.

**In simple words:**\
It’s about simplifying the data — keeping what matters, removing what doesn’t.

#### Example: Student Data

Suppose your dataset has:
| Features | Description |
| ----------- | ----------------- |
| Marks | Exam score |
| Attendance | Percentage |
| Sleep Hours | Daily sleep |
| Study Hours | Daily study |
| Social Time | Time with friends |

Maybe these 5 features overlap —\
for example, “Study Hours” and “Marks” are strongly related.

Dimensionality reduction can merge such correlated features into 2–3 “principal components” that still represent the pattern of the data.

So, instead of working with 5 features, you work with 2 — easier, faster, and cleaner!

#### How it works

The algorithm finds new axes (directions) that capture most of the variation in the data and ignores the rest (less important info).

#### Common Techniques

| Technique                                               | Description                                                              | Use                                                  |
| ------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------- |
| **PCA (Principal Component Analysis)**                  | Projects data onto fewer dimensions while keeping variance high          | Most common, used for visualization or preprocessing |
| **t-SNE (t-Distributed Stochastic Neighbor Embedding)** | Reduces data to 2D/3D for visualization while preserving local structure | Useful in clustering or image data                   |
| **LDA (Linear Discriminant Analysis)**                  | Reduces dimensions while keeping class separation                        | Used in classification problems                      |
| **Autoencoders**                                        | Deep learning models that compress and reconstruct data                  | Used in image or noise reduction                     |

[Go To Top](#content)

---

# Clustering vs Classification

### Classification = You already know the groups

You teach the model what each group means.
Then it learns to recognize which one new data belongs to.

**Example:**\
You show pictures of:

-   🐱 Cats
-   🐶 Dogs

You tell the model:
`“These are cats, these are dogs.”`

Now, when you show a new photo,
it says — “This is a dog!”

So, you already know the categories before training.

### Clustering = You don’t know the groups

You don’t give any labels — the model finds patterns on its own.

**Example:**\
You give the model 100 animal pictures — no names.

It looks and groups them like:

-   Group 1 → furry, small = 🐱 cats
-   Group 2 → long ears = 🐶 dogs
-   Group 3 → feathers = 🐦 birds

The model discovers the groups itself — you didn’t tell it what’s what.

### Think like this:

| Question                               | Classification               | Clustering                           |
| -------------------------------------- | ---------------------------- | ------------------------------------ |
| Do we know the answer before training? | ✅ Yes                       | ❌ No                                |
| What does the model do?                | Learns to label data         | Finds hidden groups                  |
| Example                                | “Is this email spam or not?” | “Group similar emails automatically” |

### Final comparison

| Feature                   | **Clustering**                                    | **Classification**                                             |
| ------------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| **Type**                  | **Unsupervised Learning**                         | **Supervised Learning**                                        |
| **Labeled Data?**         | ❌ No labels — the algorithm finds its own groups | ✅ Has labels — the model learns from them                     |
| **Goal**                  | Find hidden **groups or patterns**                | Predict **predefined categories**                              |
| **Output**                | Unknown clusters (e.g., Group 1, Group 2...)      | Known labels (e.g., Cat, Dog, Human)                           |
| **Training Data Example** | Just features like Age, Income                    | Features + Labels (e.g., Age, Income → “Buyer” or “Non-Buyer”) |
| **Evaluation**            | Harder — no true answers                          | Easier — compare predicted vs actual labels                    |
| **Example Algorithms**    | K-Means, DBSCAN, Hierarchical                     | Decision Tree, Random Forest, SVM, Logistic Regression         |
| **Common Use Cases**      | Customer segmentation, pattern discovery          | Spam detection, disease prediction                             |

[Go To Top](#content)

---

# Liner Regression

Linear Regression is a Supervised Learning algorithm used to predict a continuous value
by finding the best straight line that fits the data.

**In short:**\
It tries to find a relationship between input (X) and output (Y) using a straight line.

The main goal of liner regression is to find the best straight line that shows the relationship between input (X) and output (Y) —
so we can predict Y for new values of X.

### Think of it like this:

-   You have a bunch of points (data).
-   Linear regression tries to draw one line that’s as close as possible to all those points.
-   That line helps you:
    -   Understand the trend → e.g., as area increases, price increases.
    -   Predict new values → if I know area = 1600, what will be the price?

### Example

![image](./images/liner_regression.png)

### General Hypothesis Equation

There are multiple string line equation that you can use for liner regression like
:

1. **Slope–Intercept Form:** $y = mx + c$
2. **Point–Slope Form:** $y-y_1 = m(x-x_1)$
3. **Two–Point Form:** $y-y_1 = \frac{y_2 - y_1}{x_2-x_!}(x-x_1)$

4. **Intercept Form:** $\frac{x}{a}+\frac{y}{b} = 1$
5. **General Form:** $Ax + By + C = 0$

but in most our case will be using `General Hypothesis Equation`

In linear regression, we assume the relationship between input x and output y is linear:

$$h_\Theta (x) = \Theta_0 + \Theta_1 (x)$$

Where:

-   $h_\Theta (x)$ → predicted value (hypothesis function)
-   $\Theta_0$ → intercept (bias term)
-   $\Theta_1$ → weight/slope parameter
-   $x$ → input feature (independent variable)

### Linear Regression assumption

#### 1. Linearity

The relationship between independent variables (X) and dependent variable (Y) should be linear.
That is,

**Example**
| Hours Studied (X) | Marks Scored (Y) |
| ----------------- | ---------------- |
| 1 | 20 |
| 2 | 40 |
| 3 | 60 |
| 4 | 80 |

This forms a straight-line pattern → as hours increase, marks increase proportionally. The model can easily fit a straight line through the points.

#### 2. No Multicollinearity

Independent variables should not be highly correlated with each other.

**Example:**

Predicting salary based on:

-   Years of experience
-   Education level

These are independent enough.

Predicting salary based on:

-   Years of experience
-   Number of projects handled

If more experience almost always means more projects, both variables say the same thing → high multicollinearity.

This makes the model unstable — coefficients (weights) fluctuate unpredictably.

[Go To Top](#content)

---

# Cost Function

The Cost Function (also called Loss Function) tells the model how wrong its predictions are.
It’s like a scorecard — the lower the cost, the better your model is doing.

**In short:**\
The cost function measures the error between the model’s predicted values and the actual values.

### Example

Let’s say your model predicts house prices:
| Actual Price (Y) | Predicted Price (Ŷ) | Error (Y - Ŷ) |
| ---------------- | ------------------- | ------------- |
| 50 | 48 | 2 |
| 60 | 65 | -5 |
| 70 | 68 | 2 |

Here, the errors are small, but we want to measure the total error to see how far off we are.

### Mean Squared Error (MSE)

In [Linear Regression](#liner-regression), the most common cost function is Mean Squared Error:

$$J(m,c) = \frac{1}{n}\sum(Y_i - \bar{Y_i})^2$$

Where:

-   $Y_i$ → Actual value
-   $\bar{Y_i}$ → Predicted value
-   $n$ → Number of data points
-   $J(m,c)$ → Cost (depends on slope m and intercept c)

The model tries to find values of m and c that make J(m, c) as small as possible.

This is done using an optimization method like Gradient Descent, which gradually adjusts m and c to reduce cost.

### Example

let say you have dataset like
| input | output|
|--- | ---|
|1|1|
|2|2
3|3

Using general hypothesis equation

$$h_\Theta (x) = \Theta_0 + \Theta_1 (x)$$

lets assume $\Theta_0 = 0$

Therefor our equation becomes:

$$h_\Theta (x) =  \Theta_1 (x)$$

#### For $\Theta_1 = 1$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$ | Actual Output $(y_i)$ |
| ------------- | -------------------------------- | --------------------- |
| 1             | 1                                | 1                     |
| 2             | 2                                | 2                     |
| 3             | 3                                | 3                     |

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-1)^2 + (2-2)^2 + (3-3)^2] = 0$

<img src="./images/cost_1.png" style="width:600px">

#### For $\Theta_1 = 0.5$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$ | Actual Output $(y_i)$ |
| ------------- | -------------------------------- | --------------------- |
| 1             | 0.5                              | 1                     |
| 2             | 1                                | 2                     |
| 3             | 1.5                              | 3                     |

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0.5)^2 + (2-1)^2 + (3-1.5)^2] ≈ 0.58$

<img src="./images/cost_2.png" style="width:600px">

#### For $\Theta_1 = 0$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$ | Actual Output $(y_i)$ |
| ------------- | -------------------------------- | --------------------- |
| 1             | 0                                | 1                     |
| 2             | 0                                | 2                     |
| 3             | 0                                | 3                     |

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0)^2 + (2-0)^2 + (3-0)^2] ≈ 2.3$

<img src="./images/cost_3.png" style="width:600px">

#### From those three cases, here’s what we can conclude about the relationship between $\Theta_1$ and the cost function $J(\Theta_1)$

| Θ₁ value | Cost Function (J(Θ₁)) | Interpretation                                                   |
| -------- | --------------------- | ---------------------------------------------------------------- |
| 1        | 0                     | Perfect fit — predictions exactly match the actual values.       |
| 0.5      | 0.58                  | Predictions are somewhat close but not perfect — moderate error. |
| 0        | 2.3                   | Predictions are completely off — large error.                    |

[Go To Top](#content)

---

# Gradient Descent

Gradient Descent is an optimization algorithm that helps a model learn the best parameters (like slope `m` and intercept `c` in linear regression) by minimizing the cost function.

### Example

let say you have dataset like
| input | output|
|--- | ---|
|1|1|
|2|2
3|3

Using general hypothesis equation

$$h_\Theta (x) = \Theta_0 + \Theta_1 (x)$$

Where:

-   $h_\Theta (x)$ → predicted value (hypothesis function)
-   $\Theta_0$ → intercept (bias term)
-   $\Theta_1$ → weight/slope parameter
-   $x$ → input feature (independent variable)

lets assume $\Theta_0 = 0$

Therefor our equation becomes:

$$h_\Theta (x) =  \Theta_1 (x)$$

#### For $\Theta_1 = 1$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$ | Actual Output $(y_i)$ |
| ------------- | -------------------------------- | --------------------- |
| 1             | 1                                | 1                     |
| 2             | 2                                | 2                     |
| 3             | 3                                | 3                     |

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-1)^2 + (2-2)^2 + (3-3)^2] = 0$

#### For $\Theta_1 = 0.5$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$ | Actual Output $(y_i)$ |
| ------------- | -------------------------------- | --------------------- |
| 1             | 0.5                              | 1                     |
| 2             | 1                                | 2                     |
| 3             | 1.5                              | 3                     |

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0.5)^2 + (2-1)^2 + (3-1.5)^2] ≈ 1.17$

#### For $\Theta_1 = 0$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$ | Actual Output $(y_i)$ |
| ------------- | -------------------------------- | --------------------- |
| 1             | 0                                | 1                     |
| 2             | 0                                | 2                     |
| 3             | 0                                | 3                     |

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0)^2 + (2-0)^2 + (3-0)^2] ≈ 4.67$

#### Similarly when you calculated $J(\Theta_1)$ other values of $\Theta_1$ you'll get following data

|  Θ₁  | Predictions (hΘ(x)) | Errors (y - hΘ(x)) | Sum of squared errors   | J(Θ₁) = 1/3 \* SSE |
| :--: | :------------------ | :----------------- | :---------------------- | :----------------: |
|  0   | [0, 0, 0]           | [1, 2, 3]          | 1² + 2² + 3² = 14       |      **4.67**      |
| 0.5  | [0.5, 1, 1.5]       | [0.5, 1, 1.5]      | 0.25 + 1 + 2.25 = 3.5   |      **1.17**      |
|  1   | [1, 2, 3]           | [0, 0, 0]          | 0                       |       **0**        |
| 1.5  | [1.5, 3, 4.5]       | [-0.5, -1, -1.5]   | 0.25 + 1 + 2.25 = 3.5   |      **1.17**      |
|  2   | [2, 4, 6]           | [-1, -2, -3]       | 1 + 4 + 9 = 14          |      **4.67**      |
| -0.5 | [-0.5, -1, -1.5]    | [1.5, 3, 4.5]      | 2.25 + 9 + 20.25 = 31.5 |      **10.5**      |

Now if you plot the graph using this data then you get:

<img src="./images/cost_fun_grapn.png" style="width:600px">

-   When we draw the cost function (J) against the model parameter (like θ₁), we get a U-shaped curve.
-   The lowest point on this curve (for example, at θ₁ = 1) shows where the error is smallest.
-   Since the error is smallest there, that θ₁ value gives the best possible line that fits our data.

> The bottom of the curve = minimum error = best fit line.

### Minima

-   The lowest point in gradient decent is called minima
-   When we talk about minima in Gradient Descent (i.e., the points where cost function is low), there are a few types

| Feature                            | 🟢 **Global Minimum**                                  | 🟡 **Local Minimum**                                              |
| ---------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| **Definition**                     | The **lowest point** on the entire cost function curve | A **low point** in a small region, but **not the lowest overall** |
| **Error value**                    | **Smallest possible error** (best result)              | Error is **low**, but not the smallest                            |
| **Gradient value (slope)**         | Zero (no lower point exists)                           | Zero (but there are lower points elsewhere)                       |
| **Outcome**                        | Gives the **best model parameters**                    | Gives **sub-optimal parameters**                                  |
| **Linear Regression**              | Always reaches global minimum                          | — (no local minima exist here)                                    |
| **Deep Learning / Complex Models** | Hard to find (many local minima exist)                 | Very common in complex models                                     |
| **Example**                        | The **bottom of the deepest valley**                   | A **smaller dip** before the deepest valley                       |

<img src="./images/local_vs_global_minima.png" style="width:600px">

### Maxima

-   When we maximize something (like accuracy or profit), we look for the highest point on a curve instead of the lowest.
-   It’s the opposite of minima.

| Feature              | 🔵 **Global Maximum**                         | 🟣 **Local Maximum**                                            |
| -------------------- | --------------------------------------------- | --------------------------------------------------------------- |
| **Definition**       | The **highest point** on the entire curve     | A **high point** in a small region, but not the highest overall |
| **Value**            | **Largest possible value** (best performance) | **High**, but not the highest                                   |
| **Gradient (slope)** | Zero (no higher point exists)                 | Zero (but higher points exist elsewhere)                        |
| **Outcome**          | Gives **best possible performance**           | Gives **good but not best** performance                         |
| **Example**          | **Top of the tallest mountain**               | **Top of a smaller hill** nearby                                |

<img src="./images/local_vs_global_maxima.png" style="width:600px">

[Go To Top](#content)

---

# Convergence Equation

-   When we train a model (like using Gradient Descent), we keep updating parameters (θ) step by step to reduce error (Cost Function J).
-   The process keeps going until the error stops changing much — that point is called Convergence.

### Equation

$$
\Theta_j = \Theta_j - \alpha \frac{\partial J(\Theta)}{\partial \Theta_j}
$$

-   this equation is the heart of gradient descent, and it’s used for one simple reason: \
    to reduce the error (cost function) step by step until it reaches the minimum.

-   we use this equation because it tells how to update our parameters (θ values) so that our model learns and the error decreases.

| Part                                           | Meaning                                              | Purpose                                                              |
| ---------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------- |
| $\frac{\partial J(\Theta)}{\partial \Theta_j}$ | The **slope** of cost function (direction of change) | Tells whether we need to go **left or right** to reduce error        |
| $\alpha$                                       | Learning rate                                        | Controls **how big the step** should be                              |
| ( - ) (minus sign)                             | Move in **opposite direction** of slope              | Because slope shows **increasing error**, we want to **decrease it** |
| $\Theta_j$                                     | Model parameter                                      | Gets updated each iteration to get closer to best value              |

### Why we need 𝛼 (learning rate)

Think of gradient descent like walking downhill to reach the lowest point (global minima).

-   The gradient (slope) tells you which direction to move.
-   But it doesn’t tell you how far to move in that direction. That’s where α comes in — it controls the step size.

| α (learning rate) | What happens                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| **Too large**     | You take huge steps — might **jump over** the minimum or even **oscillate** forever.     |
| **Too small**     | You take tiny steps — you **move very slowly**, might take forever to reach the minimum. |
| **Just right**    | You smoothly go downhill and reach the **global minimum** quickly.                       |

![Image](./images/leaarning_rate.png)

### Type of slope

The slope tells us how steep a line or curve is and which direction it’s going.

#### Positive Slope

-   The line or curve is going upward as you move right.
-   It means the value of $J(\Theta)$ (cost) increases when you increase $\Theta$
-   So, to reduce cost, you should go left (decrease $\Theta$)

#### Negative Slope

-   The line or curve is going downward as you move right.
-   It means $J(\Theta)$ decreases when $\Theta$ increases.
-   So, to reduce cost even more, you should go right (increase $\Theta$)

#### Example

<img src="./images/slope_positive_negative.svg" style="width:600px">

#### In short

| Slope Type         | Curve Direction          | What It Means                           | Move Which Way To Reduce Cost? |
| ------------------ | ------------------------ | --------------------------------------- | ------------------------------ |
| **Positive (+ve)** | Goes up as θ increases   | You’re on the left side of the minimum  | Move **left**                  |
| **Negative (−ve)** | Goes down as θ increases | You’re on the right side of the minimum | Move **right**                 |

### How it helps find the minima

1. **Find the slope (gradient)**
    - The slope tells you which way the hill is tilted.
    - If the slope is positive → the hill goes up to the right.
    - If the slope is negative → the hill goes up to the left.
2. **Move in the opposite direction**
    - Because we want to go downhill, not uphill.
    - That’s why we use the minus (−) in the equation.
    - So if slope is positive → go left (decrease $\Theta$)
    - If slope is negative → go right (increase $\Theta$)
3. **Control how big each step is → that’s what α (alpha) does.**
    - Big α → big steps (you might jump over the bottom).
    - Small α → small steps (you’ll reach slowly but safely).
4. **Keep repeating**
    - After each step, check the slope again.
    - As you get closer to the bottom, the slope becomes smaller.
    - When slope ≈ 0 → you’re at the lowest point (minima).

### Example

Suppose our cost function is:

$$J(\Theta) = \Theta^2$$

That’s a simple U-shaped curve — its minimum is at $\Theta = 0$

#### Step 1: Compute derivative

$$\frac{dJ}{d\Theta} = 2\Theta$$

This tells us the slope at any point.

#### Step 2: Use gradient descent update rule

$$\Theta = \Theta - \alpha(2\Theta)$$

or

$$\Theta = \Theta(1 - 2\alpha)$$

#### Step 3: Start with some initial value

Let’s take:

-   Initial $\Theta = 4$
-   Learning rate $\alpha = 0.1$

Now, update step by step
| Step | Old $\Theta $ | Derivative (2Θ) | New $ \Theta = \Theta - \alpha(2Θ) $ |
| ---- | -------------- | --------------- | ------------------------------------ |
| 1 | 4.0 | 8 | 4 - 0.1×8 = **3.2** |
| 2 | 3.2 | 6.4 | 3.2 - 0.1×6.4 = **2.56** |
| 3 | 2.56 | 5.12 | 2.56 - 0.1×5.12 = **2.048** |
| 4 | 2.048 | 4.096 | 2.048 - 0.1×4.096 = **1.638** |

After each step, θ keeps getting smaller → we’re moving toward 0, the minimum of the curve.

[Go To Top](#content)

---

# Gradient Decent Algorithm For Liner Regression

from convergence equation

$$
\Theta_j = \Theta_j - \alpha \frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_j}
$$

We know that

$$J(\Theta_0, \Theta_1) = \frac{1}{2n}\sum(h_0(x^i) - y^i)^2$$

is a cost function where:

-   $h_0(x^i)$ -> predicted value
-   $y^i$ -> actual value
-   $n$ → Number of data points

### Compute derivative

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_j} = \frac{\partial }{\partial \Theta_j}[\frac{1}{n} \sum(h_0(x^i) - y^i)^2]$$

> $\frac{\partial x^2}{\partial x} = 2x$
>
> similaly
>
> $\frac{\partial \sum (x^2)}{\partial x} = 2\sum(x)$

For j = 1

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_1} = \frac{\partial }{\partial \Theta_1}\left[\frac{1}{n} \sum(h_0(x^i) - y^i)^2\right]$$

from general hypothesis equation we know that

$$h_\Theta (x^i) = \Theta_0 + \Theta_1 (x^i)$$

$$\frac{\partial h_\theta(x^i)}{\partial \Theta_1} = x^i$$

Therefor, we multiply this $x^i$ in our final equation

$$\boxed{\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_1} = \frac{2}{n} \sum(h_0(x^i) - y^i)(x^i)}$$

For j = 0

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_0} = \frac{\partial }{\partial \Theta_0}\left[\frac{1}{n} \sum(h_0(x^i) - y^i)^2\right]$$

from general hypothesis equation we know that

$$h_\Theta (x^i) = \Theta_0 + \Theta_1 (x^i)$$

$$\frac{\partial h_\theta(x^i)}{\partial \Theta_1} = \Theta_0$$

Therefor, we doesn't multiply anything in our final equation

$$\boxed{\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_0} = \frac{2}{n} \sum(h_0(x^i) - y^i)}$$

### Put this values in convergence equation

original equation

$$
\Theta_j = \Theta_j - \alpha \frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_j}
$$

for $\Theta_0$

$$\Theta_0 = \Theta_0 - \alpha\left[\frac{2}{n} \sum(h_0(x^i) - y^i)\right]$$

for $\Theta_1$

$$\Theta_1 = \Theta_1 - \alpha\left[\frac{2}{n} \sum(h_0(x^i) - y^i)(x^i)\right]$$

### These equations tell us:

-   How to update both parameters (θ₀ and θ₁) step by step so that the prediction error (cost) keeps decreasing
-   These two equations work together to slowly adjust the line so that it fits the data points perfectly — i.e., they find the minimum cost through gradient descent.

#### for $\Theta_0$

$$\Theta_0 = \Theta_0 - \alpha[\frac{2}{n} \sum(h_0(x^i) - y^i)]$$

-   It updates the intercept of the line.
-   It shifts the line up or down to reduce overall error.
-   The term $(h_0(x^i) - y^i)$ shows how far predictions are from real values.

So:\
If predictions are too high → θ₀ decreases (moves line down)\
If predictions are too low → θ₀ increases (moves line up)

#### for $\Theta_1$

$$\Theta_1 = \Theta_1 - \alpha[\frac{2}{n} \sum(h_0(x^i) - y^i)(x^i)]$$

-   It updates the slope of the line.
-   It controls how tilted the line is.
-   The extra $(x^i)$ term helps the model learn how much each feature (x) affects the output.

So:\
If the line is too flat → θ₁ increases (line tilts upward)\
If the line is too steep → θ₁ decreases (line tilts downward)

#### In short

| Parameter | Controls                  | What the equation does        |
| --------- | ------------------------- | ----------------------------- |
| **θ₀**    | Line’s height (intercept) | Moves line up or down         |
| **θ₁**    | Line’s tilt (slope)       | Changes how steep the line is |

[Go To Top](#content)

---

# Performance Matrix

A performance metric is a numerical measure used to evaluate how good (or bad) your model’s predictions are compared to actual results.

It tells:

-   How accurate is it?
-   How much error is it making?
-   Is it predicting too high or too low?

### Common Performance Metrics

1. For Regression Problems

| Metric                                         | Formula                              | Meaning                                                    |
| ---------------------------------------------- | ------------------------------------ | ---------------------------------------------------------- |
| [**MSE** (Mean Squared Error)](#cost-function) | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | Average of squared errors. Penalizes big errors.           |
| **RMSE** (Root MSE)                            | $\sqrt{MSE}$                         | Easier to interpret (same units as output).                |
| **MAE** (Mean Absolute Error)                  | $\frac{1}{n}\sum y_i - \hat{y}_i$    | Average of absolute differences. Less harsh on outliers.   |
| [**R² Score**](#score)                         | $1 - \frac{SS_{res}}{SS_{tot}}$      | How much of data variance is explained by the model (0–1). |

2. For Classification Problems

| Metric                                                        | Meaning                                              |
| ------------------------------------------------------------- | ---------------------------------------------------- |
| [**Confusion Matrix**](#confusion-matrix)                     | Table showing True/False Positive/Negative counts.   |
| [**Accuracy**](#calculate-accuracy-from-the-confusion-matrix) | How many predictions are correct overall.            |
| [**Precision**](#precision-recall-and-f1-f-beta)              | Of all predicted “positives”, how many were correct. |
| [**Recall**](#precision-recall-and-f1-f-beta)                 | Of all actual “positives”, how many did we find.     |
| [**F1 Score**](#precision-recall-and-f1-f-beta)               | Balance between Precision and Recall.                |

[Go To Top](#content)

---

# $R^2$ Score

It tells how well your regression line fits the data

### Formula

$$R^2 = 1-\frac{SS_{res}}{SS_{tot}}$$

Where:

-   $SS_{res} = \sum(y_i - \hat y_i)^2$
-   $SS_{tot} = \sum(y_i - \bar y)^2$

Here also:

-   $\hat y_i$ → value predicted by your model for input $x_i$ (represent best fit line)
-   $\bar y$ → average of all actual outputs in your dataset (represent average fit line)
-   $y_i$ → actual datapoint

![Img](./images/avg_line.png)

> Average fit line will always be a flat line, and in $SS_{tot}$ we try to find the error with respect to this average fit line (thats way in $SS_{tot}$ $\bar y$ is constant)

### Example

Let’s say we want to predict marks based on study hours.

| Hours (x) | Actual Marks (y) | Predicted Marks (ŷ) |
| --------- | ---------------- | ------------------- |
| 1         | 20               | 22                  |
| 2         | 40               | 38                  |
| 3         | 60               | 58                  |
| 4         | 80               | 78                  |

Now:

$$SS_{res} = (20 - 22)^2 + (40 - 38)^2 + (60 - 58)^2 + (80 - 78)^2 = 16$$

<br>

$$\bar y = \frac{20 + 40 + 60 + 80}{4} = 50$$

<br>

$$SS_{tot} = (20 - 50)^2 + (40 - 20)^2 + (60 - 20)^2 + (80 - 20)^2 = 2000$$

<br>

$$R^2 = 1 - \frac{16}{2000} = 0.992$$

So, R² = 0.992, meaning our model explains 99.2% of the variation — an excellent fit!

### Problem with $R^2$

-   When You Add a Useful (Relevant) Feature:

    -   That feature actually helps your model predict better.
    -   So:
        -   Prediction error decreases
        -   Cost function J(Θ) decreases
        -   R² increases

-   When You Add an Unnecessary (Irrelevant) Feature:
    -   That feature doesn’t help prediction (maybe just random noise).
    -   Then:
        -   R² still increases slightly (mathematically, it never decreases)
            > Because R² measures how much variation your model explains compared to a flat mean line. Even if you add noise, the model can “fit” that noise a little, making the R² look better — but not actually better.
-   Conclusion:\
    Adding Irrelevant new feature increases the $R^2$ value for no reason, deceiving the computer to think model with irrelevant feature is the better model cause it has high $R^2$ value

### Why R² increases when we add more input variables

R² tells us how well our model fits the data.

When you add more inputs (even random ones), the model gets more flexibility to “bend” and fit the data a bit better — so the total error slightly decreases,

So:

-   “More flexibility to bend” → model adjusts more to match the data
-   “Total error decreases” → predictions become slightly closer to the real values
-   But sometimes, it starts matching noise (random variations), not real patterns

That’s why R² goes up — because it only checks if prediction error got smaller,
not if it’s meaningful.

<img src="./images/R_squre_adding_input.png" style="width:800px">

## Adjusted R²

-   Adjusted R² is an improved version of R² that checks if the new features you add really help your model or not.
-   If a new feature doesn’t make predictions better, it reduces the score instead of increasing it.

#### Why do we need it?

Problem with normal R²:\
R² always increases when you add more features —
even if those features are useless!

That can make you think your model got better, but it actually just got more complex, not more accurate.

#### Adjusted R² fixes this

-   It adjusts R² based on how many predictors (features) you have.
-   If you add a new feature that doesn’t improve the model,
-   Adjusted R² will decrease — telling you it was unnecessary.

#### Formula

$$\text{Adjusted $R^2$} = 1 - [\frac{(1-R^2)(n-1)}{n-p-1}]$$

Where:

-   $n$ = number of data points
-   $p$ = number of features (independent variables) also called predictor
-   $R^2$ = normal R² score

> The more features (p) you add, the denominator grows, which reduces the Adjusted R²

[Go To Top](#content)

---

# Underfitting & Overfitting

When you build an ML model, you want it to learn patterns from known data and then make predictions on new, unseen data.

To do that, we split our dataset into two (sometimes three) parts:

1. Training Data
2. Testing Data

> training & test data help you spot overfitting and underfitting.

### 1. Training Data

-   This is the data the model learns from.
-   The model adjusts its parameters (like slope and intercept in linear regression) by minimizing error on this data.
-   Think of it like studying for an exam — this is your practice material.

### 2. Testing Data

-   This data is not shown to the model during training.
-   It is used after training to check how well the model can generalize — i.e., predict unseen data.
-   Think of it like your final exam — you test how well you actually learned.

### When a model “fits” the training data…

We look at two types of errors:

1. Training error → how well the model fits the data it has seen i.e training data
2. Testing error → how well the model predicts data it hasn’t seen i.e testing data

The balance between these two tells us whether the model is:

-   good (generalizes well)
-   overfitting
-   underfitting

### Underfitting → “Didn’t learn enough”

| Data              | What Happens                                            |
| ----------------- | ------------------------------------------------------- |
| **Training Data** | Model performs poorly — can’t capture the pattern.      |
| **Testing Data**  | Also performs poorly — since it never learned properly. |

Example:
| Dataset | Error |
| -------- | ------ |
| Training | High ❌ |
| Testing | High ❌ |

Model didn’t learn the pattern → underfit.

<img src="./images/underfit.png" style="width:700px">

### Overfitting → “Learned too much (memorized)”

| Data              | What Happens                                      |
| ----------------- | ------------------------------------------------- |
| **Training Data** | Model performs _extremely well_ (memorized data). |
| **Testing Data**  | Performs _poorly_ — fails on unseen data.         |

Example:
| Dataset | Error |
| -------- | ---------- |
| Training | Very Low ✅ |
| Testing | High ❌ |

Model learned noise, not the actual pattern → overfit.

<img src="./images/overfit.png" style="width:700px">

### Good Fit (Just Right)

| Data              | What Happens                    |
| ----------------- | ------------------------------- |
| **Training Data** | Fits well (low error).          |
| **Testing Data**  | Also performs well (low error). |

Model learned the true relationship and generalizes correctly.

<img src="./images/gootFit.png" style="width:700px">

### Summary Table

| Type             | Training Error | Testing Error | Model Behavior |
| ---------------- | -------------- | ------------- | -------------- |
| **Underfitting** | High           | High          | Too simple     |
| **Overfitting**  | Low            | High          | Too complex    |
| **Good Fit**     | Low            | Low           | Just right     |

### Bias–Variance Tradeoff

1. Bias\
   Bias means how much your model’s predictions are off from the true values — it’s the error due to wrong assumptions in the model. - High bias → High Error→ Model is too simple, doesn’t learn enough patterns. - Low bias → Low Error → Model captures the trend correctly.
2. Variance\
   Variance means how much your model’s predictions change when given different data — it’s the sensitivity to training data. - High variance → Model reacts too much to small changes (memorizes data). - Low variance → Model remains stable even if data changes slightly.

You can think of it like a see-saw:

-   If you reduce bias too much, variance increases.
-   If you reduce variance too much, bias increases.

#### Why this happen?

When training a model, you have two goals:

-   Learn the real pattern (↓ bias)
-   Stay stable on new data (↓ variance)

Let’s say you make your model more complex (add more features or increase polynomial degree).

Effect:

-   It can fit the training data better → bias decreases
-   But it also starts reacting to tiny random changes or noise in the data → variance increases
-   The model starts memorizing — so it performs perfectly on training data, but poorly on unseen data.
    That’s overfitting.

Now, if you make your model simpler (fewer features or lower polynomial degree):

Effect:

-   It stops reacting to small details → variance decreases
-   But now it can’t capture the full pattern → bias increases
-   It generalizes too much — predicting roughly the same for all inputs.
    That’s underfitting.

> The trick is to find a sweet spot — not too simple, not too complex — where the model captures the true pattern and still generalizes well.

| Type             | Bias    | Variance | Model Behavior                    | Example                       |
| ---------------- | ------- | -------- | --------------------------------- | ----------------------------- |
| **Underfitting** | 🔺 High | 🔻 Low   | Too simple, misses patterns       | Straight line for curved data |
| **Overfitting**  | 🔻 Low  | 🔺 High  | Too complex, memorizes data       | Wiggly curve following noise  |
| **Good Fit**     | ✅ Low  | ✅ Low   | Learns pattern + generalizes well | Smooth curve matching trend   |

#### In short:

-   Underfitting = High Bias, Low Variance → model is dumb (doesn’t learn enough)
-   Overfitting = Low Bias, High Variance → model is too smart (learns even noise)
-   Good Fit = Balance → learns real pattern and generalizes well

[Go To Top](#content)

---

# Ridge Regression

Ridge Regression is a type of Linear Regression that adds a penalty to the model to prevent overfitting.

It’s also called L2 Regularization.

### Normal Linear Regression equation

The goal in normal regression is to minimize the cost function:

$$J(\Theta) = \frac{1}{n}\sum(Y_i - \bar{Y_i})^2$$

Where:

-   $Y_i$ → Actual value
-   $\bar{Y_i}$ → Predicted value
-   $n$ → Number of data points
-   $J(\Theta)$ → Cost (depends on slope m and intercept c)

This just tries to make predictions close to actual values.

let say somehow you'll get the best fit line as follow

<img src="./images/ridge_overfit.png" style="width:600px">

if you calculate the cost function for this graph then:

$$J(\Theta) = \frac{1}{2}[(2-2) + (8-8)] = 0$$

Whenever $J(\Theta)$ becomes 0 its the condition of overfitting

in such cases use Ridge equation

### Ridge Regression equation

$$J(\Theta) = \frac{1}{n}\sum(Y_i - \bar{Y_i})^2 + \lambda(slope)^2$$

Here,

-   $\lambda$ = regularization strength (a positive number) that tells how much slope should change during each iteration

if you calculate the slope of above graph then you'll get:

$$Slope = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2$$

now our cost function becomes:

-   take $\lambda$ = 1

$$J(\Theta_1) = \frac{1}{2}[(2-2)^2 + (8-8)^2] + (1 \times 2^2) = 0 + 4 = 4$$

now as $J(\Theta_1) = 4$ is high our machine will try to reduce it and change the value of $\Theta_1$

Now let say we get our next befit line as follow:

<img src="./images/ridge_overfit_improved.png" style="width:600px">

Now our new cost function (Ridge Regression equation) becomes

$$Slope = \frac{7.3 - 2.8}{4-1} = \frac{4.5}{3} = 1.5$$

$$J(\Theta_2) = \frac{1}{2}[(2-2.8)^2 + (8-7.3)^2] + (1 \times 1.5^2)$$

$$J(\Theta_2) = \frac{1}{2}[0.64 + 0.49] + 2.25 = 0.565 + 2.25 = 2.81$$

As you can see 2.81 < 4 we can say that the value of cost function is less for $\Theta_2$ than that of $\Theta_1$

That means:

-   $\Theta_1$ = high cost → because of overfitting issue
-   $\Theta_2$ = low cost → less overfitting
-   Therefor $\Theta_2$ will be preferred over $\Theta_1$

[Go To Top](#content)

---

# Lasso Regression

Lasso Regression is another type of Regularized Linear Regression, just like Ridge.

It’s also called L1 Regularization.

### The Lasso Cost Function:

$$J(\Theta) = \frac{1}{n}\sum(Y_i - \bar{Y_i})^2 + \lambda|slope|$$

Because of the absolute value penalty (`|slope|`), Lasso can remove unimportant features by setting their weights to zero.

So, Lasso not only reduces overfitting, but also performs feature selection!

Example:

-   Imagine you have 10 input features (x₁, x₂, …, x₁₀).
-   After applying Lasso, maybe only 3 features get non-zero coefficients.
-   So the final model becomes simpler and focuses only on the important ones.

### How it works (conceptually)

When we train a model, we try to find the best $\Theta$ (coefficients) that minimize the cost function $J(\Theta)$

Now, because of the |Θⱼ| penalty:

-   If a feature (say x₃) doesn’t help in predicting y much,
-   The algorithm realizes that it can reduce the cost more by setting Θ₃ = 0 (since |Θ₃| adds unnecessary penalty).
-   So it “drops” that feature automatically.

[Go To Top](#content)

---

# Why Not To Use Liner Regression for classification?

Let’s say you want to predict whether a student will pass (1) or fail (0) based on study hours.

-   more than 3.5 hours → pass
-   less than 3.4 hours → fail

with dataset like
| Study Hours (x) | Result (y) |
| --------------- | ---------- |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1|

if we plot a graph:

<img src="./images/liner_regression_for_classification.png" style="width:600px">

from this graph we can say that:

-   Result >= 0.5 → Hours >= 3.5 → pass
-   Result < 0.5 → Hours < 3.5 → fail

But let say there is a valid outlier where is it recorded that a student is pass by studying for 9 hours, Therefor we get new entry as:

-   Study Hours(x) = 9 ; Result(y) = 1

now the graph we get:

<img src="./images/liner_regression_for_classification_with_error.png" style="width:600px">

now as you can see there is a bit disturbance at the boundary of pass and fail

This time our ML model says:

-   Result >= 0.5 → Hours >= 3.83
-   Result < 0.45 → Hours < 3.5

now let say i want to find whether the student who have study for 3.6 hours will pass or not?

-   From our graph
    -   For Hours = 3.6 → Result = 1.48
    -   Hours > 3.5 but Result < 0.5
-   for student to consider pass his result must be greater than 0.5 otherwise the respective student is fail
-   but in our case even though the student has studied more than 3.5 hours his result is less than 0.5 i.e, fail
-   This error occur because our line has tilted towards the outlier causing the disturbance in boundary

So, this example makes it clear why Linear Regression isn’t used for classification — it can’t handle class boundaries properly.

[Go To Top](#content)

---

# Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for classification problems, not regression (despite its name).

It predicts categorical outcomes, like:

-   Whether an email is spam or not spam,
-   Whether a student passes or fails,
-   Whether a customer will buy a product or not, etc.

It works like Linear Regression, but instead of predicting continuous values, it predicts the probability that a data point belongs to a certain class (usually 0 or 1).

### Example:

Suppose you want to predict if a student passes based on hours studied.
| Hours Studied | Pass (y) |
| ------------- | -------- |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1 |

A logistic regression model will learn a curve like this:

<img src="./images/logistic_regrassion_example.png" style="width:600px">

That “S-shaped” curve is the Sigmoid function, showing how probability increases with study hours.

from this curve we can find the probability of student passes on the bases of their study hours

[Go To Top](#content)

---

# Sigmoidal Function

The sigmoid function (also called the logistic function) is a mathematical function that converts any real number into a value between 0 and 1.

That’s why it’s often used in logistic regression — to express probabilities.

### Squashing

> squash means to press something so that it is damaged, changes shape or becomes flat

in logistic regression, we take the linear line (from linear regression) and then squash it using sigmoidal function so that the outputs become probabilities between 0 and 1.

<img src="./images/linear-regression-vs-logistic-regression-2.webp" style="width:800px">

### Definition

$$g(z) = \frac{1}{1 + e^{-z}}$$

where:

-   $z$ = the input (can be any number, from -∞ to +∞)
-   $e$ = Euler’s number (~2.718)

### Behavior

| z (input) | Output σ(z) | Meaning              |
| --------- | ----------- | -------------------- |
| -∞        | 0           | almost 0 probability |
| -2        | 0.12        | low probability      |
| 0         | 0.5         | 50% probability      |
| 2         | 0.88        | high probability     |
| +∞        | 1           | almost 1 probability |

So, the sigmoid turns large negative values into near 0, and large positive values into near 1.

**For more understanding:**

<img src="./images/logistic_function.png" style="width:600px">

from this graph we can say that:

-   if $z$ >= 0 then $g(z)$ >= 0.5

### How to use in Logistic Regression

we know that in logistic regression we just squash the straight line which we can construct using liner regression

Therefor, equation of straight line:

$$h(x) = \Theta_0 + \Theta_1x$$

Where:

-   $h(x)$ = predicted output for input $x$ in liner regression
-   $\Theta_0$ = intercept
-   $\Theta_1$ = slope
-   $x$ = input

this will give us the needed straight line, then we just apply the sigmoidal function to squash it down

$$g(h_0(x)) = \frac{1}{1 + e^{-h(x)}}$$

$$g(h_0(x)) = \frac{1}{1 + e^{-(\Theta_0 + \Theta_1x)}}$$

Now this will become our new equation of line for logistic regression which will give us the probability for any input value

Therefor we can say that for logistic regression:

$$h_0(x) = g(h(x))$$

$$\boxed{h_0(x) = \frac{1}{1 + e^{-(\Theta_0 + \Theta_1x)}}}$$

Here:

-   $h_0(x)$ = potability for input $x$ in logistic equation regression
-   $\Theta_0$ = intercept of liner line
-   $\Theta_1$ = slope of liner line
-   $x$ = input

[Go To Top](#content)

---

# Cost Function For Logistic Regression

> make sure you know about [Cost Function](#cost-function) before you jump onto this topic

we know thw cost function of [liner regression](#cost-function):

$$J(\Theta) = \frac{1}{n}\sum(Y_i - h_0(x_i))^2 _{---------}(i)$$

Where:

-   $Y_i$ → Actual value
-   $h_0(x_i)$ → Predicted value
-   $n$ → Number of data points
-   $J(m,c)$ → Cost (depends on slope m and intercept c)

we also know that for logistic regression:

$$h_0(x) = \frac{1}{1 + e^{-(\Theta_0 + \Theta_1x)}}_{-------}(ii)$$

now by putting the equation (ii) into equation (i) we will get the cost function for logistic regression

### Although this equation work we never use it as equation (ii) is non-convex function

<img src="./images/non-convex-vs-convex.png" style="width:600px">

-   non-convex function has multiple local minima
-   because of the presence of local minima our ML model might get stuck on those local minima resulting in poor prediction

### Another Equation

$$
Cost(h_\theta(x), y) =
\begin{cases}
  -\log(h_\theta(x)) & \text{if } y = 1, \\
  -\log(1 - h_\theta(x)) & \text{if } y = 0
\end{cases}
$$

we know that $h_0(x)$ tells probability and probability is always in between of 0 to 1, hence we can say that $h_0(x)$ will always can stat from 0 up to 1

Therefor

#### for y = 1

will get graph:

<img src="./images/cost_fun_for_logisitic_regression_y_1.png" style="width:600px">

this graph says that for:\
if y = 1 and $h(x)$ = 1 then cost = 0

#### for y = 0

will get graph:

<img src="./images/cost_fun_for_logisitic_regression_y_0.png" style="width:600px">

this graph says that for:\
if y = 0 and $h(x)$ = 0 then cost = 0

### Now when you combine this two graph you'll get

<img src="./images/cost_fun_for_logisitic_regression_combine.png" style="width:600px">

this is a convex graph

### Updated cost function

$$\boxed{cost(h_\Theta(x^i, y)) = -y\ log(h_\Theta(x^i)) - (1-y)\ log(1-h_\Theta(x))}$$

<!-- Note that:
- for y = 0 : $cost(h_\Theta(x^i, y)) = -0 - 1 \times log(1-h_\Theta(x)) = - log(1-h_\Theta(x))$
- for y = 1 : $cost(h_\Theta(x^i, y)) = -1 \times log(h_\Theta(x^i)) - 0 = -log(h_\Theta(x^i))$
- this is how we handle those boundary condition -->

#### Explanation

**When y=1:**

$$cost(h_\Theta(x^i, y)) = -log(h_\Theta(x^i))$$

The second term becomes zero, since $(1 - y ) = 0$

**When y=0:**

$$cost(h_\Theta(x^i, y)) = -log(1 - h_\Theta(x^i))$$

The first term becomes zero, since $y = 0$

**Therefor we can wite:**

$$\boxed{J(\Theta_1) =-\frac{1}{n} \sum \left[ -y\ log(h_\Theta(x^i)) - (1-y)\ log(1-h_\Theta(x))\right]}$$

Where:

$$h_0(x^i) = \frac{1}{1 + e^{\Theta_ix}}$$

[Go To Top](#content)

---

# Confusion Matrix

the confusion matrix is one of the most important tools to evaluate a classification model (like logistic regression).

A confusion matrix is a summary table used to evaluate how well a classification model performs — especially binary models like Logistic Regression.

It tells you where your model is getting confused — i.e., which classes it predicts correctly and which ones it mistakes.

### Structure of the Matrix

For binary classification (two classes: 0 and 1):
| **Actual \ Predicted** | **Predicted: 1 (Positive)** | **Predicted: 0 (Negative)** |
| ------------------------ | --------------------------- | --------------------------- |
| **Actual: 1 (Positive)** | ✅ **True Positive (TP)** | ❌ **False Negative (FN)** |
| **Actual: 0 (Negative)** | ❌ **False Positive (FP)** | ✅ **True Negative (TN)** |

### What Each Term Means

| Term                    | Meaning                                         | Real Example (Spam Email)                           |
| ----------------------- | ----------------------------------------------- | --------------------------------------------------- |
| **TP** (True Positive)  | Model predicted **1** and it was actually **1** | Predicted spam → actually spam ✅                   |
| **TN** (True Negative)  | Model predicted **0** and it was actually **0** | Predicted not spam → actually not spam ✅           |
| **FP** (False Positive) | Model predicted **1** but it was **0**          | Predicted spam → actually not spam ❌ (false alarm) |
| **FN** (False Negative) | Model predicted **0** but it was **1**          | Predicted not spam → actually spam ❌ (missed case) |

xx

### Example

Suppose you built a model to detect spam emails:
| Actual | Predicted |
| :----: | :-------: |
| 1 | 1 |
| 0 | 0 |
| 1 | 0 |
| 0 | 1 |
| 1 | 1 |

Now count:

-   TP = 2 → (1→1 twice)
-   TN = 1 → (0→0 once)
-   FP = 1 → (0→1 once)
-   FN = 1 → (1→0 once)

In matrix format:

|                          | Predicted: Spam (1) | Predicted: Not Spam (0) |
| ------------------------ | ------------------- | ----------------------- |
| **Actual: Spam (1)**     | **TP = 2**          | **FN = 1**              |
| **Actual: Not Spam (0)** | **FP = 1**          | **TN = 1**              |

[Go To Top](#content)

---

# Calculate Accuracy from the Confusion Matrix

> Make sure you know about [confusion matrix](#confusion-matrix)

### Formula for Accuracy:

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

Where:

-   TP = True Positive
-   TN = True Negative
-   FP = False Positive
-   FN = False Negative

> Accuracy = (All Correct Predictions) / (All Predictions)

### Example

| **Actual \ Predicted** | **Predicted: 1** | **Predicted: 0** |
| ---------------------- | ---------------- | ---------------- |
| **Actual: 1**          | TP = 50          | FN = 10          |
| **Actual: 0**          | FP = 5           | TN = 35          |

Now plug values into the formula:

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

$$Accuracy = \frac{50 + 35}{50 + 35 + 5 + 10} = \frac{85}{100} = 0.85$$

Accuracy = 85%

[Go To Top](#content)

---

# Precision, Recall, and F1 (F-Beta)

> Make sure you know about [confusion matrix](#confusion-matrix) as they all come directly from the Confusion Matrix

### 1. Precision

Definition:\
Of all the points predicted as positive, how many were actually positive?

$$Precision = \frac{TP}{TP + FP}$$

High precision = very few false alarms (model rarely predicts “positive” when it’s wrong).

Example (spam filter):\
If 100 emails were predicted as spam, and 90 were actually spam →

$$Precision = \frac{90}{100} = 0.9$$

> Model predict -> 100 positive -> out of those 100 only 90 are actually positive

> We do not care how many positive entries are present in our original dataset — it might have 120 or only 90 positive entries. What we care about is: out of all the positive predictions, what percentage of predictions is correct.

> Think of it like: “Be careful when calling something positive”

### 2. Recall (Sensitivity or True Positive Rate)

Definition:\
Of all the actual positives, how many did the model correctly detect?

$$Recall = \frac{TP}{TP + FN}$$

High recall = model catches almost all real positives (even if some false positives).

Example (spam filter):\
If there were 120 spam emails total and your model caught 90 →

$$Recall = \frac{90}{120} = 0.75$$

> model predict -> 90 positive -> original dataset have 120 positive

> Here we care about our original dataset and check how many positive entry was detected by our model

> Think of it like: “How many actual positives you catch”

### 3. F1 Score (or F-Beta Score)

Definition:\
The harmonic mean of precision and recall — it balances both.

$$F1 = (1 + \beta^2) \times \frac{Precision \times Recall}{Precision + Recall}$$

High F1 means both precision and recall are good (balanced performance).
If one is low, F1 also drops.

Example:\
If Precision = 0.9, Recall = 0.75, Beta = 1

$$F1 = 2 \times \frac{0.9 \times 0.75}{0.9 + 0.75} = 0.814$$

> Note: \
> $\beta = 1$ means focus is on both FP and FN \
> $\beta \lt 1$ means FP is more important than that of FN\
> $\beta \gt 1$ means FN is more important than that of FP

### Example:

A hospital uses an AI model to detect if a person has diabetes.\
(1 = has diabetes, 0 = healthy)

| Patient | **Actual (True)** | **Predicted (Model)** |
| :------ | :---------------: | :-------------------: |
| 1       |         1         |           1           |
| 2       |         0         |           0           |
| 3       |         1         |           1           |
| 4       |         1         |           0           |
| 5       |         0         |           1           |
| 6       |         0         |           0           |
| 7       |         1         |           1           |
| 8       |         0         |           0           |

Confusion Matrix:
| **Actual \ Predicted** | **Predicted: Diabetes (1)** | **Predicted: Healthy (0)** |
| ------------------------ | --------------------------- | -------------------------- |
| **Actual: Diabetes (1)** | ✅ **TP = 3** | ❌ **FN = 1** |
| **Actual: Healthy (0)** | ❌ **FP = 1** | ✅ **TN = 3** |

**Precision**

$$Precision = \frac{TP}{TP+FP} = \frac{3}{3+1} = 0.75$$

Precision = 75%

> Out of all people predicted diabetic Patient, 75% actually had diabetes.

**Recall (Sensitivity)**

$$Precision = \frac{TP}{TP+FN} = \frac{3}{3+1} = 0.75$$

Recall = 75%

> The model correctly identified 75% of all actual diabetic patients.

**F1 Score ($\beta = 1$)**

$$F1 = (1 + \beta^2) \times \frac{Precision \times Recall}{Precision + Recall}$$

$$F1 = 2 \times \frac{0.75 \times 0.75}{0.75 + 0.75} = 0.75$$

F1 = 75%

[Go To Top](#content)

---

# Naïve Bayes Algorithm

Naïve Bayes is a probabilistic model based on Bayes’ Theorem, assuming that all input features are independent given the target.

### Independent and Dependent Events

An event is any possible outcome or set of outcomes from an experiment.

Example:

-   Toss a coin → event “Head”
-   Roll a die → event “getting 6”

**Independent Events**

-   Two events are independent if the occurrence of one does not affect the occurrence of the other.
-   Example: - Event A: Toss a coin → get Head - Event B: Roll a die → get 6

        These two events don’t affect each other.

    So they are independent.

-   Mathematically:
    $$\text{P(A and B)} = P(A) \times P(B)$$

**Dependent Events**

-   Two events are dependent if the occurrence of one affects the probability of the other.
-   Example:\
    You draw 2 cards from a deck without replacement
    (meaning you don’t put the first card back). - Event A: First card is an Ace - Event B: Second card is an Ace

        After drawing the first Ace, there are fewer Aces and fewer total cards left.\
        So event B depends on event A → dependent events.

-   Mathematically:

$$\text{P(A and B)} = P(A) \times P(B|A)$$

Where $\text{P(A and B)}$ means “probability of B given A has already happened”.

**Quick Comparison**
| Type | Definition | Example | Formula |  
| ---------------------- | ---------------------------------------- | --------------------------------- | -------------------------- |
| **Independent Events** | One doesn’t affect the other | Tossing a coin & rolling a die | $P(A \cap B) = P(A)P(B)$ |  
| **Dependent Events** | One affects the probability of the other | Drawing cards without replacement | $P(A \cap B) = P(A)P(BA)$ |

### Bayes’ Theorem

Bayes’ theorem helps us update our belief about an event when we get new evidence.

It answers this question:\
“Given that we have some evidence, what is the probability that our hypothesis is true?”

**Formula**

$$P(B∣A) = \frac{p(A|B) \times P(B)}{P(A)}$$

Where:

| Term | Meaning                                                                    |
| ---- | -------------------------------------------------------------------------- |
| P(A) | **Prior probability** → your initial belief about A before seeing evidence |
| P(B) | **Evidence** → probability of seeing B (used for normalization)            |

### Naïve Bayes

Naïve Bayes is a supervised learning algorithm based on Bayes’ Theorem, used mainly for classification (like spam detection, sentiment analysis, disease prediction, etc.).

It’s called “naïve” because it assumes all features are independent — which is rarely true in real life, but surprisingly it still works very well.

> It Assume each feature is independent of one another but output is still depend on each individual feature

**Formula Using Bayes’ theorem:**

$$P(Y∣X_1​,X_2​,...,X_n​) = \frac{P(X_1​,X_2​,...,X_n​∣Y)⋅P(Y)​}{P(X_1​,X_2​,...,X_n​)}$$

<br/>
<br/>

As each feature is independent of one another we can also write:

$$P(X_1​,X_2​,...,X_n​∣Y) = P(X_1|Y) \times P(X_2|Y) ...... P(X_n|Y)_{-------------}(i)$$

$$P(X_1​,X_2​,...,X_n​) = p(X_1) \times p(X_2) ...... p(X_n)_{------------}(ii)$$

<br/>
<br/>

Therefor by putting $i$ and $ii$ into our main equation we get:

$$\boxed{P(Y∣X_1​,X_2​,...,X_n​) = \frac{P(Y) ⋅ \left[P(X_1|Y) \times P(X_2|Y) ...... P(X_n|Y)  \right]}{p(X_1) \times p(X_2) ...... p(X_n) } }$$

Here:

-   $X_i$ = features
-   $Y$ = classes

Since $p(X_1) \times p(X_2) ...... p(X_n)$ is same for all of the classes, we only care about the numerator and can ignore the denominator

> This equation says that what is the probability features $X_i$ belongs to class $Y$

### Lets understand how this equation works

let say we have multiple feature called $X$ and two classes let say Yes(1) and NO(0)

now we want to check whether our new data entry containing all features $X_i$ is belong to which class?

<br/>
<br/>

to check whether it is belong to class Yes:

$$P(Y = Yes∣X_1​,X_2​,...,X_n​) = P(Y = Yes) \times \left[P(X_1|Y) \times P(X_2|Y) ...... P(X_n|Y)  \right]$$

> This equation says that what is the probability features $X_i$ belongs to class $Y = Yes$

<br/>
<br/>

to check whether it is belong to class No:

$$P(Y = No ∣X_1​,X_2​,...,X_n​) = P(Y = No) \times \left[P(X_1|Y) \times P(X_2|Y) ...... P(X_n|Y)  \right]$$

> This equation says that what is the probability features $X_i$ belongs to class $Y = No$

<br/>
<br/>

Let say we get output like:

$$P(Y = Yes∣X_1​,X_2​,...,X_n​) = 0.13$$

$$P(Y = No ∣X_1​,X_2​,...,X_n​) = 0.05$$

> In binary classification we know that:
>
> Y = 1 if and only if P(Y) >= 0.5\
> if P(Y) < 0.5 then Y = 0

Normalize this probability:

> Normalization means scaling data so that all feature values lie in a similar range (commonly between 0 and 1).

$$P(Y = Yes∣X_1​,X_2​,...,X_n​) = \frac{0.13}{0.13 + 0.05} = 0.72 = \text{72\%}$$
$$P(Y = No∣X_1​,X_2​,...,X_n​) = \frac{0.05}{0.13 + 0.05} = 0.28 = \text{28\%}$$

from this we can say that for input features $X_i$ we will get $Y = Yes$

That is inputted data($X_i$ features) belongs to class($Y$) Yes

### Example:

lets predict whether a person buys a computer based on Age and Income.

| Age    | Income | Buys |
| ------ | ------ | ---- |
| Young  | High   | No   |
| Young  | High   | No   |
| Middle | High   | Yes  |
| Old    | Medium | Yes  |
| Old    | Low    | Yes  |
| Old    | Low    | No   |
| Middle | Low    | Yes  |
| Young  | Medium | No   |
| Young  | Low    | Yes  |
| Old    | Medium | Yes  |

We’ll predict for this person:\
**Age = Young, Income = Medium**

#### Step 1: Find Prior Probabilities

Count how many “Yes” and “No” labels:

-   Yes = 6
-   No = 4
-   Total = 10

$$P(Yes) = \frac{6}{10} = 0.6$$

$$P(No) = \frac{4}{10} = 0.4$$

#### Step 2: Find Conditional Probabilities

For Age:

| Age    | Yes count | No count | P(Yes) = Yes count/Total Yes count | P(No) = No count/Total No count |
| ------ | --------- | -------- | ---------------------------------- | ------------------------------- |
| Young  | 1         | 3        | 1/6                                | 3/4                             |
| Middle | 2         | 0        | 2/6                                | 0/4                             |
| Old    | 3         | 1        | 3/6                                | 1/4                             |
| Total  | 6         | 4        |

For Income:

| Income | Yes count | No count | P(Yes) = Yes count/Total Yes count | P(No) = No count/Total No count |
| ------ | --------- | -------- | ---------------------------------- | ------------------------------- |
| High   | 1         | 2        | 1/6                                | 2/4                             |
| Medium | 2         | 1        | 2/6                                | 1/4                             |
| Low    | 3         | 1        | 3/6                                | 1/4                             |
| Total  | 6         | 4        |

#### Step 3: Apply Bayes’ Theorem

For the person (Young, Medium)

<br/>
<br/>

**Case 1: “Yes”**

$$P(Yes∣Young,Medium) = P(Yes) \times P(Young | yes) \times P(Medium | yes)$$

$$ = 0.6 \times \frac{1}{6} \times \frac{2}{6} = 0.033 $$

<br/>
<br/>

**Case 1: No**

$$P(No∣Young,Medium) = P(No) \times P(Young | No) \times P(Medium | No)$$

$$ = 0.4 \times \frac{3}{4} \times \frac{1}{4} = 0.075 $$

#### Step 4: Normalization, Compare and Decide

$$P(Yes∣Young,Medium) = \frac{0.033}{0.033 + 0.075} = 0.30 = 30\%$$

$$P(No∣Young,Medium) = \frac{0.075}{0.033 + 0.075} = 0.70 = 70\%$$

The higher probability is for “No”\
Prediction → Person will NOT buy a computer

[Go To Top](#content)

---

# KNN Algorithm

-   Also known as K-Nearest Neighbors
-   KNN is a supervised learning algorithm used for classification and regression problems.
-   It works purely on the idea of similarity (distance)
    > “If something looks like its neighbors, it probably belongs to the same group.”

### How it Works for Classification Problem

Let’s assume we’re classifying whether a student will pass or fail based on hours studied and sleep hours.

1. **Store all training data points**\
   Each data point has features (hours studied, sleep hours) and a label (Pass/Fail).
2. **Pick the number `K`**\
   Example: `K = 3` → look at 3 nearest neighbors.
3. **Calculate distance**\
   For a new student’s data, calculate the distance between this student and all others
4. **Find K nearest neighbors**\
   Sort distances and take the K(`K = 3`) closest points.
5. **Majority voting (for classification)**\
   Check which label (Pass or Fail) appears most among these K points.

6. **Assign the class**\
   The new student gets the label that most neighbors have.

### Example

| Hours Studied | Sleep Hours | Result |
| ------------: | ----------: | :----- |
|           5.0 |         7.0 | Pass   |
|           2.0 |         5.5 | Fail   |
|           4.5 |         5.0 | Pass   |
|           1.0 |         3.0 | Fail   |
|           6.5 |         8.0 | Pass   |
|           3.0 |         4.0 | Fail   |
|           5.5 |         6.5 | Pass   |
|           2.5 |         3.5 | Fail   |

Predict for `(3, 5)` (new student).

1. Compute distances to all points
2. Select 3 nearest points (`K=3`)
3. Suppose 2 are “Fail” and 1 is “Pass”\
   ✅ → Predicted: Fail

#### To understand visually:

<img src="./images/KNN_classsification.png" style="background:white; width:600px">

### How it Works for Regression Problem

1. **Store all training data points**\
   Each data point has features (hours studied, sleep hours) and a label (Pass/Fail).
2. **Pick the number `K`**\
   Example: `K = 3` → look at 3 nearest neighbors.
3. **Calculate distance**\
   For a new student’s data, calculate the distance between this student and all others
4. **Find K nearest neighbors**\
   Sort distances and take the K(`K = 3`) closest points.

5. **Take the average of their target values**\
   Instead of “majority vote,” we take the mean (or weighted mean).

6. **Assign that average as the prediction**\
   That’s your final output.

### Example

| Size (sq.ft) | Price ($000) |
| -----------: | -----------: |
|          950 |          145 |
|         1100 |          175 |
|         1350 |          190 |
|         1600 |          230 |
|         1800 |          260 |
|         2100 |          300 |
|         2500 |          350 |
|         2900 |          420 |

Predict for size = 2000 and K = 3

1. Compute distances:

2. nearest 3 neighbors: (1600→230), (1800→260), (2100→300)
3. Average: (230 + 260 + 300)/3 = 790/3 = 263.33

Predicted price = $263,333

#### To understand visually

<img src="./images/KNN_regression.png" style="background:white; width:600px">

### Formula to calculate distance

#### 1. Euclidean Distance (default)

$$d(p, q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}$$

**Example**\
Between (2,3) and (5,7):

$$\sqrt{(2-5)^2 + (3-7)^2} = \sqrt{9 + 16} = 5$$

#### 2. Manhattan Distance (City Block Distance)

$$d(p, q) = |x_1 - y_1| + |x_2 + y_2| + ... + |x_n + y_n|$$

**Example:**\
Between (2,3) and (5,7):

$$∣2−5∣+∣3−7∣=3+4=7$$

#### Difference between Euclidean and Manhattan Distance

<img src="./images/distance_type.jpg" style="background:white; width:600px">

### When KNN fails

1. **High-Dimensional Data (Curse of Dimensionality)**

    - When you have many features (columns) — like 100+ — the distance between points becomes less meaningful.
    - All points start to seem equally far apart, so "nearest" neighbors aren’t truly similar anymore.

2. **Large Datasets**
    - KNN is a lazy learner, meaning it stores all training data and compares with every point during prediction.
    - For large datasets, this makes predictions slow (O(n) time per query).
3. **Unscaled Features** - KNN relies on distance — if features are on different scales, one feature can dominate. - Example:\
   If you mix “age (0–100)” and “income (0–1000000)”, income will outweigh age.
4. **Imbalanced Data** - When one class has many more samples, the majority class dominates neighbor votes. - Example:\
   If 90% are “Pass” and 10% are “Fail,” most predictions will be “Pass.”
5. **Noisy Data**
    - If training data contains outliers or mislabeled points, KNN will easily get confused since it treats all data equally.

[Go To Top](#content)

---

# Decision Tree

A Decision Tree is a supervised learning algorithm that makes predictions by asking a series of yes/no questions based on feature values — just like how humans make decisions.

> “If marks > 80 → Pass else → Fail.”

### Structure

```css
        [Root Node]
           ↓
   ┌───────┴────────┐
[Decision Node]   [Decision Node]
   ↓                   ↓
[Leaf Node]         [Leaf Node]
```

-   Root Node → first split (best feature)
-   Decision Node → internal condition
-   Leaf Node → final output (class/value)

### Example:

let say we have code like

```py
if(age <= 20):
    print("study")
elif(age > 20 and age <= 35):
    print("work")
else:
    print("retire")
```

Decision Tree Representation

```yaml
                [age <= 20 ?]
                  /       \
              Yes          No
            study        [age <= 35 ?]
                           /       \
                        Yes         No
                       work       retire
```

### Example with dataset

here we split the dataset into groups (branches)
|person| Weather | will dink cola? |
| --- | --- | --- |
| A | worm | yes
| B | cool | no
| C | mild | yes
| D | mild | no

```yaml
   [ Whether ]
   /    |    \
 worm  mild  cool
 /     /  \    \
yes  yes  no    no
```

### Pure and Impure Split

When we split the dataset into groups (branches),
we want each group to contain only one type of output class (like all “Yes” or all “No”).

-   Pure Split:\
    → All samples in the branch belong to one class.\
    → Example: all are “Play = Yes”.
-   Impure Split:\
    → The branch has a mix of classes.\
    → Example: some “Yes” and some “No”.

**Example: Play Tennis Dataset**
| Outlook | Temperature | Humidity | Play |
| -------- | ----------- | -------- | ---- |
| Sunny | Hot | High | No |
| Sunny | Mild | Normal | Yes |
| Overcast | Cool | Normal | Yes |

Let’s say we split by Outlook.

**Split 1: Outlook = "Overcast"**
| Outlook | Play |
| -------- | ---- |
| Overcast | Yes |

All “Yes” → Pure Split

**Split 2: Outlook = "Sunny"**
| Outlook | Play |
| ------- | ---- |
| Sunny | No |
| Sunny | Yes |

Mixed “Yes” and “No” → Impure Split

### Purity

Purity tells how mixed or uniform a group (node) is after a split.

-   If all records belong to the same class → node is pure (good).
-   If records are mixed (Yes/No, Spam/NotSpam) → node is impure (bad).

> Pure Split → high Purity (good)\
> Impure Split → low Purity (bad)

There are various way to calculate the purity of the node but most useful are as follow

1. [Entropy](#entropy) : measure of uncertainty, disorder, or impurity in the data.
2. Gini Coefficient

[Go To Top](#content)

---

# Entropy

Entropy = measure of uncertainty, disorder, or impurity in the data.

-   If all outcomes are the same → no uncertainty → low entropy (0)
-   If outcomes are mixed → high uncertainty → high entropy (1)

It tells the algorithm how confused it is about the class labels in a group.

### Mathematical Formula

$$Entropy = - \sum p_i\ \log_2(p_i)$$

where:

-   $p_i$ = probability of class i (like Yes or No)
-   The sum runs over all possible classes.

### Example

Imagine you have a box of balls:

| Box | Red Balls | Blue Balls | Total |
| --- | --------- | ---------- | ----- |
| A   | 5         | 0          | 5     |
| B   | 3         | 2          | 5     |
| C   | 2         | 2          | 4     |

We’ll calculate Entropy for each box using:

$$Entropy = - \left[P_{red}\ \log_2(P_{red}) + P_{blue}\ \log_2(P_{blue})  \right]$$

#### For Box A

Red = 5, Blue = 0, Total = 5

$$P_{red} = 5 / 5 = 1$$

$$P_{blue} = 0 / 5 = 0$$

$$Entropy = - \left[ 1 \times\log_2 (1) + 0 \times\log_2 (0) \right]$$

Since $\log_2(1) = 0$ and $0\log_2(0)$ is treated as 0

$$Entropy = - \left[ 1 \times 0 + 0 \right] = 0$$

Box A Entropy = 0 (pure)

#### For Box B

Red = 3, Blue = 2, Total = 5

$$P_{red} = 3 / 5 = 0.6$$

$$P_{blue} = 2 / 5 = 0.4$$

$$Entropy = - \left[ 0.6 \times\log_2 (0.6) + 0.4 \times\log_2 (0.4) \right]$$

Now calculate:

-   $\log_2(0.6) = -0.737$
-   $\log_2(0.4) = -1.322$

$$Entropy = - \left[ 0.6 \times -0.737 + 0.4 \times -1.322 \right]$$

$$Entropy = - \left[ -0.422 - 0.529 \right] = 0.971$$

Box B Entropy ≈ 0.97 (medium impurity)

#### For Box B

Red = 2, Blue = 2, Total = 4

$$P_{red} = 2 / 4 = 0.5$$

$$P_{blue} = 2 / 4 = 0.5$$

$$Entropy = - \left[ 0.5 \times\log_2 (0.5) + 0.5 \times\log_2 (0.5) \right]$$

Now calculate:

-   $\log_2(0.5) = -1$

$$Entropy = - \left[ 0.5 \times -1 + 0.5 \times -1 \right]$$

$$Entropy = - \left[ -0.5 - 0.5 \right] = 1$$

Box C Entropy = 1 (completely impure)

[Go To Top](#content)

---

# Gini Coefficient

Gini impurity tells us how mixed the classes are in a group (or node).

It answers this question:

> “If I randomly pick two items from this group, what are the chances they belong to different classes?”

> Lower Gini → low mixed → purer node → better split.\
> Higher Gini → high mixed → impure node → poor split

### Formula

$$Gini = 1 - \sum(p_i)^2$$

Where:

-   $p_i$ = probability of each class 𝑖

### Example

let say you have dataset like:

| Person | Weather  | Play Tennis |
| ------ | -------- | ----------- |
| 1      | Sunny    | No          |
| 2      | Sunny    | No          |
| 3      | Overcast | Yes         |
| 4      | Rain     | Yes         |
| 5      | Rain     | Yes         |
| 6      | Rain     | No          |
| 7      | Overcast | Yes         |
| 8      | Sunny    | Yes         |

We want to build a Decision Tree that predicts Play Tennis (Yes/No) using Weather as the feature.

To do that, we’ll calculate the Gini impurity of each split.

#### Gini of the Whole Dataset

Count the classes:
| Class | Count |
| ----- | ----- |
| Yes | 5 |
| No | 3 |

Total = 8 samples

$$p(yes) = 5/8,\ \ \ p(no) = 3/8 $$

$$Gini = 1 - \left[p(yes)^2 + p(no)^2 \right]$$

$$ = 1 - \left[(5/8)^2 + (3/8)^2 \right]$$

$$= 1 - (0.3906 + 0.1406) = 0.4688$$

**Gini(Whole Dataset) = 0.47**

#### Split by “Weather” - Weather = Sunny

| Play | Count |
| ---- | ----- |
| Yes  | 1     |
| No   | 2     |

$$p(yes) = 1/3,\ \ \ p(no) = 2/3 $$

$$Gini(sunny) = 1 - \left[(1/3)^2 + (2/3)^2 \right]$$

$$ = 1-(0.111 + 0.444) = 0.445$$

**Gini(Sunny) = 0.445**

#### Split by “Weather” - Weather = Overcast

| Play | Count |
| ---- | ----- |
| Yes  | 2     |
| No   | 0     |

$$p(yes) = 1,\ \ \ p(no) = 0 $$

$$Gini(Overcast) = 1 - \left(1^2 + 0^2 \right) = 0$$

**Pure node → Gini = 0**

#### Split by “Weather” - Weather = Rain

| Play | Count |
| ---- | ----- |
| Yes  | 2     |
| No   | 1     |

$$p(yes) = 2/3,\ \ \ p(no) = 1/3 $$

$$Gini(Rain) = 1 - \left[(2/3)^2 + (1/3)^2 \right]$$

$$ = 1-(0.444 + 0.111) = 0.445$$

**Gini(Rain) = 0.445**

[Go To Top](#content)

---

# Information Gain

Information Gain (IG) tells us how much “purity” improves after we split the dataset using a feature.

In other words:\
 It measures how much uncertainty (impurity) is reduced by a particular feature split.

> higher the IG higher the purity of node after splitting

### Formula (using Entropy)

$$IG = Entropy(Parent) - \sum \left(\frac{n_{child}}{n_{parent} } \times Entropy(Child) \right)$$

Here:

-   $n_{child}$ = no. child sample
-   $n_{parent}$ = no. parent sample

> Information Gain = Original Entropy − Weighted Average Entropy of Child Nodes

> Instead of Entropy we can also use Gini coefficient

### Example

Let’s take a mini dataset
| Weather | Play |
| -------- | ---- |
| Sunny | No |
| Sunny | No |
| Overcast | Yes |
| Rain | Yes |
| Rain | No |

#### Step 1 — Calculate Entropy before split

| Play | Count |
| ---- | ----- |
| Yes  | 2     |
| No   | 3     |

$$p(Yes) = 2/5, \ \ \ p(No) = 3/5$$

$$Entropy(Parent) = - \left( \frac{2}{5} \log_2 \frac{2}{5} + \frac{3}{5} \log_2 \frac{3}{5} \right)$$

$$=−(0.4×−1.32+0.6×−0.736)=0.971$$

**Entropy(Parent) = 0.97**

#### Step 2️ — Split by “Weather”

-   Weather = Sunny:\
    2 samples → [No, No] → Pure → Entropy = 0

-   Weather = Overcast:\
    1 sample → [Yes] → Pure → Entropy = 0

-   Weather = Rain:\
    2 samples → [Yes, No] → Mixed

        $Entropy = -(0.5 \log_2 0.5 + 0.5 \log_2 0.5) = 1$

#### Step 3️ — Weighted Average Entropy after split

$$\sum \left(\frac{n_{child}}{n_{parent} } \times Entropy(Child) \right) = \left(\frac{2}{5} \times 0 \right) + \left(\frac{1}{5} \times 0 \right) + \left(\frac{2}{5} \times 1 \right) = 0.4$$

#### Step 4️ — Information Gain

$$IG = Entropy(Parent) - \sum \left(\frac{n_{child}}{n_{parent} } \times Entropy(Child) \right)$$

$$IG = 0.97 - 0.4 = 0.57$$

**Information Gain = 0.57**

That means:\
Splitting by Weather reduces our confusion by 0.57 bits of information — it made the data much more pure.

[Go To Top](#content)

---

# Decision Tree for Classification

In classification, a Decision Tree predicts a category (like Yes/No, Pass/Fail, Spam/Not Spam).

### Understand how it work

let say we have dataset like:

| Outlook  | Temperature | Humidity | Wind   | Play Tennis |
| -------- | ----------- | -------- | ------ | ----------- |
| Sunny    | Hot         | High     | Weak   | No          |
| Sunny    | Hot         | High     | Strong | No          |
| Overcast | Hot         | High     | Weak   | Yes         |
| Rain     | Mild        | High     | Weak   | Yes         |
| Rain     | Cool        | Normal   | Weak   | Yes         |
| Rain     | Cool        | Normal   | Strong | No          |
| Overcast | Cool        | Normal   | Strong | Yes         |
| Sunny    | Mild        | High     | Weak   | No          |
| Sunny    | Cool        | Normal   | Weak   | Yes         |
| Rain     | Mild        | Normal   | Weak   | Yes         |
| Sunny    | Mild        | Normal   | Strong | Yes         |
| Overcast | Mild        | High     | Strong | Yes         |
| Overcast | Hot         | Normal   | Weak   | Yes         |
| Rain     | Mild        | High     | Strong | No          |

Target variable → Play Tennis (Yes / No)

and our goal is to build a Decision Tree to predict Play Tennis (Yes or No) based on the weather conditions.

### Step 1: Calculate Total Entropy

We have:

-   9 “Yes”
-   5 “No”

$$Entropy(S) = -\frac{9}{14} \log_2 (\frac{9}{14})-\frac{5}{14} \log_2 (\frac{5}{14})$$

$$Entropy(S)=0.94$$

This is our starting impurity before splitting.

### Step 2: Test Each Feature to Find the Best Split

We’ll compute Information Gain (IG) for each feature —
the one with the highest IG becomes the Root Node.

#### Feature 1: Outlook

| Outlook  | Yes | No  | Entropy |
| -------- | --- | --- | ------- |
| Sunny    | 2   | 3   | 0.97    |
| Overcast | 4   | 0   | 0       |
| Rain     | 3   | 2   | 0.97    |

Weighted Entropy:

$$E(Outlook) = \frac{5}{14}(0.97) + \frac{4}{14}(0) + \frac{5}{14}(0.97) = 0.693$$

Information Gain:

$$\boxed{IG(Outlook)=0.94−0.693=0.247}$$

#### Feature 2: Temperature

| Temp | Yes | No  | Entropy |
| ---- | --- | --- | ------- |
| Hot  | 2   | 2   | 1.0     |
| Mild | 4   | 2   | 0.918   |
| Cool | 3   | 1   | 0.811   |

Weighted Entropy:

$$E(Temp) = \frac{4}{14}(1) + \frac{6}{14}(0.918) + \frac{4}{14}(0.811) = 0.911$$

Information Gain:

$$\boxed{IG(Temp)=0.94−0.911=0.029}$$

#### Feature 3: Humidity

| Humidity | Yes | No  | Entropy |
| -------- | --- | --- | ------- |
| High     | 3   | 4   | 0.985   |
| Normal   | 6   | 1   | 0.592   |

Weighted Entropy:

$$E(Humidity) = \frac{7}{14}(0.985) + \frac{7}{14}(0.592)  = 0.789$$

Information Gain:

$$\boxed{IG(Humidity)=0.94−0.789=0.151}$$

#### Feature 4: Wind

| Wind   | Yes | No  | Entropy |
| ------ | --- | --- | ------- |
| Weak   | 6   | 2   | 0.811   |
| Strong | 3   | 3   | 1.0     |

Weighted Entropy:

$$E(Wind) = \frac{8}{14}(0.811) + \frac{6}{14}(1)  = 0.892$$

Information Gain:

$$\boxed{IG(Wind)=0.94−0.892=0.048}$$

### Step 3: Choose the Best Split

Information Gain (IG) tells us how much “purity” improves after we split the dataset using a feature.

> higher the IG higher the purity of node after splitting

| Feature     | Info Gain |
| ----------- | --------- |
| Outlook     | 0.247 ✅  |
| Temperature | 0.029     |
| Humidity    | 0.151     |
| Wind        | 0.048     |

So the best feature = Outlook → it becomes our Root Node.

### Step 4: Split the Tree by Outlook

```
             [Outlook]
            /    |     \
         Sunny  Overcast  Rain
```

Now handle each branch separately

> Perform step 1 to 4 for each branch

#### Case 1: Outlook = Overcast

All “Yes” → pure branch → Leaf Node = Yes

#### Case 2: Outlook = Sunny

Subset:

| Humidity | Play |
| -------- | ---- |
| High     | No   |
| High     | No   |
| High     | No   |
| Normal   | Yes  |
| Normal   | Yes  |

-   If Humidity = High → No
-   If Humidity = Normal → Yes

Split rule: Sunny → Humidity

#### Case 3: Outlook = Rain

Subset:
| Wind | Play |
| ------ | ---- |
| Weak | Yes |
| Weak | Yes |
| Weak | Yes |
| Strong | No |
| Strong | No |

-   If Wind = Weak → Yes
-   If Wind = Strong → No

Split rule: Rain → Wind

### Final Decision Tree

```
                [Outlook]
              /     |      \
        Sunny     Overcast    Rain
         |            |          |
     [Humidity]       Yes      [Wind]
      /      \                  /   \
   High      Normal        Strong   Weak
    No          Yes           No      Yes
```

[Go To Top](#content)

---

# Decision Tree for Regression

A Regression Tree splits the data into groups so that each group has similar numeric values.
Instead of trying to make groups “pure by class,” it tries to make groups where the numbers are close to each other.

### Example

| Hours | Marks |
| ----- | ----- |
| 1     | 40    |
| 2     | 45    |
| 3     | 50    |
| 6     | 80    |
| 7     | 85    |

We will build a regression tree to predict Marks.

We will try splits on Hours and choose the best one using [MSE](#mean-squared-error-mse).

### STEP 1 → Try a split

Try split at Hours < 4

#### Left node (Hours: 1,2,3)

Marks → [40, 45, 50]

Mean:

$$\bar{Y}_L = \frac{40 + 45 + 50}{3} = 45$$

MSE Left:

$$(40−45)^2+(45−45)^2+(50−45)^2 = 50 $$

#### Right node (Hours: 6,7)

Marks → [80, 85]

Mean:

$$\bar{Y}​_R​=82.5$$

MSE Right:

$$(80−82.5)_2+(85−82.5)_2 = 12.5$$

### STEP 2 → Weighted Total MSE

$$\text{Total MSE} = \frac{3}{5}(50) + \frac{2}{5} = (12.5) = 35$$

Total MSE for split “Hours < 4” = 35

### Now Tree Will Try Other Splits

Possible split points:

-   Hours < 2
-   Hours < 3
-   Hours < 4
-   Hours < 6

For each split, compute:

1. Mean of left group
2. MSE of left group
3. Mean of right group
4. MSE of right group
5. Weighted total MSE

Finally…\
Choose the split with the LOWEST total MSE.

### Final Regression Tree

```
                (root)
             Hours < 4 ?
             /         \
            /           \
       YES /             \ NO
          /               \
  Predict = 45         Predict = 82.5
(Avg of 40,45,50)   (Avg of 80,85)
```

[Go To Top](#content)

---

# Decision Trees Overfit

Decision Trees are one of the easiest models to overfit.

### Why?

A decision tree keeps splitting until:

-   every leaf becomes pure (all samples same output), or
-   each leaf contains only one sample.

This creates a tree that is:

-   very deep
-   very specific
-   memorizes the training data
-   captures noise instead of patterns

This is exactly what we call overfitting.

### Simple Example

Suppose your data has small variations:
| Hours | Marks |
| ----- | ----- |
| 1 | 40 |
| 2 | 45 |
| 3 | 50 |
| 6 | 80 |
| 7 | 83 |
| 8 | 81 |

A deep tree might create splits like:

```
      ┌───────────────────────────────┐
      │          Hours < 5 ?          │
      └───────────────────────────────┘
                /            \
               / YES          \ NO
              /                \
Predict = (left branch)      ┌────────────────────────┐
                             │      Hours < 6.5 ?     │
                             └────────────────────────┘
                               /             \
                              / YES           \ NO
                             /                 \
                    Predict = 80         ┌─────────────────────┐
                                         │     Hours < 7.5 ?   │
                                         └─────────────────────┘
                                           /            \
                                          / YES          \ NO
                                         /                \
                               Predict = 83            Predict = 81
```

What the Tree Learned
It memorized tiny differences:

-   6 hrs → 80
-   7 hrs → 83
-   8 hrs → 81

It assumes these exact boundaries are true forever.

### Now predict

New student studies 5.2 hours\
Realistic marks should be around 60–70

Tree says:

-   Hours < 5? → No\
    (because 5.2 > 5)
-   Hours < 6.5? → Yes\
    ➡ Predict = 80

This is huge error leading to overfitting

[Go To Top](#content)

---

# Ensemble Techniques

Ensemble techniques = using multiple models together to make a final prediction.

It means you don’t rely on one model, but combine many models to get:

-   higher accuracy
-   less overfitting
-   more stable predictions

> Think of it like taking multiple opinions instead of trusting only one person.

## Types of Ensembles

### 1. Bagging (Bootstrap Aggregating)

Idea: Train many same type of models on different random subsets of the data.

**Example**\
Imagine you train 100 decision trees:

-   each tree gets a random sample of rows
-   each tree trains separately
-   all trees vote together

Final prediction = majority vote (classification) or average (regression)

> you can combine multiple models (liner regression + KNN, etc) to make prediction each model will be trained on different subset

**Most famous Bagging algorithm is Random Forest**

### 2. Boosting

Idea: Train weak models one after another.
Each new model focuses on errors made by previous models.

**Example**

1. Train Tree 1
2. Check where Tree 1 made mistakes
3. Give those wrongly predicted samples more weight
4. Train Tree 2
5. Repeat…

Final prediction = weighted votes from all small trees.

**Famous Boosting algorithms**

-   AdaBoost
-   Gradient Boosting
-   XGBoost (most used)
-   LightGBM
-   CatBoost

### 3. Stacking

Idea: Use different models together and let another model learn how to combine them.

**Ensemble**

-   Model 1 → Logistic Regression
-   Model 2 → Naive Bayes
-   Model 3 → Decision Tree

All three give predictions.

Now you train a meta-model (e.g., Linear Regression) on those predictions to make the final output.

## To understand visually

<img src="./images/bagging-boosting-stacking.webp" style="width:800px">

[Go To Top](#content)

---

# Random Forest

It is an ensemble of many Decision Trees where:

-   each tree is trained on a random subset of rows
-   each tree sees only a random subset of features
-   all trees predict
-   final answer = majority vote (for classification) or average (for regression)

This randomness makes the model:

-   more accurate
-   more stable
-   less overfitted than a single tree

### Why Random Forest works better than a single Decision Tree?

One decision tree can become biased or overfit.

But if you train 100 different trees:

-   each tree gives a slightly different prediction
-   combining them reduces mistakes
-   like taking an opinion from 100 people instead of 1

### How it works

Suppose your dataset is:
| Age | Salary | Buy? |
| --- | ------ | ---- |
| 22 | 20k | No |
| 25 | 30k | No |
| 28 | 40k | Yes |
| 30 | 45k | Yes |
| 35 | 60k | Yes |

Random Forest wants to build, say, 3 trees.

#### Step 1 → Random samples for each tree (bootstrap sampling)

Tree 1 gets rows: 1, 2, 4, 5\
Tree 2 gets rows: 2, 3, 3, 4\
Tree 3 gets rows: 1, 3, 5, 5

> Repeating rows is allowed

#### Step 2 → Random features

Each split in a tree may choose from only 1 random feature:

-   Tree 1 might see only “Age”
-   Tree 2 might see only “Salary”
-   Tree 3 might see both but randomly selected at each split

#### Step 3 → Build 3 different Decision Trees

Each tree gives its own prediction for a new person.

Example input:\
Age = 27, Salary = 36k

Tree 1 → "Yes"\
Tree 2 → "No"\
Tree 3 → "Yes"

#### Step 4 → Final prediction

Classification → Majority vote\
Prediction: Yes (2 out of 3)

Regression → Average

### Key Concepts Inside Random Forest

-   Bootstrap sampling → random subset of rows for each tree
-   Feature randomness → random subset of features per split
-   Ensembling → multiple models combined
-   Voting/Averaging → final result

### Random Forest advantages

-   handles missing values well
-   reduces overfitting
-   works well for both regression & classification
-   supports high-dimensional data

### Disadvantages

-   slower than a single tree
-   not as interpretable
-   too many trees = more compute

[Go To Top](#content)

---

# AdaBoost

-   AdaBoost = Adaptive Boosting
-   It builds many weak models (usually tiny decision trees) one after another.
-   Each new model tries to fix the mistakes made by the previous one.

### Why “adaptive”?

Because after each model:

-   the samples that were predicted WRONG
-   the next model focuses more on those difficult samples

So the algorithm adapts to errors.

### stump

A stump means:\
A decision tree with only ONE split.

Visual

```
         (X < 5 ?)
         /     \
       0        1
```

### Why AdaBoost uses stumps?

Because AdaBoost wants weak models so it can boost them.

-   A stump is simple
-   Makes mistakes easily
-   AdaBoost can improve by adding more stumps

Each stump focuses on fixing previous stump’s mistakes.

### How AdaBoost Works

| ID  | X   | Class   |
| --- | --- | ------- |
| 1   | 1   | 0 (No)  |
| 2   | 2   | 0 (No)  |
| 3   | 8   | 1 (Yes) |
| 4   | 9   | 1 (Yes) |

We will train 2 stumps (tiny decision trees).

#### STEP 1 — Initial Weights

All data points get equal weight:

```
W = [0.25, 0.25, 0.25, 0.25]
```

> sum of their weight must be equal to 1

#### STEP 2 — Train Stump 1

Try a stump:

```py
if X < 9 → 0
else → 1
```

Predictions:
| ID | X | True | Pred | Correct? |
| -- | - | ---- | ---- | -------- |
| 1 | 1 | 0 | 0 | ✔ |
| 2 | 2 | 0 | 0 | ✔ |
| 3 | 8 | 1 | 0 | ❌ |
| 4 | 9 | 1 | 1 | ✔ |

Only one mistake (ID 3)

$\text{Total error (TE)} = 0.25$

#### STEP 3 — Compute α₁ (importance of stump 1)

$$\alpha_1 = \frac{1}{2}\ ln\left(\frac{1-TE}{TE} \right)$$

$$ = \frac{1}{2} \ ln \left(\frac{0.75}{0.25} \right) ≈ 0.55$$

#### STEP 4 — Update Weights

Weight update rule:

-   If prediction is correct → weight × $e^{-\alpha}$
-   If prediction is wrong → weight × $e^{+\alpha}$

Therefor:

$$e^{0.55} ≈ 1.73$$
$$e^{-0.55} ≈ 0.58$$

New weights
| ID | Correct? | Old W | New W |
| -- | -------- | ----- | -------------------- |
| 1 | ✔ | 0.25 | 0.25 × 0.58 = 0.145 |
| 2 | ✔ | 0.25 | 0.145 |
| 3 | ❌ | 0.25 | 0.25 × 1.73 = 0.4325 |
| 4 | ✔ | 0.25 | 0.145 |

Total Weight = 0.8675

> Total weight must be equal to 1, therefor to make it equal to 1 we perform normalization

Normalize:

$$Formula = \frac{\text{Weight of each row}}{\text{Total Weight}}$$

| ID  | Final Weight                              |
| --- | ----------------------------------------- |
| 1   | 0.167                                     |
| 2   | 0.167                                     |
| 3   | 0.498 _(highest weight — most difficult)_ |
| 4   | 0.167                                     |

#### STEP 5 — Train Stump 2 (focuses on mistake)

Try stump:

```py
if X < 1.5 → 0
else → 1
```

Predictions:
| ID | X | True | Pred | Weight | Correct? |
| -- | - | ---- | ---- | ------ | -------- |
| 1 | 1 | 0 | 0 | 0.167 | ✔ |
| 2 | 2 | 0 | 1 | 0.167 | ❌ |
| 3 | 8 | 1 | 1 | 0.498 | ✔ |
| 4 | 9 | 1 | 1 | 0.167 | ✔ |

$\text{Total error (TE)} = 0.167$

#### STEP 6 — Compute α₂

$$\alpha_2 = \frac{1}{2}\ ln\left(\frac{1-0.167}{0.167} \right) ≈ 0.80$$

### Final prediction

we use two methods to calculate the final output

1. majority vote (classification) or average(regression)
2. weighted voting

$$\text{final prediction} = sign(\alpha_1 \times prediction_1 + \alpha_2 \times prediction_2 )$$

> sign() just checks if the final score is:\
> positive → +1\
> negative → -1\
> zero → tie

[Go To Top](#content)

---

# K-Means Clustering

K-Means is an unsupervised learning algorithm used to group similar data points into K clusters.

<img src="./images/k-mean.webp" style="width:600px">

### How It Works

-   **Step 1: Choose K**\
    Decide how many clusters you want.
-   **Step 2: Pick K random centroids**\
    These are like “centers” of your clusters. > **Centroid:**\
     >A centroid is just the middle point of that group.
-   **Step 3: Assign points to nearest centroid**\
    Distance is usually Euclidean distance. > Euclidean Distance = straight-line distance\
     > Mathematically: > > $$Distance = \sqrt{(x_2 - x_1)^2 + (y_2-y_1)^2}$$
-   **Step 4: Recalculate centroids**\
    Each cluster’s centroid becomes the mean of all points inside it.

-   **Step 5: Repeat Steps 3–4**\
    Stop when centroids stop moving (converged).

### Example

Let’s say your dataset has students’ marks in two subjects:
| Student | Math | Science |
| ------- | ---- | ------- |
| A | 35 | 30 |
| B | 40 | 25 |
| C | 70 | 80 |
| D | 75 | 78 |
| E | 82 | 88 |

We want K = 2 clusters
(Cluster of weak students & cluster of strong students)

#### Step 1: Random centroids (start points)

Let’s pick:

-   Centroid 1 = (40, 30)
-   Centroid 2 = (70, 87)

<img src="./images/k-mean-example-1.png" style="width:400px">

#### Step 2: Assign students to nearest centroid

Cluster 1 (near C1):

-   A (35, 30)
-   B (40, 25)

Cluster 2 (near C2):

-   C (70, 80)
-   D (75, 78)
-   E (82, 88)

#### Step 3: Recalculate new centroids

**New Centroid 1**

-   Mean of A & B:
    -   Math = (35 + 40) / 2 = 37.5
    -   Science = (30 + 25) / 2 = 27.5
-   New C1 = (37.5, 27.5)

**New Centroid 2**

-   Mean of C, D, E:
    -   Math = (70 + 75 + 82) / 3 = 75.66
    -   Science = (80 + 78 + 88) / 3 = 82
-   New C2 = (75.66, 82)

<img src="./images/k-mean-example-2.png" style="width:400px">

#### Step 4: Reassign points

Try assigning again —
you’ll see students remain in the same clusters, so we stop.

#### Final Clusters

Cluster 1 → Weak Students

-   A
-   B

Cluster 2 → Strong Students

-   C
-   D
-   E

This is exactly what K-Means tries to find.

### Data points pull the centroid toward the center.

from above example we can see that every data point acts like a magnet, pulling the centroid towards them

Therefor the centroid moves to the place where all points are balance i.e the center of the cluster.

#### Imagine this

Suppose you have 3 points:

```
●         ●       ●
2         6       10
```

The centroid becomes the average, which is 6.

Why?\
Because:

-   Point at 10 pulls it right
-   Point at 2 pulls it left
-   It settles in the middle where pulls are balanced.

### Elbow Method

for simple graph we can easily decide the how many cluster it wil form but for complex and multi dimensional graph it becomes hard and confusion, therefor to find the number of cluster we use Elbow method

It is a way to find the best number of clusters (K) in K-Means.

Here we use iterative approach

-   K = 1
-   K = 2
-   K = 3
-   K = 4\
    … and so on

For each K, you calculate the sum of square within each cluster

Now when you plot the graph you'll get something like:

<img src="./images/elbow-method.png" style="width:600px">

Elbow Point:\
It is the place where improvement suddenly slows down and this is also the place where we get the best K value.

[Go To Top](#content)

---

# Hierarchal Clustering

Hierarchical Clustering is a clustering technique that builds clusters step-by-step in a tree-like structure called a dendrogram.

> A dendrogram is simply a tree-like diagram that shows how clusters were formed step-by-step in hierarchical clustering.

There are two ways to build the clusters:

1. Agglomerative (Bottom-Up)
2. Divisive (Top-Down)

### Agglomerative (Bottom-Up)

This is the most common one.

Start with each data point as its own cluster, then merge the closest clusters until everything becomes one big cluster.

#### Simple Illustration

Imagine you have 5 points:

```
A  B  C  D  E
```

Step 1: Start with each point as a separate cluster

```
{A} {B} {C} {D} {E}
```

Step 2: Find the two closest points and merge\
Suppose A & B are closest:

```
{AB} {C} {D} {E}
```

Step 3: Again merge closest clusters\
Suppose C & D are closest:

```
{AB} {CD} {E}
```

Step 4: Continue merging\
Suppose (AB) is closest to E:

```
{ABE} {CD}
```

Step 5: Finally

```
{ABCDE}
```

This entire merge history forms a tree structure → the dendrogram.

### To understand visually

How clustering happens

<img src="./images/hierarichal-clustring.png" style="width:600px">

how can we represent it using dendrogram

<img src="./images/hierarichal-clustring-1.png" style="width:600px">

### How to choose clusters

in Hierarchal clustering we get multiple set of the cluster but we yet didn't know which cluster to take in consideration

In Hierarchical Clustering, you decide the number of clusters by cutting the dendrogram at a certain height.

Wherever your line cuts the branches, the number of cuts = number of clusters.

<img src="./images/dendogams.png" style="width:600px">

**H1 2(clusters)**

-   cluster 1: 5, 8, 2
-   cluster 2: 6, 4, 1

**H2 (4 clusters)**

-   cluster 1: 5
-   cluster 2: 8, 2
-   cluster 3: 6
-   cluster 4: 4, 1

#### How to pick the BEST cut?

Look for a big vertical gap between merges.
That gap means two groups are very far apart, which is a natural separation.

<img src="./images/best-cut-1.png" style="width:600px">

in above example we can see that on Y axis the biggest gap is from 1.5 to 7.8, therefor we make cut somewhere around this gap

like this

<img src="./images/best-cut-2.png" style="width:600px">

[Go To Top](#content)

---

# Silhouette Score

it’s a measure used to evaluate how good your clusters are.

For each point, it compares:

-   a(i) = how close the point is to its own cluster (intra-cluster distance)
-   b(i) = how far the point is from the next nearest cluster (nearest-cluster distance)

<img src="./images/silhoutte.png" style="width:600px">

Then it computes:

$$s = \frac{b(i)-a(i)}{max(a(i),\ b(i))}$$

-   s ≈ +1 → well-clustered
-   s ≈ 0 → on the boundary
-   s ≈ −1 → probably in the wrong cluster

### Example

Imagine 2 clusters:

```
Cluster 1:  [1.0, 1.2, 0.9]
Cluster 2:  [7.0, 7.1, 6.9]
```

Take a point in Cluster 1, say 1.0:

-   Average distance to Cluster 1 points = a ≈ 0.15
-   Average distance to Cluster 2 points = b ≈ 6.0

Silhouette:

$$s = \frac{6.0 - 0.15}{6.0} ≈ 0.97$$

That’s almost perfect separation.

### How Silhouette Actually Works

For each point i, we measure two things:

1. **a(i) → “How well do I fit inside my cluster?”**

    - It’s the average distance to the other points in the same cluster.
    - Small a(i) = “I’m close to my cluster mates → I belong here.”
    - Large a(i) = “I’m far from my cluster mates → maybe I don’t belong.”

2. **b(i) → “How far am I from other clusters?”**
    - For each other cluster, compute the average distance from point i to that cluster.
    - The smallest of those averages is b(i).
    - So b(i) says: “What’s the closest alternative cluster I could join?”

#### What Silhouette Does With a(i) and b(i)

**Case 1: a(i) << b(i)**

The point is much closer to its own cluster than to the nearest other cluster.

-   Numerator (b - a) is positive
-   s(i) is close to +1

Great clustering:\
“I am close to my friends and far from strangers.”

<br/>

**Case 2: a(i) ≈ b(i)**

The point is on the border between its cluster and another.

-   Numerator is close to zero
-   s(i) ≈ 0

Borderline:\
“I could belong to either cluster.”

<br/>

**Case 3: a(i) >> b(i)**

The point is closer to another cluster than its own.

-   Numerator becomes negative
-   s(i) approaches –1

Bad clustering:\
“I am closer to outsiders than my own group.”

#### In short

Silhouette checks whether a point is closer to its own cluster than to any other cluster.\
If yes → good.\
If no → bad.

[Go To Top](#content)

---

# Dimensionality reduction

Dimensionality Reduction is a technique in machine learning used to reduce the number of input features while keeping as much important information as possible.

Dimensionality reduction is a technique or algorithm that belongs to the unsupervised learning category, because:

-   it learns structure from data without labels
-   it transforms features but does not produce target outputs

### Why do we need it?

Datasets often have:

-   Too many features (high-dimensional data)
-   Redundant or noisy information
-   Features that are combinations of others

This causes:

-   Slow training
-   Overfitting
-   Harder visualization

Dimensionality reduction solves these by compressing data into fewer useful features.

### What it does

Transforms high-dimension data → low-dimension data:

```yaml
Original: 100 features → Reduced: 10 features
```

But those 10 new features still capture the major patterns.

### Main goals

| Purpose             | Example                     |
| ------------------- | --------------------------- |
| Remove noise        | Drop useless features       |
| Reduce redundancy   | Combine correlated features |
| Improve performance | Faster, less overfitting    |
| Visualize data      | Convert 100D → 2D plot      |

### Two main approaches

| Approach               | Techniques                        | Idea                           |
| ---------------------- | --------------------------------- | ------------------------------ |
| **Feature Extraction** | PCA, Autoencoders, t-SNE, UMAP    | Create new compressed features |
| **Feature Selection**  | Filter, Wrapper, Embedded methods | Choose best original features  |

[Go To Top](#content)

---

# Curse of Dimensionality

The Curse of Dimensionality refers to the set of problems that arise when the number of features (dimensions) in a dataset becomes very large.

As dimensions increase:

-   Data becomes sparse (scattered far apart)
-   Distance-based models struggle
-   Computation cost rises sharply
-   Model overfits easily because it finds noise instead of real patterns

The Curse of Dimensionality describes how high-dimensional data becomes very spread out and difficult for many ML algorithms to learn from, leading to poor performance.

### Simple Example to Understand

Imagine spreading 10 data points:

-   On a 1D line → They are close to each other
-   On a 2D plane → More spread out
-   On a 3D cube → Even more spread
-   In 100 dimensions → They are extremely far apart
-   So the model cannot find meaningful similarity patterns.

### Why is it a "curse"?

Because increasing features doesn’t always help — instead, it can cause:
| Problem | Impact |
| ----------------- | --------------------------------- |
| Overfitting | Model memorizes noise |
| Sparsity | Hard to find neighbors / clusters |
| More resources | Time, memory, training cost |
| Hard to visualize | Humans can only see up to 3D |

### Different ways to remove curse of dimensionality

1. **Feature Selection:** \
   Choose a subset of the original features (nothing new created)
2. **Feature Extraction**\
   Create new features by transforming original ones

[Go To Top](#content)

---

# Feature selection

choosing only the most useful features (columns) from your dataset to train the model.

### Why do we need Feature Selection?

If a dataset has too many features:

-   Model becomes slower and more complex
-   Higher chance of overfitting
-   Some features may be irrelevant or duplicate
-   Harder to understand the model

So, feature selection helps to:\
✔ Improve accuracy\
✔ Reduce training time\
✔ Avoid overfitting\
✔ Make model simpler and explainable

### Simple Illustration

Suppose your dataset is for predicting house price:
| Feature | Useful? |
| ----------------------- | ------- |
| Area (sq ft) | ✔ |
| No. of Bedrooms | ✔ |
| Color of wall paint | ✘ |
| Distance to city center | ✔ |
| Owner's favorite food | ✘ |

You select only useful features:

-   Area
-   Bedrooms
-   Distance to city

And remove non-useful ones:

-   Color of wall paint
-   Owner’s favorite food

### How to Select the Right Features

When working with features, we check how they are related to each other:

-   If two features depend on each other (strong relationship) → Keep only one
-   If two features don’t depend on each other (weak or no relationship) → Keep both

This helps remove unnecessary (duplicate-like) features and improves model performance.

### How to Check the Relationship Between Features

There are 3 types of relationships:

#### 1. Positive relation

If one feature increases and the other also increases\
(Or one decreases and the other also decreases)

Example:

-   More experience → higher salary
-   Less height → less weight
    > Both move in the same direction

#### 2. Negative Relation

If one feature increases but the other decreases

Example

-   More damage to a product → lower price
    > Both move in opposite directions

#### 3. No relation

Changing one feature does not affect the other

Example:

-   A person’s weight does not decide their salary
    > No effect on each other

<img src="./images/correlation.png" style="width:600px">

### covariance

To check feature selection using covariance, we look at how strongly two features are related with each other.

#### Formula

$$Cov(X, Y) = \frac{1}{n-1}\sum(X_i - \bar{X})(Y_i - \bar{Y})$$

Where:

-   $X_i$ = each value in feature X
-   $Y_i$ = each value in feature Y
-   $\bar{X}$ = mean of feature X
-   $\bar{Y}$ = mean of feature Y
-   $n$ = how many data points you have for both $X$ and $Y$

> The “n−1” is used when estimating covariance from a sample

| Covariance Value    | Relationship          | Meaning for Feature Selection                               |
| ------------------- | --------------------- | ----------------------------------------------------------- |
| Positive            | positive relationship | Both increase together → dependent → remove one             |
| Negative            | negative relationship | One increases, other decreases → dependent → may remove one |
| Zero (or near zero) | No relationship       | Independent → keep both                                     |

### Correlation

Correlation tells how strongly two features are related and in what direction.

> It is basically normalized covariance — so we get a value between -1 and +1.

#### Formula

$$Correlation(X,Y) = \frac{Cov(X,Y)​}{\sigma{x} . \sigma{y}}$$

Where:

-   Cov(X, Y) → covariance of X and Y
-   σX → standard deviation of X
-   σY → standard deviation of Y

#### Correlation Value Range

| Correlation value | Relationship           | Meaning for Feature Selection                                   |
| ----------------- | ---------------------- | --------------------------------------------------------------- |
| **Close to +1**   | Strong positive        | Both increase together → **dependent** → remove one             |
| **Close to -1**   | Strong negative        | One increases, other decreases → **dependent** → may remove one |
| **Close to 0**    | No linear relationship | **Independent** → keep both                                     |

So, correlation helps us compare relationships even when features have different scales.

[Go To Top](#content)

---

# Feature Extraction

Feature Extraction = creating new useful features from the raw data.

### Simple Example

Suppose you have a dataset:
| Name | Birth Year | Current Year |
| ---- | ---------- | ------------ |
| A | 2000 | 2025 |
| B | 1998 | 2025 |

These columns are raw features.

Now we create a new feature:

Age = Current Year – Birth Year

| Name | Birth Year | Current Year | Age |
| ---- | ---------- | ------------ | --- |
| A    | 2000       | 2025         | 25  |
| B    | 1998       | 2025         | 27  |

This Age is an extracted feature — more useful for a model.

### How Feature Extraction does Dimensionality Reduction?

It combines multiple features into fewer new features.

Instead of removing columns (like in Feature Selection), Feature Extraction creates new compressed features.

#### Example

let say we have two features like:
| Feature1 | Feature2 |
| ---------- | ---------- |
| Height(cm) | Weight(kg) |

These two are related — both measure body size.

Instead, create 1 extracted feature:\
`BodySize = (Height + Weight) / 2`

Now:
| Extracted Feature |
| -------- |
|BodySize |

We reduced 2 dimensions → 1 dimension\
but still kept the information.

[Go To Top](#content)

---

# PCA (Principal Component Analysis)

PCA takes many related features and combines them into fewer useful ones.

> its a type of Feature extraction

PCA is a dimensionality reduction technique that:

-   finds the directions in data where the variance (spread) is highest
-   re-maps the data onto fewer new features called principal components
-   these components contain most of the important information

### Example:

let say you have data like:

<img src="./images/PCA-1.png" style="width:600px">

This is a 2 dimensional data, Therefor to make it 1 dimensional you project the datapoint on X axis

<img src="./images/PCA-2.png" style="width:600px">

now if you consider datapoint on x axis as a new feature you'll have a feature that is only depend on X axis i.e, 1D feature

### Loss of information

when you directly project the datapoint on the X axis you lost huge amount of information from Y axis

<img src="./images/PCA-3.png" style="width:600px">

as you can see on Y axis the datapoint are spread from 2 to 6

-   high spread -> high Variance -> high information
    > Variance measures how far each value in a dataset is from the mean (on average). It shows the spread or variability of data.

Although projecting datapoint directly onto the X axis change the dimensions from 2D to 1D we also loss some info from Y axis

if this loss is very huge then our model might not perform well

Therefor in PCA our goal is to minimize this information loss while making the data 1D

### Axis transformation

you simply transform/rotate your axis to minimize the information loss

<img src="./images/PCA-4.png" style="width:600px">

now if you project teh datapoint onto the new X axis you'll again convert the 2D data into 1D

<img src="./images/PCA-5.png" style="width:600px">

and now this time if you look at the information loss from new Y axis you'll get:

<img src="./images/PCA-6.png" style="width:600px">

as you can see the spread on new Y axis is very less compare to spread on original Y axis therefor we can say that:

-   low spread -> low Variance -> low information

hence we can conclude that projecting the datapoint onto the new X axis not only convert it to 1D from 2D it will also have low information loss

### Main aim in PCA

Therefor from above example we can say that our main aim in PCA is to find the new Axis such that we can project the datapoint onto them to convert 2D data into 1D with minimum information loss

each new axis that captures the features is what we called principle component (PC)

-   new X axis -> PC1
-   new Y axis -> PC2
-   new Z axis -> PC3\
     ... ect

> larger variance will be captured by CP1 then CP2 then CP3 and so on

to convert the 2D datapoint into 1D we have to find the best fit Principle component (PC)

to find the best fit PC we just have to look for the the variance alone that axis

-   if variance is maximum -> capture most of the info -> best fit PC -> called PC1
-   line that capture 2nd maximum variance -> capture most the info after PC1 -> called PC2

now our goal is to get the best PC which capture maximum variance

### Example

let say we have 3D datapoint:

-   for 3D datapoint we can have PC1, PC2, PC3
-   var(PC1) > var(PC2) > var(PC3)

for 3D -> 1D:\
we project all of the datapoint on to the PC1

for 3D -> 2D:\
we project all of the datapoint on to the PC1 and PC2

[Go To Top](#content)

---

# Math intuition behind the PAC Algorithm

### 1. how to find projection

to calculate the variance we need to find the projection of all datapoint on to that PC

$$Proj_p\ u = p . u$$

this formula says projection of point $p$ onto line $u$ is equal to dot product of $p$ and $u$

here:

-   $p$ = multi dimensional datapoint
-   $u$ = Principle component (PC)

#### why dot product?

Dot product gives how much of one vector lies in the direction of another vector.

**Geometric Explanation**\
For any two vectors a and b:

$$a . b = |a||b|cos\theta$$

Here:

-   a = datapoint
-   b = PC

<img src="./images/dot-product.jpg" style="width:600px">

in PCA we ALWAYS make each Principal Component a unit vector (length = 1).

Because Principal Components are used as new axes, and axes should have:

-   Length = 1 → unit vector
-   Be perpendicular to each other (orthogonal)
-   Represent direction only, not scale

Therefor:

-   as $|b| = 1$
-   output of dot product is $|a|cos\theta$

as dot product gives scalar value:\
once we find the projection of point $P_i$ onto the PC we get $P'_i$ which is our new lower dimensional datapoint

### 2. Compute variance

as we know how to calculate the projection we first calculate the projection of all datapoint then we calculate variance using formula:

$$Variance = \frac{1}{n}\sum(X_i - \bar{X})^2$$

where:

-   $X_i$ = datapoint i
-   $\bar{X}$ = mean of all datapoint
-   $n$ = total datapoint

> our goal is to find the best unit vector (PC) that capture ths maximum variance

#### Variance as a cost function

PCA uses variance as the cost function because more variance = more information, and PCA wants to keep the most information while reducing dimensions.

### 3. Eigen Value and Eigen Vector

how to use eigen value and eigen vector:

1. find covariance matrix between feature
2. eigen value and eigen vector will be found out from this covariance matrix
3. find the largest eigen value so that its respective eigen vector will capture maximum variance
    > eigen value = magnitude of eigen vector

#### How to find the covariance matrix

we know the fromula for covariance

$$Cov(X, Y) = \frac{1}{n-1}\sum(X_i - \bar{X})(Y_i - \bar{Y})$$

Where:

-   $X_i$ = each value in feature X
-   $Y_i$ = each value in feature Y
-   $\bar{X}$ = mean of feature X
-   $\bar{Y}$ = mean of feature Y
-   $n$ = how many data points you have for both $X$ and $Y$

> The “n−1” is used when estimating covariance from a sample

Now to compute the covariance matix:

$$
\text{Cov Matrix}(X,Y) =
\begin{bmatrix}
\text{Cov}(X,X) & \text{Cov}(X,Y) \\
\text{Cov}(Y,X) & \text{Cov}(Y,Y)
\end{bmatrix}
$$

> this is for 2 feature for 3 features will be having 3X3 matrix

For easy understanding:
| | X | y |
| -- | -- | -- |
| **X** | var(X) | cov(X, Y)|
| **Y** | cov(Y, X) | var(Y) |

**Note: cov(X, X) = var(X)**

### 4. Eigen-Decomposition

We solve:

$$Cv = \lambda v$$

Where:

-   $v$ = eigenvector
-   $\lambda$ = eigenvalue
-   $C$ = convariance matrix

> no. of eigen value = no. features in covariance matrix

#### Example on how to solve eigen decomposition

Example Matrix:

$$
A =
\begin{bmatrix}
4 & 2\\
2 & 4
\end{bmatrix}
$$

**1. Find Eigenvalues**

Solve:

$$|A - \lambda I| = 0$$

$$
\begin{bmatrix}
4 - \lambda & 2\\
2 & 4 - \lambda
\end{bmatrix} = 0
$$

Determinant:

$$(4−λ)(4−λ)−2⋅2=0$$

$$(4−λ)^2−4=0$$

$$(4−λ)^2=4$$

$$4−λ=±2$$

So:

$$λ_1​=6, \ \ \ λ_2​=2$$

**2. Find Eigenvectors**

Use each eigenvalue in:

$$(A−λI)v=0$$

for $\lambda_1$ = 6

$$\begin{bmatrix}
4 - 6 & 2\\
2 & 4 - 6
\end{bmatrix}=
\begin{bmatrix}
-2 & 2\\
2 & -2
\end{bmatrix}$$

let eigen vector $v$ be as follow:

$$
v =
\begin{bmatrix}
X\\
Y
\end{bmatrix}
$$

Therefor,

$$\begin{bmatrix}
-2 & 2\\
2 & -2
\end{bmatrix}
\begin{bmatrix}
X\\
Y
\end{bmatrix}=
\begin{bmatrix}
0\\
0
\end{bmatrix}$$

Solve:

$$−2X​+2Y​=0_{--------(i)}$$

$$2X​-2Y​=0_{--------(ii)}$$

by solving (i) and (ii) we get:

$$X = Y$$

Choose simplest numbers:

$$v_1=\begin{bmatrix}
1\\
1
\end{bmatrix}$$

> perform same steps for $\lambda_2$

### 5. Normalization

-   Eigenvectors are used as Principal Components (PCs) — they are directions in space.
-   A direction should only tell where to go, not how far to go.
-   So we scale every eigenvector to unit length (magnitude = 1).

#### What happens if we don’t normalize?

Then projection value:

$$Projection=x⋅eigenvector$$

would change wrongly depending on the eigenvector length.

#### How to normalization

Example vector:

$$v=[1, 1]$$

Its magnitude (length) is:

$$||v|| = \sqrt{1^2 + 1^2} = \sqrt{2}$$

To normalize, we divide each value by the magnitude:

$$v_{normalize} = \left[\frac{1}{\sqrt{2}},\ \ \frac{1}{\sqrt{2}}\right]$$

$$v_{normalize} = \frac{1}{\sqrt{2}}[1, 1]$$

Now check length:

$$\sqrt{\left(\frac{1}{\sqrt{2}} \right)^2 + \left(\frac{1}{\sqrt{2}} \right)^2} = \sqrt{\frac{1}{2} + \frac{1}{2}} = \sqrt{1} = 1$$

#### We use normalization to ensure:

-   Vector length = 1
-   Direction remains same

[Go To Top](#content)

---
