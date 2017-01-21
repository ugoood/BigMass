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
## Data Discraption
>MNIST dataset
 train: 50,000
 validation: 10,000
 test: 10,000

## Simple NN
![SGD_weight_upgrate]("SGD_weight_upgrate")

## NN Code and Explanation
define a basic structure:
```python
# -*- coding: utf-8 -*-

import numpy as np
# define a class
class Network (object):
    """ A constructor looks like that of java"""
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
In the class **Network**, we have a function:

```python
def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):  # chapter 9
""" Train the neural network using mini-batch stochastic gradient descent.
The "training_data" is a list of tuples "(x, y)" representing the training inputs and the desired outputs. The other non-optional parameters are self-explanatory.  If "test_data" is provided then the network will be evaluated against the test data after each epoch, and partial progress printed out.  This is useful for tracking progress, but slows things down substantially.

Parameters
===
training_data: a list of tuples "(x, y)", in which the "x" is a picture, "y" is the desired label;
epochs: how many training rounds you want;
mini_batch_size: the size of mini-batch;
eta: a learning rate;
test_data: test_data
"""

  if test_data: n_test = len(test_data)  # "if test_data" means if test_data exists, return true and calculate the length of test data.
  n = len(training_data)
  for j in xrange(epochs):  # xrange(epochs) is a list [0, 1, ..., epochs]
      random.shuffle(training_data)  # shuffle the training data
      # "mini_batches" is a list [[], [], ..., []]
      mini_batches = [training_data[k : k + mini_batch_size] for k in xrange(0, n, mini_batch_size)]

      for mini_batch in mini_batches:
          self.update_mini_batch(mini_batch, eta)  # a one of core function that is to optimal self.biases(several vectors) and self.weights(several matrices)
          if test_data:
              print("Epoch {0}:{1}/{2}".format(j, self.evaluate(test_data), n_test))  # a kind of output format in python.
          else:
              print("Epoch {0} complete".format(j))
```


Here should insert a image! (SGD_weight_upgrate.png)

![SGD_weight_upgrate]("SGD_weight_upgrate")

```python
def update_mini_batch(self, mini_batch, eta):
        """
            Update the network's weights and biases by applying
            gradient descent using backpropagation to a single mini batch.
            The "mini_batch" is a list of tuples "(x, y)", and "eta"
            is the learning rate.
        """

        nabla_b = [np.zeros(b.shape) for b in self.biases]  # initialize with zero for b
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:  # for each training instance (x, y)
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)  # respectively, calculate partial derivative of b, w given a Cost function.

            """
                NOTICE: nb, dnb, nw and dnw here, all of them are the "scalar quantity"
                BUT other else e.g. "nabla_b, delta_nabla_b" extra are the matrices !
            """
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]  # summation of partial derivative of biases
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]  # same as top, but for weights
        self.biases = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)] # updating equation of biases in stochastic gradient descent learning algorithm
        self.weights = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]# same as top, but for weights

```
