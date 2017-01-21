Xiang's Study of Theory and Practice in NN
===
Author: Zhong-Liang Xiang
Establishing Date: January 20th, 2017
<br>

# MNIST
MNIST(Modified National Institute of Standards and Thechnology) DATABASE (http://yann.lecun.com/exdb/mnist/)
* training set: 60,000 pics
* testing set: 10,000 pics

# Stochastic Gradient Descent
In practice, we usualy use **stochastic gradient descent** method to train a nueral network(NN) model.
>e.g. Suppose we have 50,000 training instances, the training instances will devide into 500 groups(mini-batches), that is, each mini-batch has 100 training instances which is used for getting a average gradient and we using this gradient to form a $\Delta w$ to update the parameter-matrix $W$. After we exhaust all the 500 mini-batch, we call one **epoch** finished. Several epochs would be spend before we satisfy with the models accuracy.

# Gradient Descent in Practice
## data preparation
>MNIST dataset
 train: 50,000
 validation: 10,000
 test: 10,000

define a basic structure:
```python
# -*- coding: utf-8 -*-

import numpy as np
# define a class
class Network (object):
    # __init__, define a constructor, same as java.
    def __init__(self, sizes):
      # 'self' is 'this' in java.
      # sizes, e.g. sizes=[2,3,1], indicate 1 input layers with 2 nodes, 1 mid layers with 3 nodes and 1 output layers with 1 node.
        self.num_layers = len(sizes)  # this.age = age
        self.sizes = sizes
        # np.random.randn(y, x): values~normal(0,1), generates a matrix with y rows and x columns
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]] # bias means bias' weight！ 3*1 and 1*1 matrix
        # zip()：to build tuples
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])] # 3*2 and 1*3 matrix

net = Network([2, 3, 1])
print(net.sizes)
print(net.biases)
print(net.num_layers)
print(net.weights)
```
see this equation: $a'=f(wa+b)$, we set **sigmoid function**(even this is a bad idea) as the $f(x)$. The code is as follows:
```python

```
