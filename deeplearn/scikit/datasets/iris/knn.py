from sklearn.datasets import load_iris
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


iris = load_iris()
iris_X = iris.data
iris_Y = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_Y, test_size=0.3)

# knn
# knn = KNeighborsClassifier()
# scores = cross_val_score(knn, iris_X, iris_Y, cv=3, scoring='accuracy')
# k_range = range(2, 10)
# k_scores = []
# print(scores.mean())
# for k in k_range:
#     scores = cross_val_score(knn, iris_X, iris_Y, cv=k, scoring='accuracy')
#     k_scores.append(scores.mean())

# plt.plot(k_range, k_scores)
# plt.show()


# pca
pca = PCA(n_components=2)
pca.fit(X_train)
print(X_train.shape)
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)
print(X_train_reduction.shape)
knn = KNeighborsClassifier()
knn.fit(X_train_reduction, y_train)
print(knn.predict(X_test_reduction))
print(y_test)
