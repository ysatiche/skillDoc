import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, learning_curve, cross_val_score, validation_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits




# 第一个例子，简单介绍了sklearn中模型的用法
# iris = datasets.load_iris()
# iris_X = iris.data 
# iris_Y = iris.target

# X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_Y, test_size=0.3)
# print(X_test.shape)
# knn = KNeighborsClassifier()
# knn.fit(X_train, y_train)

# print(knn.predict(X_test))
# print(y_test)


# 第二个例子，数据标准化处理

# a = np.array([
#   [10, 2.7, 3.6],
#   [-100, 5, -2],
#   [120, 20, 40]
# ], dtype=np.float64)

# print(a)
# print(preprocessing.scale(a))


# 第三个例子，使用 SVC 模型

# 生成数据
# X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
                      # random_state=22, n_clusters_per_class=1, scale=100)
# 标准化数据, 把这行去掉，会降低很多验证精度
# X = preprocessing.scale(X)
# 划分数据
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
# 实例化SVC模型
# clf = SVC()
# 训练模型
# clf.fit(X_train, y_train)
# 验证
# print(clf.score(X_test, y_test))

# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

# 第四个例子，交叉验证 -- 数据集的优化

# iris = datasets.load_iris()
# iris_X = iris.data 
# iris_Y = iris.target
# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(knn, iris_X, iris_Y, cv=5, scoring='accuracy')
# print(scores.mean())

# 第五个例子，交叉验证 -- KNeighborsClassifier中参数的优化

# iris = datasets.load_iris()
# iris_X = iris.data 
# iris_Y = iris.target
# k_range = range(1, 31)
# k_scores = []
# for k in k_range:
#   knn = KNeighborsClassifier(n_neighbors=k)
#   loss = -cross_val_score(knn, iris_X, iris_Y, cv=10, scoring='neg_mean_squared_error') # for regression
#   scores = cross_val_score(knn, iris_X, iris_Y, cv=10, scoring='accuracy') # for clasification
#   # k_scores.append(scores.mean()) # for clasification
#   k_scores.append(loss.mean()) # for regression

# plt.plot(k_range, k_scores)
# plt.show()

# 第6个例子  过拟合

# digits = load_digits()
# X = digits.data
# y = digits.target

# # 学习率曲线 learning_curve是展示不同数据量，算法学习得分 
# train_sizes, train_loss, test_loss = learning_curve(SVC(gamma=0.001), X, y, cv=10, scoring='neg_mean_squared_error',
#     train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
# train_loss_mean = -np.mean(train_loss, axis=1)
# test_loss_mean = -np.mean(test_loss, axis=1)

# plt.plot(train_sizes, train_loss_mean, 'o-', color='r', label='Training')
# plt.plot(train_sizes, test_loss_mean, 'o-', color='g', label='Cross-validation')
# plt.xlabel('training example')
# plt.ylabel('loss')
# plt.legend(loc='best')
# plt.show()


# 第7个例子  参数

# digits = load_digits()
# X = digits.data
# y = digits.target
# param_range = np.logspace(-6, -2.3, 5)
# # validation_curve是展示某个因子，不同取值的算法得分
# train_loss, test_loss = validation_curve(SVC(), X, y, param_name='gamma', param_range=param_range, cv=5, scoring='neg_mean_squared_error')
# train_loss_mean = -np.mean(train_loss, axis=1)
# test_loss_mean = -np.mean(test_loss, axis=1)

# plt.plot(param_range, train_loss_mean, 'o-', color='r', label='Training')
# plt.plot(param_range, test_loss_mean, 'o-', color='g', label='Cross-validation')
# plt.xlabel('gamma')
# plt.ylabel('loss')
# plt.legend(loc='best')
# plt.show()