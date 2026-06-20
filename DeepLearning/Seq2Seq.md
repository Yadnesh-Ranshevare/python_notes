# Content
1. [Introduction](#introduction)
2. [Encoder Decoder](#encoder-decoder)
3. [How To Train Encoder Decoder Model](#how-to-train-encoder-decoder-model)
4. [Problem with Encoder Decoder Architecture](#problem-with-encoder-decoder-architecture)
5. [Attention Mechanism](#attention-mechanism)

---

# Introduction
A Sequence-to-Sequence (Seq2Seq) model is a neural network architecture that takes one sequence as input and generates another sequence as output. The input and output sequences can have different lengths.

think of it as variable length many to many RNN

### Example machine translation:

```
Input:  "I love programming"
Output: "मुझे प्रोग्रामिंग पसंद है।"
```
As you can see in input we have english text that contains 3 words, as each word is represented as a vector we have total of 3 vector in input

Whereas in output we have a hindi text that contains 4 words i.e, 4 output vector

- input = 3 vectors
- output = 4 vectors

### Other examples
1. Text summarization

    ```
    Input:  Long article
    Output: Short summary
    ```
2. Chatbots
    ```
    Input:  "How are you?"
    Output: "I'm doing well, thanks!"
    ```




[Go To Top](#content)

---
# Encoder Decoder
Encoder-Decoder Architecture is a neural network framework in which an encoder transforms the input into an internal representation, and a decoder uses that representation to produce the desired output sequence.

<img src="./Images/encoder-decoder.jpg" style="width:500px">

Here:
- **Encoder:** reads the input sequence and converts it into a numerical representation (called a context vector or hidden state) that captures the meaning of the input.
- **Decoder:** takes the context vector from the encoder and generates the output sequence word by word.

### Encoder
The encoder reads the input sequence and converts it into a numerical representation (called a context vector or hidden state) that captures the meaning of the input, and to do this task we use LSTM cell.

eg.,\
input sequence = `"Nice to meet you"`

<img src="./Images/encoder.png" style="width:500px">

here ht and ct are the final context vector


#### Why use LSTM
In a Seq2Seq model, the encoder needs to understand the entire input sequence and preserve important information. Regular RNNs struggle with long sequences because they suffer from the vanishing gradient problem, causing them to forget earlier information.

LSTM is a type of RNN with memory cells that can retain important information for long periods, which makes it suitable for encoders that need to understand and summarize input sequences.

> Instead of LSTM you can also use GRU, as they also helps in retaining memory over a long sequence

### Decoder

The decoder takes the context vector from the encoder and generates the output sequence token by token.

e.g,\
output sequence: `"आपसे मिलकर अच्छा लगा"`    

<img src="./Images/decoder.png" style="width:500px">

here ht and ct are the context vector provided by the encoder

- `<start>` -> a special type of symbol that tells the model to `start` producing output
- `<end>` -> a special type of symbol that tells the model to `stop` producing output




[Go To Top](#content)

---


# How To Train Encoder Decoder Model

in machine translation we generally require a supervised dataset, i.e, tabular data with one column containing sentence from input language and other with output language

### Example

english | hindi
--- | ---
"Think about it" | "इस बारे में सोचिए"


now we first convert sentence into their respective vector format using one hot encoding

- english:
    - total 3 unique words -> 3 dimensional vectors
    - think = [1, 0, 0]
    - about = [0, 1, 0]
    - it = [0, 0, 1]
- Hindi
    - total 4 unique words + 2 special symbol `<start>` and `<end>` -> 6 dimension vector
    - `<start>` = [1, 0, 0, 0, 0, 0]
    - इस = [0, 1, 0, 0, 0, 0]
    - बारे = [0, 0, 1, 0, 0, 0]
    - में = [0, 0, 0, 1, 0, 0]
    - सोचिए = [0, 0, 0, 0, 1, 0]
    - `<end>` = [0, 0, 0, 0, 0, 1]

### Dataset in vector format

input vector | output vector
--- | ---
[[1, 0, 0], [0, 1, 0], [0, 0, 1]] | [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]

### forward propagation

now we pass the input vector into encoder and compute the context vector 

initially we'll be having the random weights and biases

<img src="./Images/Encoder-training.png" style="width:500px">


Now in case of decoder:
- we first pass this context vector as a input in decoder and compute the first output for first timestamp

    <img src="./Images/Decoder-timestamp-one.png" style="width:200px">

    soft max is just a neural network that convert the LSTM cell output into an required output, in our case its 6 dimension vector containing probability that represent the output word in vector format

    now:
    - y_predicted = [0.2, 0.1, 0.8, 0.5, 0.3, 0.6]  -> [0, 0, 1, 0, 0, 0] -> में
    - y_original = [0, 1, 0, 0, 0, 0] -> इस

    As you can see there is an error at y_predicted and y_original
- now for timestamp 2 instead of passing  previous output i.e, y_predicted we pass the y_original 

    <img src="./Images/Decoder-timestamp-two.png" style="width:500px">

    here for timestamp 2:
    - y_predicted = [0.3, 0.2, 0.4, 0.6, 0.7, 0.4]  -> [0, 0, 0, 0, 1, 0] -> सोचिए
    - y_original = [0, 0, 1, 0, 0, 0] -> इस 
- we repeat this until the model outputs end or our sequence ends
        
    <img src="./Images/Decoder-timestamp-third.png" style="width:500px">

    here for timestamp 2:
    - y_predicted = [0.3, 0.2, 0.4, 0.6, 0.7, 0.9]  -> [0, 0, 0, 0, 0, 1] -> `<end>`
    - y_original = [0, 0, 0, 1, 0, 0] -> बारे

    since model output `<end>` we stop prediction

### Calculate Loss


| timestamp | 1 | 2 | 3|
--- | --- | --- | ---
**y_predicted** | [0.2, 0.1, 0.8, 0.5, 0.3, 0.6] | [0.3, 0.2, 0.4, 0.6, 0.7, 0.4] | [0.3, 0.2, 0.4, 0.6, 0.7, 0.9] |
**y_original** |[0, 1, 0, 0, 0, 0] | [0, 0, 1, 0, 0, 0] | [0, 0, 0, 1, 0, 0] | 

now calculate the loos for each timestamp
- since we have multi class classification problem will be use categorical cross entropy as a loss function
- mathematically:

    $$L = -\sum_{i=1}^n y_i^{og}\ log(y_i^{pred})$$

    here:
    - n = dimension of output vector
    - $y^{og}$ = y_original
    - $y^{pred}$ = y_predicted
- for timestamp 1:
    - $y^{og}$ = [0, 1, 0, 0, 0, 0]
    - $y^{pred}$ = [0.2, 0.1, 0.8, 0.5, 0.3, 0.6]
    - $L_1 = -[(0 \times log\ 0.2) + (1 \times log\ 0.1) + (0 \times log\ 0.8) + (0 \times log\ 0.5) + (0 \times log\ 0.3) + (0 \times log\ 0.6)]$
    - $L_1 = - (1 \times log\ 0.1) = 1$
- for timestamp 2:
    - $y^{og}$ = [0, 0, 1, 0, 0, 0]
    - $y^{pred}$ = [0.3, 0.2, 0.4, 0.6, 0.7, 0.4]
    - $L_2 = - (1 \times log\ 0.4) = 0.39$
- for timestamp 3:
    - $y^{og}$ = [0, 0, 0, 1, 0, 0]
    - $y^{pred}$ = [0.3, 0.2, 0.4, 0.6, 0.7, 0.9]
    - $L_3 = - (1 \times log\ 0.6) = 0.22$

- total loss = 1 + 0.39 + 0.22 = 1.61
- average loss = 1.61 / 3 = 0.53

### Backpropagation

1. calculate gradient for loss using formula:

    $$\frac{\partial L}{\partial W} = \sum_{i=1}^n \frac{\partial L_i}{\partial W}$$

    here:
    - $W$ = trainable Parameter
    - $L$ = loss function 
    - $i$ = number of timestamp in decoder
2. Update the parameter using gradient decent:

    $$W_{new} = W_{old} - \alpha \frac{\partial L}{\partial W_{old}}$$



[Go To Top](#content)

---
# Problem with Encoder Decoder Architecture

Suppose we have an LSTM encoder.

Input sentence:

>"The student who studied machine learning for six months built an excellent project."

The encoder reads words one by one:
```
"The"      → h1
"student"  → h2
"who"      → h3
...
"project"  → h12
```
At each step we calculate the hidden state of LSTM till we get final hidden state:
```
h12
```
This becomes the context vector.

### In encoder decoder the assumption is:
> h12 contains all important information about the entire sentence.

The decoder only receives this vector.

hidden state size is decided at the time of training and is fixed, now suppose the hidden state size is:
```
512
```
Then regardless of whether the input contains:
```
10 words
100 words
1000 words
```
the output is still:
```
512 numbers
```
That means:
```
Input
--------------------------------
10 words   → 512 values
100 words  → 512 values
1000 words → 512 values
--------------------------------
```
- The amount of information grows.
- But the storage capacity remains fixed.

### Now imagine:
```
A paragraph of 200 words
```
The encoder is being asked to compress a large amount of information into a fixed-size representation.

Think of it like this:
```
200-page book
        ↓
1-page summary
        ↓
Reconstruct the entire book
```
Information will inevitably be lost.

As a result eventually the encoder is forced to discard information.

### Earlier Words Are More Likely to Be Forgotten

Consider a 100-word sentence.
```
w1 w2 w3 ... w100
```
The encoder processes sequentially:
```
h1 → h2 → h3 → ... → h100
``` 
When computing:

```
h100
```
the information from:
```
w1
```
has been transformed 99 times.
```
w1
 ↓
h1
 ↓
h2
 ↓
...
 ↓
h100
```
Each transformation slightly alters the representation.

By the end, the signal from the earliest words may become very weak.

### Static Representation of Context 
- In the original encoder-decoder architecture, the decoder receives the same context vector at every timestamp.

- However, different output tokens require information from different parts of the input sequence.

- Since the context vector is static and represents the entire sequence, the decoder cannot selectively focus on the most relevant input words for each output step.

- This limits performance, especially for long sequences, and is one of the motivations behind the attention mechanism.



[Go To Top](#content)

---
# Attention Mechanism
The attention mechanism is a technique used in neural networks that allows a model to focus on the most relevant parts of the input when producing an output.

Suppose you're translating:
```
"The animal didn't cross the street because it was too tired."
```

To understand what "it" refers to, you need to pay more attention to "animal" than to "street". Attention gives the model this ability.

### Classical Encoder-decoder

<img src="./Images/Encoder-decoder-flow.png" style="width:500px">

In classical encoder decoder architecture we provide two vector as an input for decoder to generate the output
- $S_{i-1}$ -> predicted output of previous timestamp
- $Y_{i-1}$ -> Original output of previous timestamp

### attention mechanism

<img src="./Images/Encoder-decoder-with-attention.png" style="width:500px">

In case of attention we get three input in decoder for decoder to generate the output

- $S_{i-1}$ -> predicted output of previous timestamp
- $Y_{i-1}$ -> Original output of previous timestamp
- $C_i$ -> think of it as attention input

### What is $C_i$

$C_i$ is a weighted combination of all encoder hidden states. It summarizes the parts of the input sequence that are most relevant for generating the output at time step i.

<img src="./Images/Ci-network.png" style="width:300px">

here:
- $\alpha_{ij}$ = is like a weight between nodes $C_i$ and $h_j$, it tells how much important $h_j$ is for generating the output in timestamp $i$

#### Mathematically

If the encoder hidden states are:

$$h_1, h_2, ...h_T$$

then:

$$C_i = \sum_{j=1}^T \alpha_{ij}h_j$$

where:

- $h_j$ = encoder hidden state at input position j,
- $\alpha_{ij}$ = attention weight telling how much the decoder at step i should focus on encoder state $h_j$,



[Go To Top](#content)

---