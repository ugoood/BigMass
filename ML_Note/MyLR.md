Logistic Regression 算法向量化实现及心得
===
Author: 相忠良(Zhong-Liang Xiang)
Email: ugoood@163.com
Date: Sep. 23st, 2017

根据 Andrew Ng 老师的深度学习课程课后作业及指导，参照吴老师代码完成了这个LR的coding．

**(重要)吴老师建议,数据应组织成下列形式，有利于扫除编程bug：**
* X.shape = (n_x, m), n_x是样本维度，m是样本个数
* Y.shape = (1, m)
* w, b应该分开，其中:
  - b is a scaler
  - w.shape = (n_x, 1)
* A = sigmoid(np.dot(w.T, X)+b), A.shape = (1, m)
* dw.shape = (n_x, 1)
* db is a scaler
* dZ = A - Y, dZ.shape = A.shape = Y.shape = (1, m)
* 重要建议:
  1. 勇于使用 reshape, 使之成为我们需要的维度, 要始终使用明确维度的行、列向量和 matrix;
  2. 绝不使用 a = np.random.randn(5), a.shape = (5,)这种"rank 1 array".因为这东西使用时不符合直觉;
  3. 应该用 a = np.random.randn(5,1) 或者 (1,5) 这种非常明确的列或行向量(very important)!
  4. 若出现2所示内容，解决办法是：a = a.reshape(5,1) 或者 (1,5)重新明确shape!;
  5. 要经常并随意使用 assert(a.shape == (5,1)) 这种断言;
  7. 要仔细检查我们的 matrix, vector的维度.

<font color = red>
自己的总结：
1. 先完成推导，明确输入输出以及哪些变量是已知的，哪些是待求的．
2. 写出程序伪代码．
3. 针对伪代码，逐条完成程序的 vectorize 过程. 这时要小心地，自输入开始地，维护好各种 vector, matrix 的维度, 必要时随需求，毫不犹豫地使用 reshape．
4. 上述第3条保证了程序中尽量地少使用 for loop.
5. 遵从 Andrew Ng 老师的上述建议，尤其是对 X, Y, A, w, b, dw, db, dZ 这些 vector, matrix 们的 shape 的把握．</font>


符合上述规则和自己的总结，编出个机器学习算法就很简单了．
我整合吴老师的课后作业，加了少许修改，做出 Logisitc Regression 算法的代码, 如下:

