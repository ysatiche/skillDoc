import numpy as np

class LinearRegression:
  def __init__(self):
    self.coef = None
    self.interception = None
    self._theta = None

  def fit_normal(self, X_train, y_train):
    assert X_train.shape[0] == y_train.shape[0]

    X_b = np.hstack([np.ones(X_train.shape[0], 1)], X_train)
    self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
    self.interception = self._theta[0]
    self.coef = self._theta[1:]
    return self

  def fit_gd(self, X_train, y_train, eta=0.01, n_iters=1e4):
    def J(theta, X_b, y):
      try:
        return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
      except:
        return float('inf')

    def dJ(theta, X_b, y):
      return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

    def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e8):
      theta = initial_theta
      cur_iter = 0

  def predict(self, X_predict):
    X_b = np.hstack([np.ones(X_predict.shape[0], 1)], X_predict)
    return X_b.dot(self._theta)
  # R Square误差
  