import numpy as np
import matplotlib.pyplot as plt

plot_x = np.linspace(-1, 6, 141)
# 损失函数是个二次函数，比较常见的情况
plot_y = (plot_x - 2.5)**2 - 1 

# 对J函数求导，计算损失函数
# 参数 theta 指的是当前值对应的损失函数，类似于 x
def dJ(theta):
  try:
    return 2 * (theta - 2.5)
  # 如果有问题，返回浮点数最大值
  except:
    return float('inf')

# 当前 theta 对应的最终值
def J(theta):
  return (theta - 2.5)**2 - 1

# 学习率
eta = 0.1
# 满足条件的最小误差
epsilon = 1e-8
# 初始点
theta = 0.0

def gradient_descent(initial_theta, eta, n_iters = 1e4, epsilon=1e-8):
  theta = initial_theta
  i_iter = 0
  # 开始梯度下降
  while i_iter < n_iters:
    # 获取当前theta的斜率
    gradient = dJ(theta)
    # 储存上一次theta值
    last_theta = theta
    # 得到下一次测试的新theta值
    theta = theta - eta * gradient

    # 当上一次theta与这次theta的J值之差小于epsilon，即斜率趋向0
    if (abs(J(theta) - J(last_theta)) < epsilon):
      break

    i_iter += 1

print(theta)
print(J(theta))





