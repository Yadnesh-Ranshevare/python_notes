# Content
1. [Introduction](#introduction)


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