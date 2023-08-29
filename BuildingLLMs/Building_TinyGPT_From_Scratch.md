# TinyGPT Documentation

## Overview

This code defines and trains a simple GPT-like model named `TinyGPT` for the purpose of predicting the next word in a given sequence. The architecture comprises three self-attention layers followed by a feed-forward layer. 

## Modules and Classes

### 1. `PositionalEncoding(nn.Module)`

Embeds the positional information in sequences.

- `__init__(d_model, max_len=5000)`: Initializes the positional encodings.

### 2. `MultiHeadSelfAttention(nn.Module)`

A basic multi-head self-attention mechanism.

- `__init__(d_model, num_heads)`: Initializes query, key, value matrices and sets up the number of heads for the attention mechanism.

### 3. `FeedForward(nn.Module)`

A simple feed-forward neural network.

- `__init__(d_model, d_ff)`: Defines a feed-forward neural network with one hidden layer.

### 4. `TinyGPT(nn.Module)`

A tiny version of GPT with three attention layers.

- `__init__(vocab_size, d_model=16, num_heads=8, d_ff=64, max_len=512)`: Initializes the TinyGPT model with specified parameters.

### Utility Function

- `create_input_target_pairs(tokenized_sentences)`: Creates input and target pairs from tokenized sentences for training. The target for each input sentence is the sentence shifted by one token.

## Training Process

The training process involves the following steps:

1. Tokenization and padding of input sentences.
2. Creating input-target pairs.
3. Initializing the model, loss function, and optimizer.
4. Iteratively passing the input through the model, calculating the loss, and updating the model's weights using backpropagation.

## Sample Usage

The provided code also contains an example usage section. A few sample sentences are tokenized and padded to a fixed length. These are then passed through the model during training. After training, the model predicts the next word for each token in the input sequence.

## Output

The code will print the original input sentences and their corresponding predictions at the end of the training process.

---

Note: This documentation provides a high-level overview of the code's structure and purpose. For a detailed understanding, one should examine the code directly. Ensure that you have the necessary dependencies installed and are familiar with PyTorch's syntax and operations.
