# 多元线性回归中的梯度下降

> 损失函数

$$J=\sum_{i=1}^{m}(y^{(i)} - \hat{y}^{(i)})^{2}$$

$y^{(i)}$表示真实值，$\hat{y}^{(i)}$表示预测值

> 初始点

由于是多元函数，所以每个影响因子组合起来，初始点是个矩阵。

$${\theta}= ({\theta}_{0}, {\theta}_{1}...{\theta}_{n})$$

> 对每个因子的学习率为

$$-{\eta}\frac{dJ}{d{\theta}}=-{\eta}{\nabla}J$$

$${\nabla}J = (\frac{dJ}{d{\theta_{0}}}, \frac{dJ}{d{\theta_{1}}},...,\frac{dJ}{d{\theta_{n}}})$$

其实就是对每一个变量求偏导数

> 下方是一个二元线性梯度下降的示意图

![二元线性梯度下降](img/multiple-linear-regression-1.png)

$z=x^{2} + 2*y^{2}$是损失函数，从外到里，z的值越来越小

> 多元线性梯度下降的目标

使 $J=\sum_{i=1}^{m}(y^{(i)} - \hat{y}^{(i)})^{2}$ 取值最小，其中$\hat{y}^{(i)}={\theta}_{0} + {\theta}_{1}*X_{1}^{(i)} + {\theta}_{2}*X_{2}^{(i)} + ...+ + {\theta}_{n}*X_{n}^{(i)}$

对${\theta}$求梯度值，如下：
$${\nabla}J = (\frac{dJ}{d{\theta_{0}}}, \frac{dJ}{d{\theta_{1}}},...,\frac{dJ}{d{\theta_{n}}}) = \begin{pmatrix}\sum_{i=1}^{m}2(y^{(i)} - X_{b}^{(i)}{\theta})(-X_{0}^{(i)})\\\\\sum_{i=1}^{m}2(y^{(i)} - X_{b}^{(i)}{\theta})(-X_{1}^{(i)})\\\\...\\\\\sum_{i=1}^{m}2(y^{(i)} - X_{b}^{(i)}{\theta})(-X_{n}^{(i)})\end{pmatrix}$$

$${\nabla}J = \frac{2}{m}\begin{pmatrix}\sum_{i=1}^{m}2(X_{b}^{(i)}{\theta} - y^{(i)})(X_{0}^{(i)})\\\\\sum_{i=1}^{m}(X_{b}^{(i)}{\theta} - y^{(i)})(X_{1}^{(i)})\\\\...\\\\\sum_{i=1}^{m}(X_{b}^{(i)}{\theta} - y^{(i)})(X_{n}^{(i)})\end{pmatrix} = \frac{2}{m} {\cdot}(X_{b}^{(1)}{\theta} - y^{(1)}, X_{b}^{(2)}{\theta} - y^{(2)}, ..., X_{b}^{(m)}{\theta} - y^{(m)}){\cdot}\begin{pmatrix}X_{0}^{(1)} & X_{1}^{(1)} & ... & X_{n}^{(1)}\\\\X_{0}^{(2)} & X_{1}^{(2)} & ... & X_{n}^{(2)}\\\\... & ... & ... & ...\\\\X_{0}^{(m)} & X_{1}^{(m)} & ... & X_{n}^{(m)}\end{pmatrix}$$

$${\nabla}J = \frac{2}{m}{\cdot}(X_{b}{\theta} - y)^{T}{\cdot}X_{b}$$

$X_{b}$是一个 m * (n+1) 维的矩阵


## 随机梯度下降法

> 学习率

$$\eta = \frac{a}{i\_items + b}$$

${i\_items}$表示学习次数

$b$ 一般设置为50，以防下降过快

$a$ 可以设置为5

<font color=orange>模拟退火？</font>






