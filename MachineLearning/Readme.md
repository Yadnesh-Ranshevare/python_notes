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


---

# AI vs ML vs DL vs DS

### 1. Artificial Intelligence (AI)
**Definition:**\
AI is the broad field that focuses on making machines think and act like humans — reasoning, learning, and decision-making.

**Goal**: Create systems that can perform tasks requiring human intelligence (e.g., speech, vision, planning).

**Example:**
- Siri or Alexa understanding your voice and responding.
- Self-driving cars making driving decisions.

### 2. Machine Learning (ML)
**Definition:**\
ML is a subset of AI that teaches computers to learn from data without being explicitly programmed.

**Goal**: Make predictions or decisions using data patterns.

**Example:**
- Netflix recommending movies based on your watch history.
- Spam filter learning what emails are spam.


### 3. Data Science (DS)
**Definition:**\
Data Science focuses on collecting, cleaning, analyzing, and visualizing data to extract insights and help in decision-making.

**Goal**: Turn raw data into useful information and models.

**Example:**
- Analyzing user data to find which products sell best.
- Visualizing COVID-19 trends using graphs.
> Data Science often uses AI/ML techniques to draw conclusions from data.

### 4. Deep Learning (DL)
**Definition:**\
DL is a subset of Machine Learning that uses neural networks with many layers to learn complex patterns — similar to how the human brain works.


**Goal**: Handle large and complex data (like images, audio, or natural language).

**Example:**
- Face recognition in phones.
- ChatGPT (it uses deep learning models).

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
- The model learns from labeled data — meaning both input and correct output are known.
- **Goal:** Predict outcomes for new, unseen data.
- **Example:** If you have a dataset of house prices with features like area, location, and price — the model learns the pattern and predicts price for a new house.

**Types:**
| Type               | Description                | Example Algorithms                           |
| ------------------ | -------------------------- | -------------------------------------------- |
| **Regression**     | Predicts continuous values | Linear Regression, Decision Tree Regressor   |
| **Classification** | Predicts discrete labels   | Logistic Regression, Random Forest, SVM, KNN |

> Input and Output variable are also know as dependent and independent variables
>
> **Independent variable** -> inputs\
> **Dependent variable** -> output


### 2. Unsupervised Learning
- The model learns from unlabeled data — only inputs, no known outputs.
- **Goal:** Discover groups, similarities, or patterns without knowing the output.
- **Example:** Grouping customers with similar buying behavior (Clustering).

**Types:**
| Type            | Description                           | Example Algorithms                       |
| --------------- | ------------------------------------- | ---------------------------------------- |
| **Clustering**  | Groups similar data points            | K-Means, Hierarchical Clustering, DBSCAN |
| **Dimensionality Reduction** | Reducing dataset features while preserving key information. | PCA (Principal Component Analysis),                            |


### 3. Semi-Supervised Learning
- Uses a mix of labeled and unlabeled data — labeled data helps guide learning for unlabeled data.
- **Goal:** Improve accuracy when labeling all data is expensive or time-consuming.
- **Example:** Email spam detection — a few emails are labeled as spam or not, rest are learned automatically.
- Algorithms:
    - Self-training models
    - Graph-based models
    - Semi-supervised SVM
### 4. Reinforcement Learning (RL)

- The model learns by interacting with an environment and receiving rewards or penalties for actions.
- **Goal:** Learn the best sequence of actions to maximize rewards.
- **Example:**
    - A robot learning to walk.
    - A game-playing AI (like AlphaGo) improving with each match.
- **Algorithms:**
    - Q-Learning
    - Deep Q-Network (DQN)
    - SARSA
    - Policy Gradient Methods

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
| 1000         | 40                 |
| 1200         | 50                 |
| 1500         | 65                 |
| 1800         | 80                 |

You want to predict the price of a house that’s 1600 sq ft.

**How it works:**
1. Input (X) = Area of house
2. Output (Y) = Price of house
3. The regression algorithm tries to find a line (or curve) that best fits all data points.

This line can be represented as: `Y = mX + c`

**Where:**
- Y → Predicted value (price)
- X → Input feature (area)
- m → Slope (how much price changes per sq ft)
- c → Intercept (base price)

