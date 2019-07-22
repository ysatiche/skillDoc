# 决策树

```
from sklearn.tree import DecisionTreeClassifier

dt_clf = DecisionTreeClassifier(max_depth=2, entropy)
```

> 非参数学习算法，可以解决分类问题

### 信息熵

熵越大，数据的不确定性越高，熵越小，数据的不确定性越低

$$H = -\sum_{i=1}^{k}P_{i}log(p_{i})$$

### 使用信息熵寻找最优划分

TODO

```
def split(X, y, d, value):
  index_a = (X[:, d] <= value)
  index_b = (X[:, d] > value)
  return X[index_a], X[index_b], y[index_a], y[index_b]

def try_split(X,y):
  best_entropy = float('inf')
  best_d, best_v = -1, -1
  for d in range(X.shape[1]):
    sorted_index = np.argsort(X[:, d])
    for i in range(1, len(X)):
      v = (X[sorted_index[i-1], d] + X[sorted_index[i], d]) / 2
      X_l, X_r, y_l, y_r = split(X, y, d, v)
```

### 基尼系数

$$G = 1 - \sum_{i=1}^{k}p_{i}^{2}$$

### CART (二叉树)

降低复杂度，剪枝

