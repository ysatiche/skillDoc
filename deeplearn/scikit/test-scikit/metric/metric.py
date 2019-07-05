# 预测准确度
def accuracy_score(y_true, y_predict):
  assert y_predict.shape[0] == y_true.shape[0]

  return sum(y_predict == y_true) / len(y_predict)

# 均方根误差 RMSE(Root Mean Squared Error)

# 平均绝对误差 MAE(Mean Absolute Error)

# R Squared