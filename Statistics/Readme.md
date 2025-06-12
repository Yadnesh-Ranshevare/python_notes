# Content
1. [introduction](#introduction)
2. [Population and Sample](#population-and-sample)
3. [Sampling Techniques](#sampling-techniques)
4. [Variable](#variable)
5. [Variable Measurement Scale](#variable-measurement-scale)
6. [Study of Data Using Graph](#study-of-data-using-graph)
7. [Central Measure of Tendency](#central-measure-of-tendency)
    - [Mean](#mean)
    - [Outlier](#outlier)
    - [Median](#median)
    - [Mode](#mode)
    - [Comparison Between Mean, Median, and Mode](#comparison-between-mean-median-and-mode)
8. [Measure of Dispersion](#measure-of-dispersion)
    - [Range](#range)
    - [Variance](#variance)
    - [Standard Deviation](#standard-deviation)
    - [Standard Deviation Graph](#standard-deviation-graph)
    - [Quartile](#quartile)
    - [Interquartile Range (IQR)](#interquartile-range-iqr)
9. [Percentile](#percentile)
10. [Five Number Summary](#five-number-summary)
    - [Box Plot](#box-plot)
    - [Detecting and Removing outlier](#detecting-and-removing-outlier)


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
### Cumulative Frequency
Cumulative frequency is the running total of frequencies up to a certain value or class in a frequency distribution.

Suppose this is your frequency table:
| Marks Range | Frequency |
| ----------- | --------- |
| 0 - 10      | 3         |
| 11 - 20     | 5         |
| 21 - 30     | 7         |
| 31 - 40     | 4         |

Now let’s add cumulative frequency:
| Marks Range | Frequency | Cumulative Frequency |
| ----------- | --------- | -------------------- |
| 0 - 10      | 3         | 3                    |
| 11 - 20     | 5         | 3 + 5 = 8            |
| 21 - 30     | 7         | 8 + 7 = 15           |
| 31 - 40     | 4         | 15 + 4 = 19          |


[Go To Top](#content)

---

# Study of Data Using Graph
**Studying data using graphs in data science helps you visually understand patterns, trends, and outliers.**


## 1. Bar Graph (Column-based comparison)
- **Use it when:** You want to compare categories like favorite sport of students
- it is generally use for Discrete variables

**Example:**
| type of sport  | number of student  |
| ------ | ----- |
| Golf  | 6    |
| Tennis | 8     |
| Football  | 12     |
| Rugby  | 10     |
| Basketball  | 16     |

![Bar chart](./Images/Bar-Graph-Chart.jpg)

**from this graph we can easily say that `Golf` is the `least` favorite sport whereas `Basketball` is `most` favorite**


## 2. histogram
- **Use it when:** You want to see how values are spread like age
- it is generally use for Continues variables
- **Bin**: In data science, a bin is a range or interval used to group continuous values in a histogram.

**Example:**\
consider a following dataset of age of peoples 

```
age = {22, 26, 31, 35, 37, 39, 40, 43, 46, 48, 51, 53, 54, 55, 57, 66, 68, 69, 75, 92}
```
**From above table we get the frequency table**
Bin(age) | number of people
--- | --- 
0 - 10 | 0
10 - 20 | 0
20 - 30 | 2
30 - 40 | 4
40 - 50 | 4
50 - 60 | 5
60 - 70 | 3
70 - 80 | 1
80 - 90 | 0
90 - 100 | 1

![Histogram image](./Images/histogram.png)

## 3. Line Graph
- **Use it when:** You want to see how something changes over time (like daily temperature).
- it is generally use for Continues variables

**Example:**

![Line char Image](./Images/Line-Graph-05-min.png)



## 4. Pie Chart (Percentage of total)
**Use it when:** You want to show parts small data with respect to bigdata (e.g., vote share, budget spending).

**Example:**

![Pie chart image](./Images/pie1.png)


from the above pie chart we can say that toys has total sales of `14%`




[Go To Top](#content)

---
# Central Measure of Tendency

Central Measure of Tendency (or just Measures of Central Tendency) are statistical values that represent the **center of distribution of data**

**They help answer:**\
📌 "What is the average or middle value of this data?"


### There are 3 main types:
| Measure    | Symbol             | Meaning                          | Use Case Example              |
| ---------- | ------------------ | -------------------------------- | ----------------------------- |
| [**Mean**](#mean)   | $\bar{x}$ or $\mu$ | Average of all values            | Average marks of students     |
| [**Median**](#median) | —                  | Middle value when data is sorted | Middle income of a population |
| [**Mode**](#mode)   | —                  | Most frequently occurring value  | Most sold product             |



## Mean
The arithmetic mean is the sum of all values divided by the number of values.

#### Formula:

$$
Mean = \frac{Sum of all values
​} {Number of values}
$$


###  1. Population Mean (μ)
Used when you're dealing with the entire group (like all students in a school).

#### Formula:

$$
\mu = \frac{\sum_{}^{} X_i}{\text{N}}
$$

Where:

- **𝜇**: Population mean  
- **∑𝑋ᵢ**: Sum of all data points in the population  
- **N**: Total number of data points in the population


#### Example:
Heights of all 5 students: 150, 160, 170, 180, 190
$$
μ = \frac{150 + 160 + 170 + 180 + 190}{5} = \frac{850}{5} = 170
$$

###  2. Sample Mean (x̄)
Used when you take a subset (sample) from the population.

#### Formula:

$$
\bar{x} = \frac{\sum_{}^{} X_i}{\text{n}}
$$


Where:

- **x̄**: sample mean  
- **∑𝑋ᵢ**: Sum of all data points in the sample  
- **n**: Total number of data points in the sample

#### Example:
Heights of a sample of 3 students: 150, 170, 190

$$
\bar{x} = \frac{150 + 170 + 190}{3} = \frac{510}{3} = 170
$$

#### Key Difference

| Aspect      | Population Mean (μ) | Sample Mean (x̄) |
| ----------- | ------------------- | ---------------- |
| Use case    | Whole group         | Subset of group  |
| Notation    | $\mu$               | $\bar{x}$        |
| Size symbol | $N$                 | $n$              |


## outlier
- An outlier is a data point that is significantly different from the other values in a dataset — it either lies much higher or much lower than the rest.

**Example:**\
Data:\
`10, 12, 11, 13, 500`\
🔍 Here, `500` is an outlier because it’s far away from the other values.
 

 - An outlier can pull the mean toward itself, especially if the dataset is small.


#### How outlier affect mean
**Example:**\
Data without outlier:\
`10, 12, 14, 16, 18`

**Mean = (10 + 12 + 14 + 16 + 18) / 5 = 70 / 5 = `14`**

Now add an outlier → 100:\
`10, 12, 14, 16, 18, 100`

**Mean = (10 + 12 + 14 + 16 + 18 + 100) / 6 = 170 / 6 ≈ `28.3`**

👉 The mean jumped from **14 to 28.3** — just because of one outlier!


## Median
Median is the middle value of a sorted dataset.

#### Steps to Find the Median:
1. Sort the data
2. Use these rules:
    - If odd number of values:\
👉 Median = middle value

    - If even number of values:\
👉 Median = average of two middle values


**Example 1: Odd number of elements**

Data:\
`[5, 1, 3]` → sort it → `[1, 3, 5]`\
👉 Median = `3`


 **Example 2: Even number of elements**

Data:\
`[6, 2, 4, 8]` → sort → `[2, 4, 6, 8]`\
👉 Median = (4 + 6) / 2 = `5`

#### Median is not affected by outlier

**Example:**\
data\
`10, 12, 14, 16, 18, 100`\
outlier → 100:

**Mean = (10 + 12 + 14 + 16 + 18 + 100) / 6 = 170 / 6 ≈ `28.3`**\
**Median = (14 + 16) = `15`**

out of `28.3` and `15` median `15` is more realistic 


## Mode
Mode is the value that appears the most number of times in a dataset.
It tells you the most frequent or popular value. especially used for categorical or non-numeric data.


#### Example:
**Data:**\
`[2, 4, 4, 6, 7, 4, 8]`\
👉 Mode = 4 (because it appears 3 times)

####  Other Possibilities:
| Type of Mode   | Example              | Explanation                   |
| -------------- | -------------------- | ----------------------------- |
| **No Mode**    | `[1, 2, 3, 4]`       | All values occur only once    |
| **Unimodal**   | `[3, 3, 5, 6]`       | One mode (3)                  |
| **Bimodal**    | `[2, 2, 5, 5, 7]`    | Two modes (2 and 5)           |
| **Multimodal** | `[1, 1, 2, 2, 3, 3]` | More than two values repeated |

#### Where is Mode Useful?
| Situation                      | Why Mode Helps                          |
| ------------------------------ | --------------------------------------- |
| Most bought product            | Shows customer preference               |
| Most common exam score         | Shows what most students scored         |
| Categorical data (e.g. colors) | Mean/median doesn’t make sense for text |

#### Does an outlier affect the mode?
It depends on whether the outlier is frequent or not.

1. **Usually, outliers do NOT affect mode**\
Because mode depends on frequency, not size.\
**Example:**\
Data: `[2, 2, 3, 4, 100]`
    - Mode = 2
    - 100 is an outlier (appears once) → ❌ No effect on mode

2. **BUT — if the outlier repeats more than others, it can become the mode.**\
**Example:**\
Data: `[1, 2, 3, 4, 5, 100, 100]`

    - 100 appears twice, more than any other\
✅ Mode = 100\
🎯 Outlier became the mode


## Comparison Between Mean, Median, and Mode
| Feature                      | **Mean**                                 | **Median**                                   | **Mode**                            |
| ---------------------------- | ---------------------------------------- | -------------------------------------------- | ----------------------------------- |
| **Definition**               | Average of all values                    | Middle value in sorted data                  | Most frequently occurring value     |
| **Formula**                  | $\text{Sum of values} \div \text{Count}$ | Middle of sorted list (or avg of two middle) | Value that appears most often       |
| **Affected by Outliers**     | ✅ Yes                                    | ❌ No                                         | ❌ No                                |
| **Data Type**                | Numerical only                           | Numerical only                               | Numerical & Categorical             |
| **Use Case**                 | Balanced data                            | Skewed data or with outliers                 | Categorical or repeated values      |
| **Example (2, 3, 3, 6, 10)** | Mean = 4.8                               | Median = 3                                   | Mode = 3                            |
| **Uniqueness**               | One unique value                         | One unique value                             | Can be none, one, or multiple modes |
| **Common In**                | Grades, salary average                   | Real estate prices, age data                 | Survey results, product popularity  |


[Go To Top](#content)

---
# Measure of Dispersion
A Measure of **Dispersion** tells you how **spread** out or **scattered** the values in a dataset are.

It shows how much the data spread from the center (mean/median) — basically, how consistent or variable the data is.

### Common Measures of Dispersion:
| Measure                       | What it tells you                       |
| ----------------------------- | --------------------------------------- |
| [**Range**](#range)                     | Difference between max and min values   |
| [**Variance**](#variance)                  | Average squared deviation from the mean |
| [**Standard Deviation**](#standard-deviation)        | Square root of variance (most used)     |
| [**Interquartile Range (IQR)**](#interquartile-range-iqr) | Spread of the middle 50% of data        |

---
## Range
Range is the simplest measure of dispersion — it tells you how spread out the data is by calculating the difference between the highest and lowest values.

#### Formula:

$$
\text{Range} = \text{Maximum Value} - \text{Minimum Value}
$$

#### Example:
Data: `[4, 7, 9, 15, 20]`

- Max = 20
- Min = 4\
👉 Range = 20 - 4 = 16

#### Key Points
- Easy to calculate	
- Affected by outliers	
- Useful for quick overview	as it give basic spread
- only looks at two values (max and min), so it ignores the rest of the dataset.

---
## Variance
Variance measures how far each value in a dataset is from the mean (on average).
It shows the spread or variability of data.

#### Formula:

- For Population Variance ($\sigma^2$)

$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
$$

- For Sample Variance ($s^2$)

$$
s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

**Where:**
- $x_i$ :  each data point
- $\mu$ : population mean
- $\bar{x}$ : sample mean
- $N$ : population size
- $n$ : sample size


#### The reason why population variance uses N, but sample variance uses n − 1, comes down to accuracy and unbiased estimation.

 **Population Variance:**
- You have all data points from the population.
- So, you know the true mean 𝜇
- μ, and can calculate exact spread.
- Use divisor **N** (the total number of values).

**Sample Variance:**
- You only have a subset of the population.
- You don’t know the true mean 𝜇, so you estimate it using sample mean $\bar{x}$
- That estimation introduces a small error, which tends to underestimate the real variance.
- To correct that underestimation, we divide by n − 1 instead of n.\
→ This correction is called Bessel's correction.



#### Example:
Data: `[2, 4, 6, 8]`\
Mean = (2 + 4 + 6 + 8) / 4 = `5`

| Data $x_i$ | Mean $\bar{x} = 5$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
| ---------- | ------------------ | --------------- | ------------------- |
| 2          | 5                  | 2 − 5 = **−3**  | (−3)² = **9**       |
| 4          | 5                  | 4 − 5 = **−1**  | (−1)² = **1**       |
| 6          | 5                  | 6 − 5 = **+1**  | (+1)² = **1**       |
| 8          | 5                  | 8 − 5 = **+3**  | (+3)² = **9**       |

- $\sum{}{}(x_i - \bar{x})$ = 9 + 1 + 1 + 9 = `20`
- Number of values (n) = 4

**For Population Variance:**

$$
\sigma^2 = \frac{20}{4} = 5
$$

**For Sample Variance:**

$$
s^2 = \frac{20}{4 - 1} = \frac{20}{3} ≈ 6.67
$$

---
## Standard Deviation
Standard Deviation (SD) measures how spread out the values in a dataset are from the mean.
It tells you how much the data varies on average.

It’s the square root of the variance — this brings the unit back to the original scale of your data (unlike variance, which is squared).

#### Formula:

 **For Population:**

 $$
 \sigma = \sqrt{\frac{1}{N}\sum{}{}(x_i - \mu)^2} = \sqrt{Population Variance (\sigma^2)}
 $$

**For Sample:**

 $$
 \sigma = \sqrt{\frac{1}{n-1}\sum{}{}(x_i - \bar{x})^2} = \sqrt{Sample Variance (s^2)}
 $$


 Data: `[2, 4, 6, 8]`\
Mean = (2 + 4 + 6 + 8) / 4 = `5`

| Data $x_i$ | Mean $\bar{x} = 5$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
| ---------- | ------------------ | --------------- | ------------------- |
| 2          | 5                  | 2 − 5 = **−3**  | (−3)² = **9**       |
| 4          | 5                  | 4 − 5 = **−1**  | (−1)² = **1**       |
| 6          | 5                  | 6 − 5 = **+1**  | (+1)² = **1**       |
| 8          | 5                  | 8 − 5 = **+3**  | (+3)² = **9**       |

- $\sum{}{}(x_i - \bar{x})$ = 9 + 1 + 1 + 9 = `20`
- Number of values (n) = 4

**For Population:**

$$
Variance(\sigma^2) = \frac{20}{4} = 5
$$

$$
\text{Standard Deviation}(\sigma) = \sqrt{5} ≈ 2.24
$$

**For Sample:**

$$
Variance(s^2) = \frac{20}{4 - 1} = \frac{20}{3} ≈ 6.67
$$

$$
\text{Standard Deviation}(s) = \sqrt{6.67} ≈ 2.58
$$

---
## Standard Deviation Graph
lets assume a dataset whose mean is `50` and standard deviation is `10`
- Draw X-axis (horizontal) → represents the data values, how to create the x-axis
    - Mean = 50 and SD = 10
    - Mean $\pm$ SD = 40, 60
    - 40 - SD = 30 and 60 + SD = 70 
    - 30 - SD = 20 and 70 + SD = 80 
    - therefor mark points: 20, 30, 40, 50, 60, 70, 80  
- Draw Y-axis (vertical) → represents frequency or probability
- if you connect the all point then you'll find the smooth curve like:


![SD graph image](./Images/SD.jpg)

here:
- 50 : Standard deviation 
    - μ = 50
- 60 : 1st SD to the right of mean
    - μ + 1σ = 60
- 70 : 2nd SD to the right of mean
    - μ + 2σ = 70
- 80 : 3rd SD to the right of mean
    - μ + 3σ = 80
- 40 : 1st SD to the left of mean
    - μ − 1σ = 40
- 30 : 2nd SD to the left of mean
    - μ − 2σ = 30

- 20 : 3rd SD to the left of mean
    - μ − 3σ = 20

**Also:**
- first SD : 40 to 60
- second SD : 30 to 70
- third SD : 20 to 80

with this graph we can say that how far the value is from the mean

**Example:**\
data value 65 is 1.5 SD to the left -> $\mu$ + $1.5\sigma$ = 65 


### Also larger the curve of the graph higher the SD and smaller the curve of the graph lower the SD

![SD_high_low_image](./Images/SD_high_lowjpg.jpg)


- Higher the SD higher the value spread from mean, whereas lower the SD lower the value spread form mean

---

## Quartile
A quartile is a three statistical value that divides a dataset into four equal parts. These help describe the spread and distribution of data.

####  The 3 Quartiles are:
1. **Q1 (First Quartile)**
    - 25% of the data is less than or equal to Q1
    - It’s the median of the lower half of the data

2. **Q2 (Second Quartile)**
    - This is just the median of the entire dataset (50% mark)
3. **Q3 (Third Quartile)**
    - 75% of the data is less than or equal to Q3
    - It’s the median of the upper half of the data


#### Example:
Data: ` 2, 4, 6, 8, 10, 12, 14, 16, 18`

- Q2 (Median) = 10
- Lower half = 2, 4, 6, 8 → Q1 = (4 + 6)/2 = 5
- Upper half = 12, 14, 16, 18 → Q3 = (14 + 16)/2 = 15

✅ **So:**
- Q1 = 5
- Q2 = 10
- Q3 = 15

#### how to divide the dataset into the four equal parts
- part 1 : 0 to Q1
- part 2 : Q1 to Q2
- part 3 : Q2 to Q3
- part 4 : Q3 to last value

**Example:**\
Data: ` 2, 4, 6, 8, 10, 12, 14, 16, 18`

where:
- Q1 = 5
- Q2 = 10
- Q3 = 15

**ThereFor**\
- part 1 : `2, 4` (only 2, 4 lies in the range of 0 to Q1)
- part 2 : `6, 8, 10` (only 6, 8, 10 lies in range Q1 to Q2)
- part 3 : `12, 14` (only 12, 14 lies in the range of Q2 to Q3)
- part 4 : `16, 18` (only 16, 18 is beyond the Q3)

**Note: Values equal to Q1, Q2, or Q3 can belong to any side depending on convention**

## Interquartile Range (IQR)
IQR is a measure of dispersion that tells you how spread out the middle 50% of your data is.
It’s useful for removing the influence of outliers.

#### Formula:
$$
IRQ = Q_3 - Q_1
$$

**Where:**
- $Q_3$ = 1st quartile (25% of data below it)
- $Q_1$ = 3rd quartile (75% of data below it)

So IQR = the range between the 25th and 75th percentile.

#### Example:
Let’s take the data:\
`[5, 7, 8, 10, 12, 14, 18, 20, 22]`

1. **Sort the data**\
`[5, 7, 8, 10, 12, 14, 18, 20, 22]`

2. Find the Median (Q2)
- Total values = 9 (odd number)
- Middle value = 5th value → 12\
So,
$$Q_2 = Median = 12
$$
3. **Find Q1 (Lower Quartile)**\
Take the lower half of data, before the median: `[5, 7, 8, 10]`
    - This has 4 values → Median of this group = average of 2nd and 3rd value:
    $$
    Q_1 = \frac{7 + 8}{2} = 7.5
    $$
4. **Find Q3 (Upper Quartile)**\
Take the upper half of data, after the median:` [14, 18, 20, 22]`
    - Again, 4 values → Median = average of 2nd and 3rd:
    $$
    Q_3 = \frac{18 + 20}{2} = 19
    $$

5. **Final Answer:**

| Quartile | Value               |
| -------- | ------------------- |
| Q1       | 7.5                 |
| Q3       | 19                  |
| IQR      | 19 − 7.5 = **11.5** |



[Go To Top](#content)

---

# Percentile

A percentile is a value below which a given percentage of data falls.

It helps you understand the relative standing of a value in a dataset

**Simple Meaning:**
- The 25th percentile means 25% of the data is below that value.
- The 90th percentile means you're higher than 90% of the data.
- The 50th percentile is the median (middle value).


#### Example:
dataset: `2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9, 9, 10, 11, 11, 12`\
find the percentile of `10`

**Formula**

$$
\text{percentile of X} = \left({\frac{\text{number of value below X}}{\text{total number of value}}}\right) \times 100
$$

Therefor:\
percentile of 10 = $\left(\frac{16}{20}\right) \times 100$ = 80%ile

- we can say that 80% of the entire distribution is less than `10`

#### what is the value present at 25 percentile

**Formula:**


$$
Value = \left(\frac{percentile}{100}\right) \times (n + 1)
$$

ThereFor:\
value = $\frac{25}{100} \times 21$ = 5.25

- 5.25 is the index of value in our dataset
- there is no any index 5.25 in our dataset
- in our dataset we have nearest (5.25 will lie in between 5 & 6) index as:\
 index 5 = 5\
 index 6 = 5
- to find the value present at index 5.25 we take the mean of this two values  

Therefor, value = `5`






[Go To Top](#content)

---

# Five Number Summary
The Five Number Summary is a simple way to describe a set of data using five specific values that show the spread and center of the data.

before you learn about 5 number summary you must also know about the [quartile](#quartile)

#### The 5 numbers are:
1. **Minimum** – the smallest value
2. **Q1 (First Quartile)** – the median of the lower half (25% of data below it or you can say value at 25%ile)
3. **Median (Q2)** – the middle value of the dataset
4. **Q3 (Third Quartile)** – the median of the upper half (75% of data below it or you can say value at 75%ile)
5. **Maximum** – the largest value

#### Example
Consider this sorted dataset:\
`5, 7, 8, 10, 12, 14, 18, 20, 22`

- **Minimum** = 5
- **Q1** = 8 (middle of 5, 7, 8, 10)
- **Median (Q2)** = 12
- **Q3** = 20 (middle of 14, 18, 20, 22)
- **Maximum** = 22

**So the 5-number summary is:**\
`[5, 8, 12, 20, 22]`

## Box Plot
A box plot (also called a box-and-whisker plot) is a graphical representation of the Five Number Summary

![Box plot image](./Images/boxplotsimple.png)

Box plot diagram is use to tell how data is spread in dataset:
- higher the box length -> higher the data spread
- shorter the box length -> lesser the data spread
- max -> how far is maximum value 
- min -> how far is minimum value 



## Detecting and Removing outlier
[Click here to learn about outlier](#outlier)

- to remove outlier we calculate the lower fence and higher fence with the help of [Interquartile Range (IQR)](#interquartile-range-iqr)
- Interquartile Range (IQR) = Q3 - Q1
- formula for lower fence

$$
\text{Lower Fence} = Q1 - 1.5(IQR) 
$$

- formula for higher fence

$$
\text{Lower Fence} = Q3 + 1.5(IQR) 
$$

- Now any value which doesn't lie between the range of lower fence to higher fence will consider as outlier


#### Example:
data : `1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 27`

- Q1 = value at 25%ile = $(\frac{25}{100}) \times (19 + 1)$ = $(\frac{25}{100}) \times (20)$ = 5 -> index = `3` 
- Q3 = value at 75%ile = $(\frac{75}{100}) \times (19 + 1)$ = $(\frac{75}{100}) \times (20)$ = 15 -> index = `7`
- **Interquartile Range (IQR)** = Q3 - Q1 = 7 - 3 = `4`
- lower fence = Q1 - 1.5(IQR) = 3 - 1.5(4) = 3 - 6 = `-3`
- higher fence = Q3 + 1.5(IQR) = 7 + 1.5(4) = 7 + 6 = `13`
- Therefor our range is:\
`-3 to 13`
- in our dataset only one value which doesn't lie int this range i.e, `27`, therefor `27` is an outlier
- therefor after removing that outlier our final data becomes:\
`1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9`


[Go To Top](#content)

---
# Distribution
In statistics, a distribution tells us how data values are spread out — or how frequently each value (or range of values) occurs in a dataset.


## 1. Gaussian / Normal Distribution

 Make sure that you know about the [Standard deviation graph](#standard-deviation-graph)

![Normal distribution graph](./Images/ND.png)

- Empirical formula: its just a formula of 68.2 - 95.4 - 99.7 rate 
- this formula says
    1. 68.2% of data lie under the curve  $-1\sigma$  to $1\sigma$ i.e, first SD
    1. 95.4% of data lie under the curve $-2\sigma$  to $2\sigma$ i.e second SD
    1. 99.7% of data lie under the curve $-3\sigma$  to $3\sigma$ i.e third SD

#### Z score

A Z-score (also called a standard score) tells you how far a data point is from the mean, in terms of standard deviations.

**Example:**

consider a SD graph with mean = 50

![SD graph](./Images/SD.jpg)

from this graph we can say that point `60` will lie on to the `1 SD` to the right of mean ( $\mu + 1\sigma$ = 60 )

but what if you want to find the point `57` and where it fall. we cannot directly find that point on the graph, therefor to find this point we use Z score

**Formula:**

$$
Z = \frac{X - \mu}{\sigma}
$$

where:
- $X$ : your data point
- $\mu$ : mean of the dataset
- $\sigma$ : standard deviation

Therefor from this formula we can find the position of `57`

$$
z = \frac{57 - 50}{10} = 0.7
$$

This means you point lie at `0.7 SD` to the right pf the mean ( $\mu + 0.7\sigma$ = 57 )


**Note: if value of `Z` is `negative` that means point ile in `left` side of the graph, whereas if value of `Z` is `positive` then point lie in `right` side of the graph**

### Standardization

- currently our normal distribution are: `[20, 30, 40, 50, 60, 70, 80]` with `50 = mean` and `SD = 10`
- apply Z score over this list
    1. Z = (20 - 40) / 10 = -3
    1. Z = (30 - 40) / 10 = -2
    1. Z = (40 - 40) / 10 = -1
    1. Z = (50 - 40) / 10 = -0
    1. Z = (60 - 40) / 10 = 1
    1. Z = (70 - 40) / 10 = 2
    1. Z = (80 - 40) / 10 = 3
- therefor our new list becomes: `[-3, -2, -1, 0, 1, 2, 3]`
- from above example we can see that for any normal distribution like `[20, 30, 40, 50, 60, 70, 80]` if we apply the Z score then we get another distribution `[-3, -2, -1, 0, 1, 2, 3]` where `mean = 0` and `SD = 1`
- This new distribution (`[-3, -2, -1, 0, 1, 2, 3]`) is known as **standard normal distribution** and the process of converting normal distribution to standard normal distribution is called **standardization**

### How to use Z score to find the value?

you have given a graph of SAT score with `mean = 1150` and `SD = 150` find the probability of score being more than `1380`

**Solution:**\
for `1380`:

$
Z = \frac{X - \mu}{\sigma} = \frac{1380 - 1150}{150} = 1.53
$

![Graph](./Images/standard-normal-shaded-area-example.webp)

- now to find the probability of score being more than `1380` we have to find the area of graph where `z > 1.53`

- considering the area of whole graph is `1`, therefor we can say that area of graph where `z > 1.53` is: `P(z > 1.53) = 1 - (area of graph from -3 to 1.53)`

- to find the area of graph between -3 to 1.53 we use Z-score table

- from the table we get `area = 0.9370`

- Therefor the area of graph for `Z > 1.53` = `1 - 0.9370` = `0.063`
- hence we can say that probability of marks being more than `1380` is `6.3%`


[Go To Top](#content)

---




