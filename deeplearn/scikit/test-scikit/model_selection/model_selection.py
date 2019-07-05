import numpy as np
# 划分数据集
def train_test_split(X, y, test_radio=0.5, seed=None):
  assert X.shape[0] == y.shape[0]
  assert 0 < test_radio < 1

  if seed:
    np.random.seed(seed)
  # 打乱元素顺序
  shuffled_indexes = np.random.permutation(len(X))

  dataLen = int(X.shape[0] * test_radio)
  test_indexes = shuffled_indexes[:dataLen]
  train_indexes = shuffled_indexes[dataLen:]

  X_train = X[train_indexes]
  y_train = y[train_indexes]

  X_test = X[test_indexes]
  y_test = y[test_indexes]
  return X_train, y_train, X_test, y_test

# 数据归一化