<img src="./images/regration_example.png" style="width:600px">

from this graph we can predict the housing price for 1600 sq ft.
- for above graph calculated slope is `m = 0.04`
- Therefor, `Price = 0.04 * Area + 0`
- `Price = 0.04 * 1600` = `₹64 lakhs`



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
| Email text                     | Label    |
| ------------------------------ | -------- |
| “You won a lottery!”           | Spam     |
| “Meeting at 10 AM”             | Not Spam |
| “Get rich fast!”               | Spam     |
| “Your project is due tomorrow” | Not Spam |

The algorithm learns the patterns:
- Words like “lottery”, “win”, “offer” → Spam
- Words like “meeting”, “project” → Not spam

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
| A        | 18  | 80             |
| B        | 22  | 75             |
| C        | 45  | 30             |
| D        | 48  | 25             |
| E        | 28  | 85             |
| F        | 50  | 20             |

You don’t know who’s which type of customer,

but clustering algorithms can group them like:
- **Cluster 1**: Young customers who spend more (A, B, E)
- **Cluster 2**: Older customers who spend less (C, D, F)

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
| Features    | Description       |
| ----------- | ----------------- |
| Marks       | Exam score        |
| Attendance  | Percentage        |
| Sleep Hours | Daily sleep       |
| Study Hours | Daily study       |
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
- 🐱 Cats
- 🐶 Dogs

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
- Group 1 → furry, small = 🐱 cats
- Group 2 → long ears = 🐶 dogs
- Group 3 → feathers = 🐦 birds

The model discovers the groups itself — you didn’t tell it what’s what.

### Think like this:
| Question                               | Classification               | Clustering                           |
| -------------------------------------- | ---------------------------- | ------------------------------------ |
| Do we know the answer before training? | ✅ Yes                        | ❌ No                                 |
| What does the model do?                | Learns to label data         | Finds hidden groups                  |
| Example                                | “Is this email spam or not?” | “Group similar emails automatically” |


### Final comparison
| Feature                   | **Clustering**                                   | **Classification**                                             |
| ------------------------- | ------------------------------------------------ | -------------------------------------------------------------- |
| **Type**                  | **Unsupervised Learning**                        | **Supervised Learning**                                        |
| **Labeled Data?**         | ❌ No labels — the algorithm finds its own groups | ✅ Has labels — the model learns from them                      |
| **Goal**                  | Find hidden **groups or patterns**               | Predict **predefined categories**                              |
| **Output**                | Unknown clusters (e.g., Group 1, Group 2...)     | Known labels (e.g., Cat, Dog, Human)                           |
| **Training Data Example** | Just features like Age, Income                   | Features + Labels (e.g., Age, Income → “Buyer” or “Non-Buyer”) |
| **Evaluation**            | Harder — no true answers                         | Easier — compare predicted vs actual labels                    |
| **Example Algorithms**    | K-Means, DBSCAN, Hierarchical                    | Decision Tree, Random Forest, SVM, Logistic Regression         |
| **Common Use Cases**      | Customer segmentation, pattern discovery         | Spam detection, disease prediction                             |



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
- You have a bunch of points (data).
- Linear regression tries to draw one line that’s as close as possible to all those points.
- That line helps you:
    - Understand the trend → e.g., as area increases, price increases.
    -  Predict new values → if I know area = 1600, what will be the price?

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
- $h_\Theta (x)$ → predicted value (hypothesis function)
- $\Theta_0$ → intercept (bias term)
- $\Theta_1$ → weight/slope parameter
- $x$ → input feature (independent variable) 

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
| 50               | 48                  | 2             |
| 60               | 65                  | -5            |
| 70               | 68                  | 2             |

Here, the errors are small, but we want to measure the total error to see how far off we are.

