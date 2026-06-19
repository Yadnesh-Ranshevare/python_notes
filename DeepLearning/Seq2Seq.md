# Content
1. [Introduction](#introduction)
2. [Encoder Decoder](#encoder-decoder)
3. [How To Train Encoder Decoder Model](#how-to-train-encoder-decoder-model)

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