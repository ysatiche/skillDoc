from sklearn.datasets import load_boston
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

boston = load_boston()
boston_X = boston.data
boston_Y = boston.target

poly = PolynomialFeatures()
boston_X = poly.fit_transform(boston_X)

X_train, X_test, y_train, y_test = train_test_split(boston_X, boston_Y, test_size=0.3)

linearRegression = LinearRegression()
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
linearRegression.fit(X_train, y_train)
y_predict = linearRegression.predict(X_test)
# print(y_test.shape)
print(linearRegression.score(X_test, y_test))