```python
# !/usr/bin/python
# -*- coding:utf-8 -*-


"""
Re-implement Logistic Regression algorithm as a practice
使用该 LR re-implement 的前提：
    Due to the binary classifier of LR
    The label of a sample must be as probability
    train data　的标签必须转成0,1的形式
"""

# Author: 相忠良(Zhong-Liang Xiang) <ugoood@163.com>
# Finished on September 23rd, 2017

import h5py
import numpy as np


def load_dataset():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def load_data():
    train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes = load_dataset()
    train_X = (train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T) / 255.  # flatten and divide 255
    test_X = (test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T) / 255.  # flatten and divide 255
    return train_X, train_set_y_orig, test_X, test_set_y_orig, classes


def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """

    s = 1.0 / (1 + np.exp(-z))
    return s


def init_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0.

    Argument:
    dim -- size of the w vector we want (or number of parameters in this case)

    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias)
    """

    w = np.zeros((dim, 1))
    b = 0
    assert (w.shape == (dim, 1))
    assert (isinstance(b, float) or isinstance(b, int))
    return w, b


def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)

    Return:
    cost -- negative log-likelihood cost for logistic regression
    dw -- gradient of the loss with respect to w, thus same shape as w
    db -- gradient of the loss with respect to b, thus same shape as b
    """

    # FORWARD PROPAGATION(FROM X TO COST)
    m = X.shape[1]  # 样本个数
    A = sigmoid(np.dot(w.T, X) + b)  # activation (1 * m)
    cost = (np.dot(np.log(A), Y.T) + np.dot(np.log(1 - A), (1 - Y).T)) / -m  # a scaler

    # BACKWARD PROPAGATION (TO FIND GRAD)
    dZ = A - Y  # (1 * m)
    dw = np.dot(X, dZ.T) / m  # (n_x, 1) n_x 是 样本的维度
    db = np.sum(dZ) / m  # a scaler

    # ASSERT
    assert (dw.shape == w.shape)
    assert (db.dtype == float)

    cost = np.squeeze(cost)  # 变成个数字
    assert (cost.shape == ())

    grads = {"dw": dw,
             "db": db}

    return grads, cost


def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost):
    """
    This function optimizes w and b by running a gradient descent algorithm

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of shape (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    print_cost -- True to print the loss every 100 steps

    Returns:
    params -- dictionary containing the weights w and bias b
    grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
    costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.
    """

    costs = []  # 将迭代过程中算出的cost收集起来

    for i in range(num_iterations):

        # Cost and gradient calculation
        grads, cost = propagate(w, b, X, Y)

        # Retrieve derivatives from grads
        dw = grads["dw"]
        db = grads["db"]

        # update dw, db
        w = w - learning_rate * dw
        b = b - learning_rate * db

        # Record the costs
        if i % 100 == 0:
            costs.append(cost)

        # Print the cost every 100 iterations
        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    params = {"w": w,
              "b": b}
    grads = {"dw": dw,
             "db": db}
    return params, grads, costs


class MyLogisticRegression:
    costs = []
    params = {}  # w, b
    grads = {}  # dw, db
    num_iterations = 0
    learning_rate = 0.
    print_cost = False

    def __init__(self, num_iterations=1000, learning_rate=0.01, print_cost=False):
        # 初始化超參數 num_iterations, learning_rate
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate
        self.print_cost = print_cost
        return

    def fit(self, X, Y):
        n_x = X.shape[0]  # dim of X
        w, b = init_with_zeros(n_x)  # initialize w,b with zeros,  w.shape=(n_x, 1), b=0 a scaler.

        # 前向传播获取cost,反向传播获取grads,并更新params．这种事情做了num_iterations次，学习率为learning_rate
        self.params, self.grads, self.costs = optimize(w, b, X, Y, self.num_iterations, self.learning_rate,
                                                       self.print_cost)
        # fit函数的结果是获取params.顺便得到了grads, costs, 便于我们查看并对costs画图，以检查时候模型学到了东西．

    def predict(self, X):
        m = X.shape[1]  # the number of samples
        Y_predict = np.zeros((1, m))  # initialize Y_predict
        w = self.params["w"]  # 获取已经训练好的 w
        b = self.params["b"]  # 获取已经训练好的 b
        A = sigmoid(np.dot(w.T, X) + b)  # 根据 训练好的w,b,计算 p(Y=1|X)

        # 将预测概率p(Y=1|X)转换为标签值，　大于0.5的标签值为１，否则为０
        for i in range(A.shape[1]):
            Y_predict[0, i] = 1 if A[0, i] > 0.5 else 0

        assert (Y_predict.shape == (1, m))
        return Y_predict

    def score(self, X, y):
        pass


## 测试用例
train_X, train_y, test_X, test_y, classes = load_data()
cls = MyLogisticRegression(num_iterations=2000, learning_rate=0.005, print_cost=True)

cls.fit(train_X, train_y)

Y_predict_test = cls.predict(test_X)
Y_predict_train = cls.predict(train_X)

print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_predict_train - train_y)) * 100))
print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_predict_test - test_y)) * 100))

"""
运行结果

/usr/bin/python2.7 /home/xiang/桌面/ML_Course_20170314/xiang_code/Xiang_ml_in_practice/MyLogisticRegression.py
Cost after iteration 0: 0.693147
Cost after iteration 100: 0.584508
Cost after iteration 200: 0.466949
Cost after iteration 300: 0.376007
Cost after iteration 400: 0.331463
Cost after iteration 500: 0.303273
Cost after iteration 600: 0.279880
Cost after iteration 700: 0.260042
Cost after iteration 800: 0.242941
Cost after iteration 900: 0.228004
Cost after iteration 1000: 0.214820
Cost after iteration 1100: 0.203078
Cost after iteration 1200: 0.192544
Cost after iteration 1300: 0.183033
Cost after iteration 1400: 0.174399
Cost after iteration 1500: 0.166521
Cost after iteration 1600: 0.159305
Cost after iteration 1700: 0.152667
Cost after iteration 1800: 0.146542
Cost after iteration 1900: 0.140872
train accuracy: 99.043062201 %
test accuracy: 70.0 %
"""

```
