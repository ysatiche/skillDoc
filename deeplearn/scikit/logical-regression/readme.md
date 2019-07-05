# 逻辑回归

### 解决分类问题

普通的分类算法：$\hat{y} = f(x)$ 表示预测值

逻辑回归，先计算一个概率值。$\hat{p} = f(x)$ 


$$ \hat{y}=\left\{
\begin{aligned}
 1, \hat{p} >= 0.5 \\
 2, \hat{p} <= 0.5
\end{aligned}
\right.
$$

逻辑回归既可以看做是一个分类算法，也可以看作一个回归算法，一般用来做分类，且只能是二分类。

### Sigmoid函数

将从负无穷到正无穷的数映射到[0, 1]之间。

$$\hat{p} = \sigma(\theta^{T}x_{b}) = \frac{1}{1+e^{-\theta^{T}x_{b}}}$$

$$ \hat{y}=\left\{
\begin{aligned}
 1, \hat{p} >= 0.5 \\
 2, \hat{p} <= 0.5
\end{aligned}
\right.
$$

如何找到参数$\theta$拟合样本数据集？

损失函数。

$$ cost=\left\{
\begin{aligned}
 -log(\hat{p}), y = 1 \\
 -log(1-\hat{p}), y = 0
\end{aligned}
\right.
$$

$$J(\theta) = -\frac{1}{m}\sum_{i=1}^{m}y^{(i)}log(\sigma(X_{b}^{(i)}\theta))+(1-y^{(i)})log(1-\sigma(X_{b}^{(i)}\theta))$$

该损失函数是个凸函数，可以使用梯度下降法求解。

通过向量化，可得到损失函数

$$J(\theta) = $$

### 决策边界

$$\theta^{T} x_{b} = 0$$

### 逻辑回归添加多项式

### 正则化

$$C J(\theta) + L_{1}$$