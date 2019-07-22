# svm(support vector machine)

### svm思想

> 不适定问题（决策边界不唯一）

> svm

让决策边界离左右两边最靠近的点尽可能的一致，保证泛化能力。svm最大化margin(hard margin svm)

### 如何用数学最大化margin

> 点到直线的距离

$(x, y)$ 到 $Ax + By + C = 0$的距离 $\frac{|Ax + By + C|}{\sqrt{A^{2}+B^{2}}}$

拓展到N维空间，$\theta^{T}x_{b} = 0 => w^{T}x + b = 0$

$$\frac{|w^{T}x+b|}{||w||} ||w|| = \sqrt{w_{1}^{2} + ...+ w_{i}^{2}}$$

支撑向量机满足的表达式$y^{(i)}(w^{T}x^{(i)} +b) >= 1$,在此条件上，最小化损失函数$min\frac{1}{2}||w||^{2}$

> 有条件的最优化和全局最优化问题

拉布拉斯算子

### soft margin 和 svm 的正则化

> hard margin svm

$$min\frac{1}{2}||w||^{2}$$

$$s.t. y^{(i)}(w^{T}x^{(i)} + b) >= 1$$

> soft margin svm

L1正则：
$$min\frac{1}{2}||w||^{2} + C\sum_{i=1}^{m}\eta_{i}$$

L2正则：
$$min\frac{1}{2}||w||^{2} + C\sum_{i=1}^{m}\eta_{i}^{2}$$

$$s.t. y^{(i)}(w^{T}x^{(i)} + b) >= 1 - \eta$$

### scikit svm

> 数据标准化

### svm使用多项式特征

> 多项式核函数的SVM

```
def PolynomiaKernelSVC(degree, C=1.0):
  return Pipeline([
    ('std_scaler', StandardScaler()),
    ('kernerSVC', SVC(kernel='poly', degree=degree, C=C))
  ])

poly_kernel_svc = PolynomiaKernelSVC(degree=3)
poly_kernel_svc.fit(X, y)
```

$$min\frac{1}{2}||w||^{2} + C\sum_{i=1}^{m}\eta_{i}$$
$$s.t. y^{(i)}(w^{T}x^{(i)} + b) >= 1 -\eta$$

$$=>$$

$$max\sum_{i=1}^{m}a_{i} - \frac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}a_{i}a_{j}y_{i}y_{j}x_{i}x_{j}$$

$$s.t. 0<=a_{i}<=C \sum_{x=i}^{m}a_{i}y_{i} =0$$

> 核函数

$$max\sum_{i=1}^{m}a_{i} - \frac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}a_{i}a_{j}y_{i}y_{j}K(x_{i}, x_{j})$$

$$s.t. 0<=a_{i}<=C \sum_{x=i}^{m}a_{i}y_{i} =0$$

存在$x_{i}x_{j}$这种式子都可以用核函数

$$K(x,y) = (xy +c)^{d}$$

> 高斯核函数(RBF核)

$$K(x, y) = e^{-\eta||x-y||^{2}}$$

> 多项式特征

依靠升维使得原来线性不可分的数据线性可分