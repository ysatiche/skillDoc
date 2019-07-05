import numpy as np
import matplotlib.pyplot as plt

x = 2 * np.random.random(size=100)

y = x * 3. + 4. + np.random.normal(size=100)

X = x.reshape(-1, 1)

# 对J函数求导，计算损失函数
# 参数 theta 指的是当前值对应的损失函数，类似于 x
def dJ(theta, X_b, y):
  # res = np.empty(len(theta))
  # res[0] = np.sum(X_b.dot(theta) - y)
  # for i in range(1, len(theta)):
  #   res[i] = (X_b.dot(theta) - y).dot(X_b[:, i])
  # return res * 2 / len(X_b)
  return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

# 当前 theta 对应的最终值
def J(theta, X_b, y):
  try:
    return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
  except:
    return float('inf')

def gradient_descent(X_b, y, initial_theta, eta, n_iters = 1e4, epsilon=1e-8):
  theta = initial_theta
  i_iter = 0
  # 开始梯度下降
  while i_iter < n_iters:
    # 获取当前theta的斜率
    gradient = dJ(theta, X_b, y)
    # 储存上一次theta值
    last_theta = theta
    # 得到下一次测试的新theta值
    theta = theta - eta * gradient

    # 当上一次theta与这次theta的J值之差小于epsilon，即斜率趋向0
    if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
      break

    i_iter += 1
  return theta

# 随机梯度下降法
def dJ_sgd(theta, X_b_i, y_i):
  return X_b_i.T.dot(X_b_i.dot(theta) - y_i) * 2.

# 随机梯度下降法
def sgd(X_b, y, initial_theta, n_iters):
  t0 = 5
  t1 = 50
  theta = initial_theta
  def learning_rate(t):
    return t0 / (t + t1)
  # 损失函数不能保证一直在减小的
  for cur_iter in range(n_iters):
    rand_i = np.random.randint(len(X_b))
    gradient = dJ_sgd(theta, X_b[rand_i], y[rand_i])
    theta = theta - learning_rate(theta) * gradient

  return theta

# 学习率
eta = 0.01

# 批量梯度下降法
# X_b = np.hstack([np.ones((len(x), 1)), x.reshape(-1, 1)])
# initial_theta = np.zeros(X_b.shape[1])
# print(initial_theta)

# theta = gradient_descent(X_b, y, initial_theta, eta)

# print(theta)

# 随机梯度下降法
X_b = np.hstack([np.ones((len(X), 1)), X])
initial_theta = np.zeros(X_b.shape[1])
theta = sgd(X_b, y, initial_theta, n_iters=len(X_b)//2)

print(theta)