### Mean Squared Error (MSE)
In [Linear Regression](#liner-regression), the most common cost function is Mean Squared Error:

$$J(m,c) = \frac{1}{n}\sum(Y_i - \bar{Y_i})^2$$

Where:
- $Y_i$ → Actual value
- $\bar{Y_i}$ → Predicted value
- $n$ → Number of data points
- $J(m,c)$ → Cost (depends on slope m and intercept c)

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

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$| Actual Output $(y_i)$
---| --- | ---
1|1 |1
2|2 | 2
3|3 |3

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-1)^2 + (2-2)^2 + (3-3)^2] = 0$  

<img src="./images/cost_1.png" style="width:600px">

#### For $\Theta_1 = 0.5$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$| Actual Output $(y_i)$
---| --- | ---
1|0.5 |1
2|1 | 2
3|1.5 |3

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0.5)^2 + (2-1)^2 + (3-1.5)^2] ≈ 0.58$ 

<img src="./images/cost_2.png" style="width:600px">

#### For $\Theta_1 = 0$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$| Actual Output $(y_i)$
---| --- | ---
1|0 |1
2|0 | 2
3|0 |3

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
- $h_\Theta (x)$ → predicted value (hypothesis function)
- $\Theta_0$ → intercept (bias term)
- $\Theta_1$ → weight/slope parameter
- $x$ → input feature (independent variable) 


lets assume $\Theta_0 = 0$ 

Therefor our equation becomes:

$$h_\Theta (x) =  \Theta_1 (x)$$


#### For $\Theta_1 = 1$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$| Actual Output $(y_i)$
---| --- | ---
1|1 |1
2|2 | 2
3|3 |3

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-1)^2 + (2-2)^2 + (3-3)^2] = 0$  



#### For $\Theta_1 = 0.5$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$| Actual Output $(y_i)$
---| --- | ---
1|0.5 |1
2|1 | 2
3|1.5 |3

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0.5)^2 + (2-1)^2 + (3-1.5)^2] ≈ 1.17$  

#### For $\Theta_1 = 0$

| input $(x_i)$ | predicted Output $h_\Theta(x_i)$| Actual Output $(y_i)$
---| --- | ---
1|0 |1
2|0 | 2
3|0 |3

cost function = $J(\Theta_1) = \frac{1}{n}\sum(Y_i - h_\Theta(x_i))^2 = \frac{1}{3}[(1-0)^2 + (2-0)^2 + (3-0)^2] ≈ 4.67$  

#### Similarly when you calculated $J(\Theta_1)$ other values of $\Theta_1$ you'll get following data
|  Θ₁  | Predictions (hΘ(x)) | Errors (y - hΘ(x)) | Sum of squared errors   | J(Θ₁) = 1/3 * SSE |
| :--: | :------------------ | :----------------- | :---------------------- | :---------------: |
|   0  | [0, 0, 0]           | [1, 2, 3]          | 1² + 2² + 3² = 14       |      **4.67**     |
|  0.5 | [0.5, 1, 1.5]       | [0.5, 1, 1.5]      | 0.25 + 1 + 2.25 = 3.5   |      **1.17**     |
|   1  | [1, 2, 3]           | [0, 0, 0]          | 0                       |       **0**       |
|  1.5 | [1.5, 3, 4.5]       | [-0.5, -1, -1.5]   | 0.25 + 1 + 2.25 = 3.5   |      **1.17**     |
|   2  | [2, 4, 6]           | [-1, -2, -3]       | 1 + 4 + 9 = 14          |      **4.67**     |
| -0.5 | [-0.5, -1, -1.5]    | [1.5, 3, 4.5]      | 2.25 + 9 + 20.25 = 31.5 |      **10.5**     |


Now if you plot the graph using this data then you get:

<img src="./images/cost_fun_grapn.png" style="width:600px">

- When we draw the cost function (J) against the model parameter (like θ₁), we get a U-shaped curve.
- The lowest point on this curve (for example, at θ₁ = 1) shows where the error is smallest.
- Since the error is smallest there, that θ₁ value gives the best possible line that fits our data.

> The bottom of the curve = minimum error = best fit line.

### Minima
- The lowest point in gradient decent is called minima
- When we talk about minima in Gradient Descent (i.e., the points where cost function is low), there are a few types

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
- When we maximize something (like accuracy or profit), we look for the highest point on a curve instead of the lowest.
- It’s the opposite of minima.

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
- When we train a model (like using Gradient Descent), we keep updating parameters (θ) step by step to reduce error (Cost Function J).
- The process keeps going until the error stops changing much — that point is called Convergence.

