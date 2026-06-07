<h3 style="text-align: center;">RNN - Recurrent Neural Network </h3>

---

# Content
1. [Introduction](#introduction)
2. [Why to use RNN over ANN](#why-to-use-rnn-over-ann)
3. [Zero Padding Problem](#zero-padding)
4. [[timestep, input_feature]](#timestep-input_feature)
5. [Architecture](#architecture)

---
# Introduction
RNN (Recurrent Neural Network) is a type of neural network designed to process sequential data, where the order of inputs matters.

Sequential data is data where order matters. The meaning of the data changes if you shuffle it. Each element depends on its position in a sequence and/or previous elements.

### Example of Sequential data

1. **Text (language)**
    
    - Sentence: `“I love AI”`
    - If you shuffle it: `“AI love I”` → meaning breaks completely

2. **Time series data**

    - Example: stock price over days

        | Day | Price |
        | --- | ----- |
        | 1   | 100   |
        | 2   | 105   |
        | 3   | 102   |
    - Order matters because tomorrow depends on today.

3. **Audio / Speech**

    - Sound is a wave over time.
    - If you reorder audio samples, you don’t get speech anymore—you get noise.

4. **Video**

    - Video = sequence of frames.
    - Frame 1 → Frame 2 → Frame 3
    - Changing order breaks motion logic.


### Memory in RNN via Hidden State

RNNs have a concept of “memory” through a hidden state. This hidden state is a vector that carries information from previous time steps to the current step.

At each step, the model updates this hidden state using the current input and the previous hidden state. Because of this, earlier information in the sequence influences later outputs.

Example sentence: `“I love AI”`
1. Input: `“I”`\
    → model processes it\
    → creates hidden state (context so far)
2. Input: `“love”`\
→ uses “love” + previous hidden state (“I” context)

3. Input: `“AI”`\
→ uses “AI” + updated hidden state (“I love” context)

Note: this is not true memory like storing facts. It is a compressed representation of past information, and older details can get weaker as the sequence becomes longer.


[Go To Top](#content)

---

# Why to use RNN over ANN

the problem of ANN is that it only accept the fixed size input

lets supposes you have three sentence:

- "Hey my name is abc"
- "I love AI"
- "India won the match"

now we vectorize this sentence using one hot encoding

- there are total 12 different word in  those three sentence
- we separate out each word to perform one hot encoding to compute the input vector for that respective word
    - "hey" = $[1, 0, 0, ..., 0]_{1\times12}$
    - "my" = $[0, 1, 0, ..., 0]_{1\times12}$
    - "name" = $[0, 0, 1, ..., 0]_{1\times12}$
    - "match" = $[0, 0, 0, ..., 1]_{1\times12}$
- now sentence "Hey my name is abc" can be represented as:

|Word| Hey | my | name | is | abc |
|---|--- | --- | --- | --- | --- |
|**input vectors**| $[1, 0, 0, ..., 0]_{1\times12}$| $[0, 1, 0, ..., 0]_{1\times12}$| $[0, 0, 1, ..., 0]_{1\times12}$|$[0, 0, 0, 1 ..., 0]_{1\times12}$ | $[0, 0, 0, 0, 1..., 0]_{1\times12}$|
- similarly we can do for other two sentence as well
- Also understand that:\
number of words per sentence = number of input vectors for that sentence
- each input vector provide n input variable where n is size of the input vector

once the vectorization is done we feed the table to an ANN to predict an output

but the problem is:
- sentence 1 = "Hey my name is abc" = 5 words = 5 input vectors = 60 (5 x 12) input variable
- sentence 2 = "I love AI" = 3 words = 3 input vectors = 36 (3 x 12) input variables
- sentence 3 = "India won the match" = 4 words = 4 input vectors = 48 (4 x 12) input variable

This creates the problem as ANN only accept the fixed number input variables but with sequential data we didn't have  fixed number of input





[Go To Top](#content)

---

# Zero Padding
to solve this dynamic input size problem with sequential data we can use the zero padding method

lets suppose input vectors of:
- sentence a (3 words) = [1, 0, 0, 0, 0] [0, 1, 0, 0, 0] [0, 0, 1, 0, 0]
- sentence b (1 words) = [0, 0, 0, 1, 0]
- sentence c (2 words) =  [0, 0, 0, 1, 0] [0, 1, 0, 0, 0] 

as sentence a is biggest here with 3 input vectors, our ANN will need at least 3 input node to process them

whereas sentence b has only one input vector, but we have 3 input node in our ANN

therefore we provide this single input vector as a input to any of the input node while other two accepts 0 vector as a input

zero vector = vector having all zero init and having same size as that of other input vector

as zero vector will have all zero present inside it will not contribute in prediction at all, and is only present to solve that dynamic input size problem 



Example:

- sentence a
    ```
    input vector = v1, v2, v3

    input to ANN = v1, v2, v3
    ```

- sentence b
    ```
    input vector = v1

    input to ANN = v1, 0v, 0v
    ```

- sentence a
    ```
    input vector = v1, v2

    input to ANN = v1, v2, 0v
    ```

### Problem?

lets suppose we have large dataset of text having approximately 10,000 unique word throughout the dataset

then our single input vector (using one hot encoding) will be like:

$$[1, 0, 0, ...., 0]_{1\times10,000}$$

as you can see the size of input vector is 10,000

lets suppose the largest sentence inside the dataset is of 10 words, suggesting that there will be 10 input nodes

therefore number of input variable will be: 10,000 x 10 = 1,00,000

lets suppose you have smallest sentence is of 4 words and on an average there are only 6-7 words per sentence

now:
- for smallest word we have 6 zero vector of size 1x10,000\
number of input variable not contributing due to zero vector = 6 x 10,000 = 60,000
- for average size sentence we have 4-3 zero vector of size 1x10,000\
number of input variable not contributing due to zero vector = (3 to 4) x 10,000 = 30,000 - 40,000

this numbers are too high for any dataset, around 30% - 40% input variable are 0 in average case whereas in worst case 60% input variable are 0

also having zero as a input variable stops the model form learning. as gradient depends on this input variable and having zero as a input makes the gradient zero as well

- Gradient w.r.t weights:

$$\frac{\partial L}{\partial w} = x \times \frac{\partial L}{\partial z}$$

- But since x = 0:

$$\frac{\partial L}{\partial w} = 0$$

- now according to gradient decent:

$$w_{new} = w_{old}- \alpha  \frac{\partial L}{\partial w}$$

$$w_{new} = w_{old}$$


Meaning:
- No weight update comes from padded positions
- Model literally learns nothing from them
- So padding = dead zones for learning


Mathematically those zeros don’t contribute at all but:
- they still go through matrix multiplications
- still consume compute and memory bandwidth
- as a result we waste computation

so in our case we have around 30% - 60% of zero input variable which indicate high dead zones for learning and hugh unnessery computational cost

### Problem 2

all the above analysis works in a ideal case where we are assuming all the input text are equal to or less than that of largest sentence present inside the dataset used for training

but at the time of testing we might encounter a bigger sentence that that of training time

| dataset | larges sentence |
| --- | --- |
|training | 10 words |
| testing | 15 words |

As during training we have largest sentence with 10 words there must be 10 input vector in our model, even with the zero padding we can only accept at max 10 input vector

but in the testing we have a word with 15 words i.e, 15 input vectors and our model can only take 10 input vector 

> in production a user might pass even larger word on which we have no control 




[Go To Top](#content)

---
# [timestep, input_feature]

It describes the shape (structure) of input data for an RNN.

### 1. Timestep = “how many steps in the sequence”

This is the length of the sequence.

Example:

- Sentence: “I love AI”
- Timesteps = 3 (I → love → AI)

### 2. Input_feature = “what each step contains”
This is the size of each input at one timestep.

> It is NOT “number of words”.

It is the vector representation of each word.

Example:\
Each word is converted into numbers (embedding):

- “I” → [0.2, 0.8, 0.1]
- “love” → [0.5, 0.9, 0.3]
- “AI” → [0.7, 0.4, 0.6]

Here:
- input_feature = 3 (because each word is a 3D vector)

### Example 

consider a dataset:

| no. | text|
|--- | ---|
|1. | `movie` `was` `good`|
|2. | movie was `not` good | 

as we have 4 unique in our dataset (movie, was, good, not) our vocabulary size of 4

we can use one hot encoding to convert each word into their respective vector representation

word | vector representation
--- |---
movie | [1, 0, 0, 0]
was | [0, 1, 0, 0]
good | [0, 0, 1, 0]
not | [0, 0, 0, 1]

now as each vector is of 4 size `input_feature = 4`

Therefore

| no. | text| vector form | length / timestep  | [timestep, input_feature] |
|--- | ---| --- | --- | --- |
|1. | `movie` `was` `good`| [[1, 0, 0, 0]  [0, 1, 0, 0] [0, 0, 1, 0]] | 3 | [3, 4]
|2. | movie was `not` good | [[1, 0, 0, 0] [0, 1, 0, 0] [0, 0, 0, 1] [0, 0, 1, 0]] | 4 | [4, 4]


> you can think of [timestep, input_feature] as dimension of vector form of that respective sentence

so for sentence `movie was good` we provide a array of size 3x4 into our model to process



[Go To Top](#content)

---
# Architecture

in ANN whatever input we provide it flows only in forward direction to provide an output

```
input layer -> hidden layer -> output layer
```

but in RNN the output of each hidden layer is pass again into that hidden layer for future computation 

<img src="./Images/RNN.png" style="width:500px">



### Example

consider a simple network:

```
input layer → single hidden layer → output layer
```

sentence `movie was good`

so when we pass this sentence inside a model,  it process each word at a time i.e, 
- for t = 1 → `movie`
- for t = 2 → `was`
- for t = 3 → `good`

whenever we process any word we use output of hidden layer from previous timestamp in current timestamp

> i.e, using hidden layer output at t = 1 as a input for hidden layer when t = 2

input = `movie`
```
"movie" vector → input layer → hidden layer → hidden layer output for word "movie"
```
input = `was`
```
                    hidden layer output for word "movie"
                                 ↓
"was" vector → input layer → hidden layer → hidden layer output for word "was"                  
```
input = `good`
```
                        hidden layer output for word "was" 
                                 ↓
"good" vector → input layer → hidden layer → output layer → output
```

<img src="./Images/RNN-architecture.png" style="width:500px">

in above image you can see how exactly the output of hidden layer from previous timestamp is passed as input into the hidden layer of current timestamp

for t = 1 (first pass) we provide a default input (all 0 or random values) in place of previous hidden layer output


for t = 1 → input = `movie`
```
                          random values / all 0
                                   ↓
"movie" vector → input layer → hidden layer → hidden layer output for word "movie"
```
The Actual flow

```
                   default      "was" vector     "good" vector 
                      ↓                ↓            ↓
"movie" vector → hidden layer → hidden layer → hidden layer → output
```

so you can think of it as a loop that accept the initial word compute the output, loop back to accept the second word and again compute the output with second word and output of previous iteration, and repeat until all the words from a sentence gets completed

<img src="./Images/RNN-flow.png" style="width:500px">

[Go To Top](#content)

---