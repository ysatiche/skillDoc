# 多项式回归

将 $y = ax^{2} + bx + c$ 这个二次方程理解成两个变量 $x^{2}$ 和$x$ 的多项式方程

如果单纯以 linearRegression 来fit数据的话，会出现以直线来描绘曲线的场景，所以我们得向上述所说的添加一个特征。构造 $x^{2}$ 的数据。

# scikit-learn 中的多项式回归

```
from sklearn.preprocessing import PolynomiaFeatures

poly = PolynomiaFeatures(degree=2)
poly.fit(X)
X2 = poly.transform(X)
```

> pipeline 顺序执行

```
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

poly_req = Pipeline([
  ('poly', PolynomialFeatures(degress=2)),
  ('std_scalar', StandardScalar()),
  ('lin_req', LinearRegression())
])

poly_req.fit(X, y)
```

# 过拟合，欠拟合


# 偏差方差权衡

模型误差 = 偏差（bias）+ 方差（variance）+不可避免的误差

有一些算法天生就是高方差的算法，如KNN

非参数学习通常都是高方差的算法，因为不对数据进行任何假设

有一些算法天生就是高偏差的算法，如线性回归

参数学习通常都是高偏差算法，因为堆数据具有极强的假设

> 如何解决方差

1. 降低模型复杂度
2. 降噪，降低数据维度
3. 增加样本数量
4. 使用交叉验证


# 模型正则化

> 岭回归

目标：使 $J(\theta) = MSE(y, \hat{y};\theta) + a\frac{1}{2}\sum_{i=1}^{n}\theta_{i}^{2}$尽可能小

> lasso

目标：使 $J(\theta) = MSE(y, \hat{y};\theta) + a\frac{1}{2}\sum_{i=1}^{n}|\theta_{i}|$尽可能小

lasso趋向与使一部分theta值为0，所以lasso可以作为特征选择用

> L1正则，l2正则

> 弹性网

$$J(\theta) = MSE(y, \hat{y};\theta) + ra\frac{1}{2}\sum_{i=1}^{n}|\theta_{i}| + \frac{1-r}{2}a\frac{1}{2}\sum_{i=1}^{n}\theta_{i}^{2}$$


# 总结

> Ridge

$$\frac{1}{2}\sum_{i=1}^{n}\theta_{i}^{2}$$

> lasso

$$\frac{1}{2}\sum_{i=1}^{n}|\theta_{i}|$$

> MSE

$$\frac{1}{n}\sum_{i=1}^{n}(y_{i} - \hat{y}_{i})^2$$

> MAE

$$\frac{1}{n}\sum_{i=1}^{n}|y_{i} - \hat{y}_{i}|$$

> 欧拉距离

$$\sqrt{\sum_{i=1}^{n}(x_{i}^{(1)} - {x}_{i}^{(2)})^2}$$

> 曼哈顿距离

$$\sum_{i=1}^{n}|x_{i}^{(1)} - {x}_{i}^{(2)}|$$

