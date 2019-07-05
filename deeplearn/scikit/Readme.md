## 机器学习的模块

scikit-learn module https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

#### Regression

> SDG Regressor 随机梯度下降

在 large-scale learning （大规模学习）方面 SGD 获得了相当大的关注

> Lasso

Lasso 是估计稀疏系数的线性模型，它在一些情况下是有用的，因为它倾向与使用较少参数值的情况，有效的减少给定解决方案所依赖变量的数量。

> Elastic-Net 弹性网络

弹性网络时一种使用L1，L2范数作为先验证正则项训练的线性回归模型，这种组合允许学习到一个只有少量参数是非零稀疏的模型，就像 Lasso 一样，但是它仍然保持像 Ridge 的正则性质，我们可利用 L1_ratio 参数控制l1,l2的凸组合

> Ridge Regression

Ridge 回归通过对系数的大小施加惩罚来解决 普通最小二乘法 的一些问题。

> LinearSVR 

支持向量回归

> ensembleRegression



> 待续

#### datasets

https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets

#### 交叉验证

将数据更加随机化分散为训练集和测试集，使验证结果更加准确.

## 中文api

http://sklearn.apachecn.org/#/

