
# Content

1. Self Attention
    -  [Self Attention](#self-attention)
    -  [Properties of Self Attention](#properties-of-self-attention)
    -  [Task Specific Embeddings in Self Attention](#task-specific-embeddings-in-self-attention)
2. [Multi Head Attention](#multi-head-attention)
3. [Positional Encoding](#positional-encoding)
---
# Self Attention

NLP (Natural Language Processing) is a field of computer science and AI focused on enabling computers to understand, interpret, generate, and interact with human language like human text.

But the problem is that our computer only understand the numeric value and is unable to process any textual input.

Therefore in any NLP application the first important step to convert the text into number, and this numeric representation of text is what we called vector / token



### Embeddings

- Embeddings are one of the most popular methods for converting words into vectors.

- Embeddings convert things like words or sentences into lists of numbers such that similar meanings correspond to nearby vectors.

#### Why do we need embeddings?
Suppose we have:
```
cat
dog
car
```
Using One-Hot Encoding:
```
cat → [1,0,0]
dog → [0,1,0]
car → [0,0,1]
```
The model sees all three as equally unrelated.

But with embeddings:
```
cat → [0.2, -0.7, 0.9, ...]
dog → [0.3, -0.6, 0.8, ...]
car → [-0.8, 0.4, -0.1, ...]
```
Now, cat and dog have similar vectors because they are semantically related.

#### How embedding Capture semantic similarity
embedding convert word into vector such that Similar meanings word have similar vectors.

Examples:
<!-- 
- king ↔ queen
- cat ↔ dog
- happy ↔ joyful

All of those pairs will have similar vectors -->

<img src="./Images/embedding-vector.png" style="width:300px">

As you can see in above image
- `cat` and `dog` -> similar vector
- `cat` / `dog` and `snake` -> large difference between vector

This is because `cat` and `dog` is somewhat similar to each other as they both have four legs, they both can be tame, etc

whereas `snake` is soo much different from `cat` and `dog`, like `cat` and `dog` are mammals whereas `snake` is reptile

### Problem with embeddings
Embedding assign one vector per word, regardless of context.

lets suppose we have sentence like:
```
I deposited money in the bank.
I sat by the river bank.
``` 
Both occurrences of bank get the same vector, even though they mean different things, and since the vector is identical, the model mixes information and will think that they both have same meanings.

Therefore we need a mechanism where we can change the vector embedding according to sentence, like in above example both bank will have different vectors as they have different meaning

To solve this problem we use self attention, it allow us to create the different vectors for same word if they have different meaning in a sentence

### How self attention solves it?
Self-attention is a mechanism that determines how much "attention" different words or tokens in a sequence should pay to each other

Consider the sentence:\
`"The animal didn't cross the street because it was too tired."`

To understand what "it" refers to, the model needs to look at the other words in the sentence. Self-attention helps the model decide that "it" is related to "animal" more than to "street".

### Example:
consider a sentences:
1. money bank grows
2. river bank flows

here we can see word `bank` appear in both of those sentence but in each sentence the meaning of that word is different, therefore we must represent that word with different vector for different sentence

to do that we first calculate the embedding for each words 
- money = vector1
- bank = vector2
- grows = vector3 
- river = vector 4
- flows = vector6

> well only be having one vector for word bank as embedding generate same vector for same word

Now using self attention:

- sentence 1:
    - bank = 0.7 [money vector] + 0.1[bank vector] + 0.2[grows vector]
- sentence 2:
    - bank = 0.6 [river vector] + 0.2[bank vector] + 0.2[flows vector]

Now as you can see for both sentence we have different vector embedding for word `bank` indicating their meaning is different 

Also because of different vector representation the model now can distinguished between those words


You can think of it as:\
while generating the text embedding each word in a sequence giving attention to other words in its own sequence

- sentence 1 bank = 0.7[money vector] + 0.1[bank vector] + 0.2[grows vector]
    - here word bank is giving around 70% attention to vector1 i.e, money while generating embeddings
    - therefore the model will know that we are talking about money bank
- sentence 2 bank = 0.6[river vector] + 0.2[bank vector] + 0.2[flows vector]
    - here word bank is giving around 60% attention to vector4 i.e, river while generating embeddings 
    - Therefore the model will know that we are not talking about money bank, and that it's something else

### Similarly we can do for other words also
consider a sentences:
1. money bank grows
2. river bank flows

now their word embedding are:
- money = vector1
- bank = vector2
- grows = vector3 
- river = vector 4
- flows = vector6

Now with self attention:
- Sentence 1:
    - money = 0.4[vector1] + 0.1[vector2] + 0.6[vector3]
    - bank = 0.7[vector1] + 0.1[vector2] + 0.2[vector3]
    - grows = 0.5[vector1] + 0.2[vector2] + 0.3[vector3]
- Sentence 2:
    - river = 0.1[vector4] + 0.3[vector2] + 0.5[vector5]
    - bank = 0.6[vector4] + 0.2[vector2] + 0.2[vector5]
    - flows = 0.5[vector4] + 0.4[vector2] + 0.6[vector5]

### Similarity

Consider a word:
- money bank grows

their word embedding:
- money = vector1
- bank = vector2
- grows = vector3 

now using self attention:
```
bank = a [vector1] + b [vector2] + c [vector3]
```
- here a,b,c are fraction value that represent the similarity scores
    - a = similarity between bank vector and money vector
    - b = similarity between bank vector and bank vector
    - c = similarity between bank vector and grows vector
- higher the similarity more related the words are to each other

####  calculate the similarity using dot product

Whenever we have two vector we can check how much those two vector are related to each other by simply calculating the dot product between those vectors

- higher the dot product = higher the similarity
- lower the dot product = lower the similarity

from above Example:
- $vector1 \cdot vector2$ = similarity between word money and bank

Now from this we can compute:
```
bank = a [vector1] + b [vector2] + c [vector3]
```
- a = $vector2 \cdot vector1^T$
- b = $vector2 \cdot vector2^T$
- c = $vector2 \cdot vector3^T$

Therefore:

$$
bank = (vector2 \cdot vector1^T)[vector1] + (vector2 \cdot vector2^T)[vector2] + (vector2 \cdot vector3^T)[vector3]
$$

here:
- $vector1, vector2, vector3$ = n dimension vector generated using embeddings
- $vector1^T, vector2^T, vector3^T$ = Transpose vectors of $vector1, vector2, vector3$ respectively

#### Example:

sentence = Money bank grows

using embeddings we get:
- money = [0.2, 0.5, 0.3]
- bank = [0.5, 0.1, 0.4]
- grows = [0.8, 0.5, 0.1]


$$
bank = 
\left(
\begin{bmatrix}
0.5 & 0.1 & 0.4 
\end{bmatrix}
\cdot
\begin{bmatrix}
0.2\\
0.5\\
0.4
\end{bmatrix}
\right)
\begin{bmatrix}
0.2 & 0.5 & 0.4 
\end{bmatrix}
+
\left(
\begin{bmatrix}
0.5 & 0.1 & 0.4 
\end{bmatrix}
\cdot
\begin{bmatrix}
0.5\\
0.1\\
0.4
\end{bmatrix}
\right)
\begin{bmatrix}
0.5 & 0.1 & 0.4 
\end{bmatrix}
+
\left(
\begin{bmatrix}
0.5 & 0.1 & 0.4 
\end{bmatrix}
\cdot
\begin{bmatrix}
0.8\\
0.5\\
0.1
\end{bmatrix}
\right)
\begin{bmatrix}
0.8 & 0.5 & 0.1
\end{bmatrix}
$$


$$
bank = 0.27 
\begin{bmatrix}
0.2 & 0.5 & 0.4 
\end{bmatrix}
+
0.42
\begin{bmatrix}
0.5 & 0.1 & 0.4 
\end{bmatrix}
+
0.49
\begin{bmatrix}
0.8 & 0.5 & 0.1
\end{bmatrix}
$$

<!-- 
$$
bank = 
\begin{bmatrix}
0.054 & 0.135 & 0.081
\end{bmatrix}+
\begin{bmatrix}
0.210 & 0.042 & 0.168
\end{bmatrix}+
\begin{bmatrix}
0.392 & 0.245 & 0.049
\end{bmatrix}
$$

$$
bank = 
\begin{bmatrix}
0.656 & 0.422 & 0.298
\end{bmatrix}
$$ -->

### Normalization

from above example we get to know we can represent word bank in vector format using self attention mechanism

where;

$$bank = 0.27[vector1] + 0.42[vector2] + 0.49[vector3]$$

But the here problem is that in this representation we doesn't exactly know how much attention we are giving the each vector in a sequence

Therefore in this case we normalize the output of dot product, so that their sum will be equal to 1

Example:
- a = 0.27
- b = 0.42
- c = 0.49

$$a_{norm} = \frac{a}{a+b+c} = \frac{0.27}{1.18} \approx 0.23$$

$$b_{norm} = \frac{b}{a+b+c} = \frac{0.42}{1.18} \approx 0.355$$

$$c_{norm} = \frac{c}{a+b+c} = \frac{0.49}{1.18} \approx 0.415$$

Therefore

$$bank = 0.23[vector1] + 0.355[vector2] + 0.415[vector3]$$

now you can see word bank gives:
- 23% attention to vector 1
- 35.5% attention to vector 2
- 41.5% attention to vector3

Sometimes we use softmax instead of regular normalization to normalize the dot products



[Go To Top](#content)

---
# Properties of Self Attention
there are two major properties that self attention mechanism show i.e, 
1. Parallel computation
2. General contextual embeddings

### 1. Parallel computation
- once we compute the embedding for all the words in the sequence we can apply self attention to all of them parallelly
- this is because self attention is only depends on the embedding of the sequence to compute new vectors and is not depending on self attention vector of other words
- example:
    - embeddings:
        - money = [vector1]
        - bank = [vector2]
        - grows = [vector3]
    - now self attention can compute new vectors for each of those word parallelly as self attention vector of word bank is not depending on self attention vector of money or grows and same for other self attention vectors also

we can do this using liner algebra:
- money = [0.2, 0.5, 0.3]
- bank = [0.5, 0.1, 0.4]
- grows = [0.8, 0.5, 0.1]

matrix of embeddings:

$$
\begin{bmatrix}
money \ vector\\
bank\ vector\\
grows\ vector
\end{bmatrix} =
\begin{bmatrix}
0.2 & 0.5 & 0.3\\
0.5 & 0.1 & 0.4\\
0.8 & 0.5 & 0.1
\end{bmatrix}
$$

Transpose matrix

$$
\begin{bmatrix}
0.2 & 0.5 & 0.8\\
0.5 & 0.1 & 0.5\\
0.3 & 0.4 & 0.1
\end{bmatrix}
$$

dot product

$$
\begin{bmatrix}
0.2 & 0.5 & 0.3\\
0.5 & 0.1 & 0.4\\
0.8 & 0.5 & 0.1
\end{bmatrix}
\begin{bmatrix}
0.2 & 0.5 & 0.8\\
0.5 & 0.1 & 0.5\\
0.3 & 0.4 & 0.1
\end{bmatrix} =
\begin{bmatrix}
0.38 & 0.27 & 0.44\\
0.27 & 0.42 & 0.49\\
0.44 & 0.49 & 0.90
\end{bmatrix}
$$

Using normalization

$$
\begin{bmatrix}
0.35 & 0.25 & 0.40\\
0.23 & 0.36 & 0.42\\
0.24 & 0.27 & 0.49
\end{bmatrix}
$$

multiply this with embedding matrix:

$$
\begin{bmatrix}
0.35 & 0.25 & 0.40\\
0.23 & 0.36 & 0.42\\
0.24 & 0.27 & 0.49
\end{bmatrix}
\begin{bmatrix}
money \ vector\\
bank\ vector\\
grows\ vector
\end{bmatrix}
$$

Therefore:

$$
\begin{bmatrix}
0.35\ money\ vector + 0.25\ bank\ vector+ 0.40\ grows\ vector\\
0.23\ money\ vector + 0.36\ bank\ vector+ 0.42\ grows\ vector\\
0.24\ money\ vector + 0.27\ bank\ vector+ 0.49\ grows\ vector
\end{bmatrix}
$$

from this we can see:
- money = $0.35\ money\ vector + 0.25\ bank\ vector+ 0.40\ grows\ vector$
- bank = $0.23\ money\ vector + 0.36\ bank\ vector+ 0.42\ grows\ vector$
- grows = $0.24\ money\ vector + 0.27\ bank\ vector+ 0.49\ grows\ vector$

### 2. General contextual embeddings

In any Deep learning model there will always be few training parameters like weights and biases, but in self attention there is no such training parameter

Since there is no learning parameter the model is not learning from our data and is dependent on current sequence (sentence)

Therefore we can say that self attention mechanism is independent of your dataset, and can generate general contextual embeddings

These embeddings capture the meaning of tokens in context but are not optimized for any specific task.

Example:\
`"The movie was amazing."`

The embedding of "amazing" captures its contextual meaning, but it doesn't explicitly represent:

- sentiment
- spam probability
- topic category
- named entity type

It is a general representation.

#### Problem with general contextual embeddings
A general embedding tries to capture overall meaning, not what your task cares about.

Example:
```
"The movie was absolutely fantastic."
```
For sentiment analysis, the important information is that "fantastic" = positive sentiment.

A general embedding also encodes:

- grammar
- topic
- syntax
- word relationships
- sentence structure

Much of that information may be irrelevant to sentiment classification.

General embeddings are designed to work across many tasks.

As a result, they often contain features that act as noise for a specific task.


[Go To Top](#content)

---
# Task Specific Embeddings in Self Attention
> This is the actual self attention we used in todays date

As we learn that normal self attention generate the general contextual embeddings which tries to capture overall meaning of the sentence, and not what your task cares about.

To solve this problem we usually generate the task specific embeddings 

### How normal self attention work
normal self attention follows a simple flow:
1. find the vector embeddings
2. dot product between the embeddings to find similarity score
3. normalize the similarity score
3. multiply embedding with similarity score

example:
- sentence = `"money bank grows"`
- embeddings:
    - money = e1
    - bank = e2
    - grows = e3

- now with self attention:\
money = ae1 + be2 + ce3
- you can see how we compute that in following image

<img src="./Images/Self-attention.png" style="width:500px">

now if you look closely we have use 3 vector to solve this self attention problem i.e, 
- 2 vectors for dot product
- 1 vector for final attention representation

Now on the bases of how we have use those vector we can classify them into three types:

### 1. Query Vector (Q)
A Query represents:

>"What information am I looking for?"

When processing a token, its query is compared against every token's key.

For example, in:

>"money bank grows"

Suppose we're computing attention for money.

The query of money asks:

>"Which words are relevant to me?"
### 2. Key Vector (K)

A Key represents:

> "What kind of information do I contain?"

Every token publishes a key.

Examples:
```
money -> k₁
bank  -> k₂
grows -> k₃
```
### 3. Value Vector (V)
Value represents:

>"What information should I send if someone attends to me?"

Once attention scores are computed, we don't use keys anymore.

Instead we combine values.

Suppose attention weights become:
```
money -> 0.1
bank  -> 0.8
grows -> 0.1
```
Then:

money = 0.1 $V_{money}$ + 0.8 $V_{bank}$ + 0.1 $V_{grows}$

### Example
here is the example of word `money` in sentence `money bank grows`

<img src="./Images/Self-attentio-with-vectors.png" style="width:500px">

### How to divide a embedding into 3 vectors
from the above example we can see that we need to somehow convert the one embedding vector into 3 vectors i.e, query vector, key vector and value vector 

Therefore in order to transform our one embedding vector into 3 different vector we use liner transformation

> A linear transformation takes an input vector and produces a new vector according to some rule (usually a matrix multiplication). The vector may be stretched, shrunk, rotated, reflected, or sheared.

Hence we simple matrix multiplication we can transform our original embedding vector into 3 different vectors

Example:
- $e_{bank}$ =  embedding vector for word bank
- $W_q$ = matrix for query transformation
- $W_k$ = matrix for key transformation
- $W_v$ = matrix for value transformation

Therefore
- $e_{bank} \times W_q = Q_{bank}$ -> query vector
- $e_{bank} \times W_k = K_{bank}$ -> key vector
- $e_{bank} \times W_v = V_{bank}$ -> value vector

now since we have this 3 vectors we can use that self attention flow to generate the task specific embeddings

<img src="./Images/task-specific-self-attention.png" style="width:700px">

> Note: the parallel execution property of self attention is still true for this architecture

### how to find the transformation matrix $W_q, W_k$ and $W_v$
we doesn't have to decide what the matrix will be like as its done with the help of our data

- we start with the random values for matrix
- feed the data for training
- predict the output
- calculate the loss
- update the matrix values using backpropagation
- repeat until the loss is minimum

### How this solve task specific problem
normal self attention generate the general contextual embeddings which tries to capture overall meaning of the sentence, and not what your task cares about.


This is because there is no training involve in normal self attention, so our self attention model doesn't learn anything from our data. Because of this whatever vector are being generated using self attention are general contextual embedding and are not task specific contextual embedding

Therefore we use 3 transformation vectors $W_q, W_k$ and $W_v$ that learn from the dataset and transform the embedding according to our dataset and the task needed

### Mathematical Representation

$$Attention(Q,K,V) = Softmax\left( \frac{QK^T}{d_K}\right)V$$

where:
- $Q$ = quey vector
- $K$ = key vector
- $V$ = value vector
- $d_K$ = dimension of key vector

Also
- $QK^T$ = dot product between query vector and key vector

#### why $\frac{1}{d_K}$
in dot product as number of dimension of a vector increases the variance also increases

> high valance means values are far apart from each other, i.e, some values ae too big whereas some are too small

because of high variance softmax convert big number into high probability (90%-95%) and small number into small probability (1%-5%)

> softmax is just a function that takes a list of number as input and scale them such that their sum will be equal to 1 i.e, 100%

because of this we face the vanishing gradient problem where  points with low probability barely update its value

therefore to solve this vanishing gradient problem we somehow need to reduce the high variance of dot product

And since the reason behind high variance is high number of dimension of a vector we divide the dot product with the number of dimension to scale the product down to lower the variance

> if the list has high values its variance will be high and if it has small values its variance will be small



[Go To Top](#content)

---
# Multi Head Attention
Although self attention is good for capturing the contextual embedding of any word but they fails in cas of ambiguous sentence

Example:
- Sentence: `"The man saw the astronomer with a telescope"`
- who has the telescope?
    - does man use telescope to saw astronomer?
    - Or there was a astronomer who has telescope with him and that man just happen to saw that astronomer along with that telescope
- now as you can see since this sentence has multiple meaning, but our self attention can only be able to capture one one of them
- so with self attention we can either capture:
    - man with telescope
    - Or astronomer with telescope
- not both at the same time

Now to solve this problem we use multi head attention

### What is multi head attention
as we see in above example if a sentence has multiple meaning self attention can only capture one of them at a time, Therefore to solve this problem we can use multiple self attention so that each self attention will capture different meaning. Hence we call it self multi head attention


Example:
- Sentence: `"The man saw the astronomer with a telescope"`
- 1st self attention ->  man use telescope to saw astronomer
- 2nd self attention -> astronomer with telescope

as you can see with 2 self attention working together we can capture both of those meaning

<img src="./Images/multi-head-attention.png" style="width:500px">

### How to do that?
in self attention to generate any embeddings we need three essential vectors
- $Q$ = query vector
- $K$ = key vector
- $V$ = value vector

and to compute this vectors we use matrix multiplication 
- $W_k$ = matrix for key vector
- $W_Q$ = matrix for query vector
- $W_V$ = matrix for value vector

this matrix is like a trainable parameter that train over the with the help of data

Now for single self attention we need one set of that vector, by that logic for two self attention we need two sets

Therefore we can say that for multi head attention we just need multiple set of $Q, V$ and $K$ vectors
- $Q_1, K_1, V_1$ ->  1st self attention 
- $Q_2, K_2, V_2$ ->  2nd self attention 
- $Q_n, K_n, V_n$ ->  nth self attention 

and to compute this vector we need multiple matrix
- $W_k^1, W_V^1, W_Q^1$ -> key, value and quey matrix for 1st self attention
- $W_k^2, W_V^2, W_Q^2$ -> key, value and quey matrix for 2nd self attention
- $W_k^n, W_V^n, W_Q^n$ -> key, value and quey matrix for nth self attention

Now for sentence with multiple meaning:
- $W_k^1, W_V^1, W_Q^1$ -> $Q_1, K_1, V_1$ -> vector1 -> capture 1st meaning
- $W_k^2, W_V^2, W_Q^2$ -> $Q_2, K_2, V_2$ -> vector2 -> capture 2nd meaning\
and so on

### how to combine multiple output vector
now using multi head attention we may generate multiple contextual embedding so that they can capture multiple meanings, but in output we want single vector that can represent all that information

and to do that we just concatenate those multiple contextual embedding into single vector and then apply liner liner transformation to merge them

Example:
- $W_k^1, W_V^1, W_Q^1$ -> $Q_1, K_1, V_1$ -> $[a, b, b]$
- $W_k^2, W_V^2, W_Q^2$ -> $Q_2, K_2, V_2$ -> $[e, f, g]$

- concatenate: $[q, b, c, e, f, g]$
- liner transformation: $[q, b, c, e, f, g] \times W_0 = [h, i, j]$

here 
- $[h, i, j]$ is the final output of our multi head attention
- $W_0$ is the matrix that merger multiple self attention vectors, and is trainable just like $W_k, W_V, W_Q$

<img src="./Images/Multi-head-attention-2.png" style="width:700px">



[Go To Top](#content)

---
# Positional Encoding
A self attention processes all words in parallel, unlike an RNN which processes them one after another. This creates a problem where the self attention has no inherent understanding of the order of words.

For example:

- "The cat chased the dog."
- "The dog chased the cat."

Without positional information, these sentences would look like the same collection of words and our model we think both are same.

Positional encoding solves this by giving every word information about where it appears in the sequence.

[Go To Top](#content)

---