### Equation
$$
\Theta_j = \Theta_j - \alpha \frac{\partial J(\Theta)}{\partial \Theta_j}
$$


- this equation is the heart of gradient descent, and it’s used for one simple reason: \
to reduce the error (cost function) step by step until it reaches the minimum.

- we use this equation because it tells how to update our parameters (θ values) so that our model learns and the error decreases.

| Part                                             | Meaning                                              | Purpose                                                              |
| ------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------------- |
| $\frac{\partial J(\Theta)}{\partial \Theta_j}$ | The **slope** of cost function (direction of change) | Tells whether we need to go **left or right** to reduce error        |
| $\alpha$                                      | Learning rate                                        | Controls **how big the step** should be                              |
| ( - ) (minus sign)                               | Move in **opposite direction** of slope              | Because slope shows **increasing error**, we want to **decrease it** |
| $\Theta_j$                                     | Model parameter                                      | Gets updated each iteration to get closer to best value              |


### Why we need 𝛼 (learning rate)
Think of gradient descent like walking downhill to reach the lowest point (global minima).
- The gradient (slope) tells you which direction to move.
- But it doesn’t tell you how far to move in that direction. That’s where α comes in — it controls the step size.

| α (learning rate) | What happens                                                                             
| ----------------- | ---------------------------------------------------------------------------------------- | 
| **Too large**     | You take huge steps — might **jump over** the minimum or even **oscillate** forever.     | 
| **Too small**     | You take tiny steps — you **move very slowly**, might take forever to reach the minimum. | 
| **Just right**    | You smoothly go downhill and reach the **global minimum** quickly.                       | 

![Image](./images/leaarning_rate.png)



### Type of slope
The slope tells us how steep a line or curve is and which direction it’s going.

#### Positive Slope
- The line or curve is going upward as you move right.
- It means the value of $J(\Theta)$ (cost) increases when you increase $\Theta$
- So, to reduce cost, you should go left (decrease $\Theta$)

#### Negative Slope
- The line or curve is going downward as you move right.
- It means $J(\Theta)$ decreases when $\Theta$ increases.
- So, to reduce cost even more, you should go right (increase $\Theta$)

#### Example
<img src="./images/slope_positive_negative.svg" style="width:600px">



#### In short
| Slope Type         | Curve Direction          | What It Means                           | Move Which Way To Reduce Cost? |
| ------------------ | ------------------------ | --------------------------------------- | --------------- |
| **Positive (+ve)** | Goes up as θ increases   | You’re on the left side of the minimum  | Move **left**   |
| **Negative (−ve)** | Goes down as θ increases | You’re on the right side of the minimum | Move **right**  |



### How it helps find the minima
1. **Find the slope (gradient)**
    - The slope tells you which way the hill is tilted.
    -   If the slope is positive → the hill goes up to the right.
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
- Initial $\Theta = 4$
- Learning rate $\alpha = 0.1$

Now, update step by step
| Step | Old $\Theta $ | Derivative (2Θ) | New $ \Theta = \Theta - \alpha(2Θ) $ |
| ---- | -------------- | --------------- | ------------------------------------ |
| 1    | 4.0            | 8               | 4 - 0.1×8 = **3.2**                  |
| 2    | 3.2            | 6.4             | 3.2 - 0.1×6.4 = **2.56**             |
| 3    | 2.56           | 5.12            | 2.56 - 0.1×5.12 = **2.048**          |
| 4    | 2.048          | 4.096           | 2.048 - 0.1×4.096 = **1.638**        |

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
- $h_0(x^i)$ -> predicted value 
- $y^i$  -> actual value
- $n$ → Number of data points

### Compute derivative

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_j} = \frac{\partial }{\partial \Theta_j}[\frac{1}{n} \sum(h_0(x^i) - y^i)^2]$$


> $\frac{\partial x^2}{\partial x} = 2x$
>
>similaly
>
>$\frac{\partial \sum (x^2)}{\partial x} = 2\sum(x)$


