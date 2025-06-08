# Content
1. [introduction](#introduction)
2. [Population and Sample](#population-and-sample)
3. [Sampling Techniques](#sampling-techniques)
4. [Variable](#variable)
5. [Variable Measurement Scale](#variable-measurement-scale)


# Introduction
**Statistics** is a branch of mathematics that deals **with collecting, organizing, analyzing, interpreting, and presenting data.**

### What is data?
Data is the raw information that you **gather through observation, measurement, or research** — which is then used to do statistical analysis.

#### Example:
Let’s say you ask 5 people how many hours they sleep each night.

Their answers:
```
7, 6, 8, 5, 7
```
These numbers are **data**.\
You can now use **statistics** to find:
- The average sleep time
- The most common sleep time
- How spread out the values are

**Types of Data:**
| Type                          | Description                       | Example                      |
| ----------------------------- | --------------------------------- | ---------------------------- |
| **Qualitative (Categorical)** | Describes qualities or categories | Gender, Color, Type of food  |
| **Quantitative (Numerical)**  | Describes quantities or amounts   | Age, Height, Number of books |

**Quantitative is further divided into:**
- **Discrete**: Countable (e.g. number of siblings)
- **Continuous**: Measurable (e.g. weight, height)


### Two Main Types of Statistics:
| Type                       | Description                                | Example                                          |
| -------------------------- | ------------------------------------------ | ------------------------------------------------ |
| **Descriptive Statistics** | Summarizes data                            | Average height of students in a class            |
| **Inferential Statistics** | Makes predictions or conclusions from data | Predicting election results from a sample survey |

[Go To Top](#content)

---

# Population and Sample

### Population (N):
In statistics, a population is the entire group of people or items you want to study or get information about.

**Example:**\
All the students in your college.

### Sample (n):
A sample is a smaller part (subset) of the population that you actually collect data from.

Choosing a random sample is super important in statistics because it makes your results more fair, accurate, and trustworthy.

**Example:**\
You choose 50 random students from your college to survey.

#### Why use a sample?
Studying the entire population is often:

- Too big
- Too expensive
- Too time-consuming

So we study a sample and use it to make guesses (inferences) about the whole population.

#### Why Choose a Sample Randomly?
1. **Reduces Bias:**\
If you don’t choose randomly, you might pick only certain types of people (e.g., only your friends or only people who agree with you).
 Random selection ensures everyone has an equal chance, so the sample is not one-sided.

2. **Represents the Population:**\
A random sample is more likely to look like the whole population in terms of age, gender, background, etc. This means your conclusions apply to the whole population, not just the few you asked.

3. **Improves Accuracy:**\
Random samples tend to produce more accurate and reliable results — especially when the sample size is large enough.

 4. **Supports Valid Inference:**\
Statistical formulas (for confidence intervals, hypothesis testing, etc.) assume that your sample was random.
If it's not random, these methods might give wrong results.

### Example:
Your college has 2,000 students, and the management wants to know the average screen time of students per day.
| Term           | Example                                                      |
| -------------- | ------------------------------------------------------------ |
| **Population** | All **2,000 students** in your college                       |
| **Sample**     | A group of **100 students** chosen randomly from those 2,000 |

- You ask those 100 students how many hours they use their phone daily.
- You calculate the average screen time of those 100 students.
- Then, you use that result to estimate the average screen time of all 2,000 students.

### Simple Analogy:
Think of a big pot of soup (population).\
You taste one spoonful (sample) to know if it needs more salt.
If the spoonful is well mixed, it gives a good idea about the whole pot.


[Go To Top](#content)

---
# Sampling Techniques
**In statistics, sampling techniques are methods used to select a sample from a population.**

### Main Types of Sampling Techniques
Sampling techniques are divided into two categories:
| Category                        | Types                                          |
| ------------------------------- | ---------------------------------------------- |
| **1. Probability Sampling**     | Simple Random, Systematic, Stratified, Cluster |
| **2. Non-Probability Sampling** | Convenience, Judgmental, Snowball, Quota       |

## Probability Sampling
**Every member of the population has a known and equal chance of being selected.**
1. **Simple Random Sampling**
    - Every member is chosen purely by chance.
    - Like picking card from deck.
    - Example: Randomly selecting 50 students using a random number generator.

2. **Systematic Sampling**
    - Select every kᵗʰ person from a list after a random start.
    - Example: From a list of 1000 students, pick every 10th student (start at position 3 → 3, 13, 23, ...).

3. **Stratified Sampling**
    - Divide population into groups/strata (like gender or department), then randomly sample from each group.
    - Example: Divide students into "Engineering" and "Commerce", then take 20 random student from each.

4. **Cluster Sampling**
    - Divide population into clusters (groups), then randomly select entire clusters.
    - Example: Select 3 out of 10 classrooms randomly, and survey all students in those 3 classes.

## Non-Probability Sampling
**Not everyone has a guaranteed chance of being selected. It's not random.**

1. **Convenience Sampling**
    - Take samples from those easiest to reach.
    - Example: Asking your friends or students in your own class.


2. **Judgmental (Purposive) Sampling**
    - You choose who to ask based on who you think is best for the study.
    - Example: Asking only top scorers to get study tips.

3. **Snowball Sampling**
    - Existing participants refer others.
    - Example: Ask a person, they refer their friend, and so on.

4. **Quota Sampling**
    - Decide how many people you want from each group, then select non-randomly.
    - Example: You want 20 males and 20 females, so you take whoever is available until the quota is full.


[Go To Top](#content)

---
# Variable
**In statistics, a variable is any characteristic or value that can change from one individual or item to another.**

**In simple terms:**\
A variable is what you measure, observe, or record in a study.

####  Example:
If you're studying students:
| Variable | Example Values |
| -------- | -------------- |
| Age      | 18, 19, 20, 21 |
| Gender   | Male, Female   |
| Marks    | 75, 88, 92     |
| Height   | 5.5 ft, 6 ft   |

All of these are variables because they vary between students.

### Types of Variables
**Variables are mainly of two types:**

1.  **Quantitative (Numerical)**\
These represent numbers and you can do math on them.

    - **Discrete**: Countable\
Example: Number of siblings (0, 1, 2…)
    - **Continuous**: Measurable\
Example: Height, weight, temperature

2. **Qualitative (Categorical)**\
These represent categories or labels, not numbers.

    - **Example**:\
Gender (Male/Female)\
Blood type (A, B, AB, O)\
City name (Mumbai, Pune, Delhi)

### In Programming (like Java/C):
```java
int age = 20;           // Quantitative - Discrete
float height = 5.8f;    // Quantitative - Continuous
String gender = "Male"; // Qualitative
```

[Go To Top](#content)

---
# Variable Measurement Scale
**The measurement scale of a variable tells you how the data is classified, and what kind of analysis or operations you can do on it.**

## There are 4 Main Types of Measurement Scales:
| Scale        | Type         | Can You Do Math?        | Example                              |
| ------------ | ------------ | ----------------------- | ------------------------------------ |
| **Nominal**  | Qualitative  | ❌ No                    | Gender, Blood group, City name       |
| **Ordinal**  | Qualitative  | ❌ Only order matters    | Rank (1st, 2nd), Ratings (Good, Bad) |
| **Interval** | Quantitative | ✅ Yes, but no true zero | Temperature (°C), IQ score           |
| **Ratio**    | Quantitative | ✅ Yes, has true zero    | Age, Weight, Height, Salary          |


#### 1. Nominal Scale
- Data is divided into the different different category with no order or ranking. 
- You can't do any math with it.
- **Example**:
    - Gender: Male, Female
    - Blood Type: A, B, AB, O
    - Course: IT, CS, Mechanical

#### 2. Ordinal Scale
- Categories with a meaningful order or ranking.
- Example:
    - **Rank**: 1st, 2nd, 3rd
    - **Feedback**: Poor, Fair, Good, Excellent
You can say “Good is better than Fair” but not by how much.


#### 3. Interval Scale
- Numeric values with equal intervals but no true zero.
- You can add or subtract, but ratios don’t make sense.
- Example:
    - Temperature in °C or °F
    - Time of day (e.g., 3 PM, 6 PM)
    - Saying "30°C is twice as hot as 15°C" is meaningless.

#### 4. Ratio Scale
- Numeric, equal intervals, with a true zero.
- All math operations (+, −, ×, ÷) are meaningful.
- Example:
    - Height, Weight, Distance, Age, Salary
✔ 60 kg is twice as heavy as 30 kg


## Easy Memory Tip:

| Scale    | Think of it as... | Math?    | Zero? |
| -------- | ----------------- | -------- | ----- |
| Nominal  | Name              | ❌        | ❌     |
| Ordinal  | Order             | ➖        | ❌     |
| Interval | Number Line       | ➕ ➖      | ❌     |
| Ratio    | Full Math         | ➕ ➖ ✖️ ➗ | ✅     |



## Frequency Distribution

A frequency distribution shows how frequently each unique value (or interval) appears in a dataset.

#### Example:
Let’s say you surveyed 10 people on how many cups of tea they drink daily:
```
Data: 1, 2, 2, 3, 3, 3, 4, 4, 5, 5
```
| Cups of Tea (x) | Frequency (f) |
| --------------- | ------------- |
| 1               | 1             |
| 2               | 2             |
| 3               | 3             |
| 4               | 2             |
| 5               | 2             |


### Types:
1. **Ungrouped Frequency Distribution**\
Used for discrete data (individual values).

Example:
```
Marks:    10  20  30  40  
Frequency: 2   5   3   1
```
2. **Grouped Frequency Distribution**\
Used for continuous data (values in ranges).

Example:
```
Range (Marks) | Frequency
0 - 10        |     2
11 - 20       |     5
21 - 30       |     3
```

[Go To Top](#content)

---