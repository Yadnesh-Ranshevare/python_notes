# Content
1. [AI vs ML vs DL vs DS](#ai-vs-ml-vs-dl-vs-ds)
2. [Type of ML Algorithm](#type-of-ml-algorithm)
3. [Regression and Classification](#regression-and-classification)


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

### 2. Unsupervised Learning
- The model learns from unlabeled data — it finds hidden patterns or structures on its own.
- **Goal:** Discover groups, similarities, or patterns without knowing the output.
- **Example:** Grouping customers with similar buying behavior (Clustering).

**Types:**
| Type            | Description                           | Example Algorithms                       |
| --------------- | ------------------------------------- | ---------------------------------------- |
| **Clustering**  | Groups similar data points            | K-Means, Hierarchical Clustering, DBSCAN |
| **Association** | Finds relationships between variables | Apriori, Eclat                           |


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

![Image](./images/regration_example.png)

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