For j = 1

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_1} = \frac{\partial }{\partial \Theta_1}[\frac{1}{n} \sum(h_0(x^i) - y^i)^2]$$

from general hypothesis equation we know that


$$h_\Theta (x^i) = \Theta_0 + \Theta_1 (x^i)$$

$$\frac{\partial h_\theta(x^i)}{\partial \Theta_1} = x^i$$

Therefor, we multiply this $x^i$ in our final equation

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_1} = \frac{2}{n} \sum(h_0(x^i) - y^i)(x^i)$$

For j = 0

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_0} = \frac{\partial }{\partial \Theta_0}[\frac{1}{n} \sum(h_0(x^i) - y^i)^2]$$

from general hypothesis equation we know that


$$h_\Theta (x^i) = \Theta_0 + \Theta_1 (x^i)$$

$$\frac{\partial h_\theta(x^i)}{\partial \Theta_1} = \Theta_0$$

Therefor, we doesn't multiply anything in our final equation

$$\frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_0} = \frac{2}{n} \sum(h_0(x^i) - y^i)$$

### Put this values in convergence equation

original equation


$$
\Theta_j = \Theta_j - \alpha \frac{\partial J(\Theta_0, \Theta_1)}{\partial \Theta_j}
$$

for $\Theta_0$

$$\Theta_0 = \Theta_0 - \alpha[\frac{2}{n} \sum(h_0(x^i) - y^i)]$$


for $\Theta_1$

$$\Theta_1 = \Theta_1 - \alpha[\frac{2}{n} \sum(h_0(x^i) - y^i)(x^i)]$$


### These equations tell us:

- How to update both parameters (θ₀ and θ₁) step by step so that the prediction error (cost) keeps decreasing
- These two equations work together to slowly adjust the line so that it fits the data points perfectly — i.e., they find the minimum cost through gradient descent.

#### for $\Theta_0$

$$\Theta_0 = \Theta_0 - \alpha[\frac{2}{n} \sum(h_0(x^i) - y^i)]$$

- It updates the intercept of the line.
- It shifts the line up or down to reduce overall error.
- The term $(h_0(x^i) - y^i)$ shows how far predictions are from real values.

So:\
If predictions are too high → θ₀ decreases (moves line down)\
If predictions are too low → θ₀ increases (moves line up)


#### for $\Theta_1$

$$\Theta_1 = \Theta_1 - \alpha[\frac{2}{n} \sum(h_0(x^i) - y^i)(x^i)]$$

- It updates the slope of the line.
- It controls how tilted the line is.
- The extra $(x^i)$ term helps the model learn how much each feature (x) affects the output.

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

- How accurate is it?
- How much error is it making?
- Is it predicting too high or too low?

### Common Performance Metrics


1. For Regression Problems

