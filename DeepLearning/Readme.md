# Content
1. [Introduction](#introduction)
2. [Perceptron](#perceptron)
3. [Perceptron Trick](#perceptron-trick)


# Introduction
Deep learning is a subset of AI and ML that is inspired by the structure of a human brain

It is a part of broader family of ML methods based on artificial neural network with representation learning
> **Representation learning** is a concept in machine learning where the model automatically learns useful features (representations) from raw data, instead of you manually defining them.

> in **Representation learning**, model automatically perform Feature Engineering

<img src="./Images/deep-learning-subset-of-ai-diagram.png" style="width:500px">

Deep learning algorithm attempts to draw similar conclusion as human would by continually analyzing data with give logical structure called neural network

**Example:**

<img src="./Images/DNN-1.webp" style="width:500px">

DL algorithm uses multiple layers to progressively extract higher-level features form the raw input. 

For example, in image processing lower layers may identify edges, while higher layer may identify the concept relevant to human such as digit or latter or face

### DL vs ML
| Feature                | Machine Learning (ML)                               | Deep Learning (DL)                                      |
| ---------------------- | --------------------------------------------------- | ------------------------------------------------------- |
| Definition             | Subset of AI that learns from data using algorithms | Subset of ML that uses neural networks with many layers |
| Feature Engineering    | Manual (you define features)                        | Automatic (model learns features)                       |
| Data Requirement       | Works with small to medium datasets                 | Needs large datasets                                    |
| Performance            | Good for simpler problems                           | Better for complex tasks                                |
| Computation Power      | Less (CPU often enough)                             | High (GPU/TPU required)                                 |
| Training Time          | Faster                                              | Slower                                                  |
| Interpretability       | Easier to understand                                | Harder (“black box”)                                    |
| Examples of Algorithms | Decision Trees, SVM, KNN                            | CNN, RNN, Transformer                                   |
| Best For               | Structured data (tables, CSV)                       | Unstructured data (image, audio, text)                  |



### Types of Neural Networks
| Neural Network                       | Description                                               | Best For                                 | How It Works                                                                                                      |
| ------------------------------------ | --------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| MLP (Multilayer Perceptron)          | Basic fully connected neural network with multiple layers | Tabular data, classification, regression | Data passes through multiple fully connected layers where each neuron applies weights and activation functions    |
| CNN (Convolutional Neural Network)   | Specialized for processing grid-like data (images)        | Image processing, computer vision        | Applies convolution filters to extract features (edges, patterns), followed by pooling and fully connected layers |
| RNN (Recurrent Neural Network)       | Designed for sequential data with memory                  | Text, speech, time-series                | Processes input step-by-step while passing previous hidden state to next step                                     |
| Autoencoder                          | Learns to compress and reconstruct data                   | Data compression, denoising              | Encoder reduces input into smaller representation, decoder reconstructs original data from it                     |
| GAN (Generative Adversarial Network) | Two networks competing with each other                    | Image generation, deepfakes              | Generator creates fake data, discriminator evaluates it; both improve through competition                         |

[Go To Top](#content)

---
# Perceptron
Perceptron is an algorithm used for supervised ML and is one of the simplest types of artificial neural networks

<img src="./Images/perceptron.png" style="width:500px">

Here
1. **Inputs**: 
    - These are the features/data points coming into the model.
    - Each input represents some information
    
2. **Weights**: 
    - Each input is connected with a weight.
    - These control how important each input is
    - Larger weight → more influence
    - Smaller weight → less influence
3. **Summation Block**: 
    - All weighted inputs are added together here.
    - This computes the linear combination
    - $z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$
4. **Bias**: 
    - The bias is added to the sum
    - It shifts the decision boundary (like adjusting a threshold)
5. **Activation Function**: 
    - Takes the summed value and decides output
    - Example:\
    step function:
        - If the result ≥ 0 → output = 1
        - If the result < 0 → output = 0

in the training phase of the perceptron we feed the training data and try to find out the compatible `Weight` and `Bias` such that predicted output and actual output matches

Once we found out those `Weight` and `Bias` from training phase we use those same `Weight` and `Bias` for future prediction

### Perceptron is Inspired by Neuron
- perceptron was designed by copying the basic idea of how a human `neuron` works.
- A human `neuron` takes signals from `dendrites`, processes them, and sends an output, so a perceptron does the same with numbers.
- In a `neuron`, `synapses` decide signal strength, and in a perceptron, `weights` decide input importance.

    <img src="./Images/neuron-perceprton.png" style="width:500px">

- The perceptron does not copy the full complexity of the brain, it only copies the simple “input → process → output” behavior.
- So, a perceptron is a simplified mathematical version of a human `neuron`, not an exact copy.

### Geometrical Intuition Behind perceptron

Lets take a summation function of a perceptron

$$z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

keep $n = 2$

$$z = w_1x_1 + w_2x_2 + b$$

if you look closely this function is similar to equation of string line:

$$Ax + By + C = 0$$


so when we train our perceptron on a dataset we get a line as follow


<img src="./Images/binary-classification.webp" style="width:500px">

now whenever we want to predict new value we pass the input data ($x_1, x_2$), which inside summation block convert into an equation $Ax_1 + Bx_2 + C$
- A = weight of feature $x_1$
- B = weight of feature $x_2$
- C = Bias
- $Ax_1 + Bx_2 + C$ = represent a point ($x_1, x_2$) inside a plane

Inside a activation function passes the result through a step function:

- If $Ax_1 + Bx_2 + C$ ≥ 0 → output = Class A
- If $Ax_1 + Bx_2 + C$ < 0 → output = Class B


>Because of this we can classify our data into two classes, therefor we called perceptron a binary classifier

**with 2D data we get a line that separate two classes, where as in 3D we get a plane and for 4D and above we get hyperplane**

### Why compare with 0
to understand this we first need to understand how to check on which side of a line a point will lie?

To determine which side of a line a point lies on, you can use a very clean geometric idea based on the line equation sign test.

If a line is written as:

$$ax + by + c = 0$$

Then for any point ($x_1, y_1$), compute:

$$S = ax_1 + by_1 + c$$

- If S > 0 → positive region → point lies on one side of the line
- If S < 0 → negative region → point lies on the other side
- If S = 0 → point lies exactly on the line

### Woks only with liner data
in perceptron we find the best fit line that separate two classes, but we can only find this best fit line if we have liner data and will not work with non liner data

<img src="./Images/non-liner-binary-classification.jpg" style="width:500px">

[Go To Top](#content)

---
# Perceptron Trick
Perceptron Trick is a way to find the best fit line that best separate two classes

> this is iterative approach i.e, we can perform then trick in loop until we find the best fit line

we start with any random line

<img src="./Images/percepton-trick-1.png" style="width:500px">

now we randomly pick any point and check whether or not it is properly classified or not

here:
- 2,5 supposed to belong in positive region (properly classified)
- -2, -4 supposed to belongs in negative region (incorrectly classified)

if the point is properly classified then we do nothing and switch to next point

if the point is not classified correctly then that point will move the line, such that the new line will properly classify that point

in our case point (-2, -4) will move the line so that this point will come under the negative region of the line

<img src="./Images/percepton-trick-2.png" style="width:300px">

To make this transformation we only need to change the weight and bias such that the new line will  properly classified respective point

### How changing the weight and bias transform the line

Equation:

$$Ax_1 + Bx_2 + C$$

- A = weight of feature $x_1$
- B = weight of feature $x_2$
- C = Bias

Changing the C moves line up or down without changing the slop

changing the A will rotate the line along the point $x_1$

changing the B will rotate the line along the point $x_2$

### How to apply changes to weight and bias

lets take equation of line:

$$2x + 3y + 5 = 0 _{--------}(i)$$



And we have coordinates of improper classified point as follow:

$$x = 4, y = 5$$

```
(4 * 2) + (5 * 3) + 5 = 8 + 15 + 5 = 28 

28 > 0 -> +ve region
```

we add one arbitrary point:

$$x = 4, y = 5, c = 1_{--------}(ii)$$

from $(i)$ we get
- A = 2
- B = 3
- C = 5

just subtract this value form $(ii)$ x, y, c to get new equation
```
A - x = 2 - 4 = -2
B - y = 3 - 5 = -2
C - c = 5 - 1 = 4
```

Therefor new equation of line:

$$-2x-2y + 4 = 0$$

```
(-2 * 4) + (-2 * 5) + 4 = -8 + (-10) + 4 = -14

-14 < 0 -> -ve region
```
### How to pick the arbitrary point
higher the value of arbitrary point higher the transformation of line, where as lower the value of arbitrary point lower the transformation

hence we can say that this arbitrary point defines the learning rate of our model 

generally is most of the cases learning rate is equal to `0.01`

Therefor instead of subtracting the x, y ,c value directly we use formula:

$$new\ coefficient\ of\ line = old\ coefficient\ of\ line - (learning\ rate \times coordinates)$$

Example:

$A_{new} = A_{old} - 0.01 \times x = 2 - 0.04 = 1.96$

$B_{new} = B_{old} - 0.01 \times y = 3 - 0.05 = 2.95$

$C_{new} = C_{old} - 0.01 \times c = 5 - 0.01 = 4.99$

Therefor new equation of line:

$$1.96x+2.95y + 4.99 = 0$$

[Go To Top](#content)

---
