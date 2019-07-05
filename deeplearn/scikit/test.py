import numpy as np
# from sklearn import datasets
from sklearn.model_selection import train_test_split, learning_curve, cross_val_score, validation_curve, cross_val_predict
# from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, linear_model
# from sklearn.datasets.samples_generator import make_classification
# from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits, load_boston


# 对 load_boston 进行线性回归
boston = load_boston()
boston_X = boston.data
boston_y = boston.target
# X_train, X_test, y_train, y_test = train_test_split(boston_X, boston_y, test_size=0.3)

# lr = linear_model.LinearRegression()

# cross_val_predict方式
# predicted = cross_val_predict(lr, boston_X, boston_y, cv=10)
# fig, ax = plt.subplots()
# ax.scatter(boston_y, predicted, edgecolors=(0, 0, 0))
# ax.plot([boston_y.min(), boston_y.max()], [predicted.min(), predicted.max()], 'k--', lw=4)
# test = [boston_y.min(), boston_y.max()]
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()

# cross_val_score方式
# loss = -cross_val_score(lr, boston_X, boston_y, cv=10, scoring='neg_mean_squared_error')
# print(loss.mean())

# ensemble方式回归数据