| Metric                        | Formula                                | Meaning                                                    |   
| ----------------------------- | -------------------------------------- | ---------------------------------------------------------- |
| **MSE** (Mean Squared Error)  | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | Average of squared errors. Penalizes big errors.           |                                                           
| **RMSE** (Root MSE)           | $\sqrt{MSE}$                         | Easier to interpret (same units as output).                |            
| **MAE** (Mean Absolute Error) | $\frac{1}{n}\sum y_i - \hat{y}_i$                      | Average of absolute differences. Less harsh on outliers.         |  
| [**R² Score**](#score)                  | $1 - \frac{SS_{res}}{SS_{tot}}$      | How much of data variance is explained by the model (0–1). |                                                           


2. For Classification Problems

| Metric               | Meaning                                              |
| -------------------- | ---------------------------------------------------- |
| **Accuracy**         | How many predictions are correct overall.            |
| **Precision**        | Of all predicted “positives”, how many were correct. |
| **Recall**           | Of all actual “positives”, how many did we find.     |
| **F1 Score**         | Balance between Precision and Recall.                |
| **Confusion Matrix** | Table showing True/False Positive/Negative counts.   |


[Go To Top](#content)

---
# $R^2$ Score
It tells how well your regression line fits the data

### Formula

$$R^2 = 1-\frac{SS_{res}}{SS_{tot}}$$


Where:
- $SS_{res} = \sum(y_i - \hat y_i)^2$ 
- $SS_{tot} = \sum(y_i - \bar y)^2$ 

Here also:

- $\hat y_i$ → value predicted by your model for input $x_i$ (represent best fit line)
- $\bar y$ → average of all actual outputs in your dataset (represent average fit line)
- $y_i$ → actual datapoint

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

- When You Add a Useful (Relevant) Feature:

    - That feature actually helps your model predict better.
    - So:
        - Prediction error decreases
        - Cost function J(Θ) decreases
        - R² increases

- When You Add an Unnecessary (Irrelevant) Feature:
    - That feature doesn’t help prediction (maybe just random noise).
    - Then:
        - R² still increases slightly (mathematically, it never decreases)
        > Because R² measures how much variation your model explains compared to a flat mean line. Even if you add noise, the model can “fit” that noise a little, making the R² look better — but not actually better.
- Conclusion:\
Adding Irrelevant new feature increases the $R^2$ value for no reason, deceiving the computer to think model with irrelevant feature is the better model cause it has high $R^2$ value


### Why R² increases when we add more input variables

R² tells us how well our model fits the data.

When you add more inputs (even random ones), the model gets more flexibility to “bend” and fit the data a bit better — so the total error slightly decreases,

So:
- “More flexibility to bend” → model adjusts more to match the data
- “Total error decreases” → predictions become slightly closer to the real values
- But sometimes, it starts matching noise (random variations), not real patterns

That’s why R² goes up — because it only checks if prediction error got smaller,
not if it’s meaningful.

<img src="./images/R_squre_adding_input.png" style="width:800px">

## Adjusted R²
- Adjusted R² is an improved version of R² that checks if the new features you add really help your model or not.
- If a new feature doesn’t make predictions better, it reduces the score instead of increasing it.

#### Why do we need it?

Problem with normal R²:\
R² always increases when you add more features —
even if those features are useless!

That can make you think your model got better, but it actually just got more complex, not more accurate.

#### Adjusted R² fixes this
- It adjusts R² based on how many predictors (features) you have.
- If you add a new feature that doesn’t improve the model,
- Adjusted R² will decrease — telling you it was unnecessary.

#### Formula

$$\text{Adjusted $R^2$} = 1 - [\frac{(1-R^2)(n-1)}{n-p-1}]$$

Where:
- $n$ = number of data points
- $p$ = number of features (independent variables) also called predictor
- $R^2$ = normal R² score

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
- This is the data the model learns from.
- The model adjusts its parameters (like slope and intercept in linear regression) by minimizing error on this data.
- Think of it like studying for an exam — this is your practice material.


### 2. Testing Data
- This data is not shown to the model during training.
- It is used after training to check how well the model can generalize — i.e., predict unseen data.
- Think of it like your final exam — you test how well you actually learned.

### When a model “fits” the training data…
We look at two types of errors:
1. Training error → how well the model fits the data it has seen i.e training data
2. Testing error → how well the model predicts data it hasn’t seen i.e testing data

The balance between these two tells us whether the model is:

- good (generalizes well)
- overfitting
- underfitting

### Underfitting → “Didn’t learn enough”
| Data              | What Happens                                            |
| ----------------- | ------------------------------------------------------- |
| **Training Data** | Model performs poorly — can’t capture the pattern.      |
| **Testing Data**  | Also performs poorly — since it never learned properly. |

Example:
| Dataset  | Error  |
| -------- | ------ |
| Training | High ❌ |
| Testing  | High ❌ |

Model didn’t learn the pattern → underfit.

<img src="./images/underfit.png" style="width:700px">


### Overfitting → “Learned too much (memorized)”
| Data              | What Happens                                      |
| ----------------- | ------------------------------------------------- |
| **Training Data** | Model performs *extremely well* (memorized data). |
| **Testing Data**  | Performs *poorly* — fails on unseen data.         |

Example:
| Dataset  | Error      |
| -------- | ---------- |
| Training | Very Low ✅ |
| Testing  | High ❌     |

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


[Go To Top](#content)

---


