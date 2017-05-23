# -*- coding: utf-8 -*-
# scikit-learn的五种机器学习方法使用案例(python 代码)

import numpy as np
import urllib
import warnings
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Ridge
from sklearn.grid_search import GridSearchCV
from sklearn.grid_search import RandomizedSearchCV
from scipy.stats import uniform as sp_rand


# ignore warning information
warnings.filterwarnings("ignore")

# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# download the file
raw_data = urllib.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
# separate the data from the target attributes
X = dataset[:, 0:7]
y = dataset[:, 8]

# normalize the data attributes
normalized_X = preprocessing.normalize(X, norm='l2')
# standardize the data attributes
standardized_X = preprocessing.scale(X)

# feature selection
model = ExtraTreesClassifier()
model.fit(X, y)
# display the relative importance of each attribute
print(model.feature_importances_)
print model.feature_importances_[:].sum()  # summarized into 1

# Logistic Regression
model = LogisticRegression()
model.fit(X, y)
print model
# make predictions
y_true = y
y_pred = model.predict(X)
# summarize the fit of the model
print metrics.classification_report(y_true, y_pred)
print metrics.confusion_matrix(y_true, y_pred)

# Naive Bayes
model = GaussianNB()
model.fit(X, y)
print model
# make predictions
y_true = y
y_pred = model.predict(X)
# summarize the fit of the model
print metrics.classification_report(y_true, y_pred)
print metrics.confusion_matrix(y_true, y_pred)
print (429 + 160) / (108.0 + 160.0 + 429.0 + 71.0)

# K-neighborhood
# She usually is regarded as a part of other classifications.
# We can use her for feature selection.

model = KNeighborsClassifier()
model.fit(X, y)
print model
y_true = y
y_pred = model.predict(X)
print metrics.classification_report(y_true, y_pred)
print metrics.confusion_matrix(y_true, y_pred)

# Classification and Regression Trees, CART
model = DecisionTreeClassifier()
model.fit(X, y)
y_true = y
y_pred = model.predict(X)
print model
print metrics.classification_report(y_true, y_pred)
print metrics.confusion_matrix(y_true, y_pred)

# SVM
# SVM是非常流行的机器学习算法，主要用于分类问题，如同逻辑回归问题，
# 它可以使用一对多的方法进行多类别的分类。

model = SVC()
model.fit(X, y)
y_true = y
y_pred = model.predict(X)
print model
print metrics.classification_report(y_true, y_pred)
print metrics.confusion_matrix(y_true, y_pred)

# 应用 GridSearchCV 寻找最佳参数
# 下面的例子是针对 Ridge 回归， 为l2正则项选择最合适的 alpha

# prepare a list of alpha values to test
alphas = np.array([1, 0.1, 0.01, 0.001, 0.0001, 0.5, ])
# create and fit a Ridge regression model, testing each alpha
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))
grid.fit(X, y)
y_true = y
y_pred = grid.predict(X)
print grid
print 'best score:  ', grid.best_score_
print 'best alpha:  ', grid.best_estimator_.alpha
print 'best params:  ', grid.best_params_
# print "alpha = 1, 0.282118955686 "


# 有时随机从给定区间中选择参数是很有效的方法，
# 然后根据这些参数来评估算法的效果进而选择最佳的那个。
# prepare a uniform distribution to sample for the alpha parameter
param_grid = {'alpha': sp_rand()}
# create and fit a ridge regression model, testing random alpha values
model = Ridge()
rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100)  # 找100个 param samples
rsearch.fit(X, y)
print(rsearch)
# summarize the results of the random parameter search
print(rsearch.best_score_)
print(rsearch.best_estimator_.alpha)
print rsearch.best_params_