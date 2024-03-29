# 矩阵基础知识

> 坐标

> 向量

> 行列式

> 矩阵

# 行列式

### n阶行列式

克莱姆法则（n阶线性方程组的解）

未知量的个数和所含方程的个数相等的n元线性方程组

$$a_{11}x_{1} + a_{12}x_{2} + ... + a_{1n}x_{n} = b_{1}$$
$$a_{21}x_{1} + a_{22}x_{2} + ... + a_{2n}x_{n} = b_{2}$$
$$.......$$
$$a_{n1}x_{1} + a_{n2}x_{2} + ... + a_{nn}x_{n} = b_{n}$$

如果其系数行列式
$$D = \begin{vmatrix}a_{11} & a_{12} & ... & a_{1n}\\\\a_{21} & a_{22} & ... & a_{2n}\\\\... & ... & ... & ...\\\\a_{n1} & a_{n2} & ... & a_{nn}\end{vmatrix} \neq 0$$

该方程组有解且解唯一
$$x_{1} = \frac{D_{1}}{D}, x_{2} = \frac{D_{2}}{D},...,x_{n} = \frac{D_{n}}{D}$$

其中$D_{j}(j=1,2,...,n)$是将D中第j列的元素用方程组右端的常数项替换后而得到的阶行列式。

以上计算公式也称为n元线性方程组的公式解．
注意，克莱姆法则中的条件有两个：
1. 方程组中未知量的个数等于方程的个数；
2. 系数行列式不为零．

# 矩阵

矩阵与行列式的关系类似于向量与向量的模之间的关系。

### 初等矩阵

### python中矩阵的运算

$a * b$ $(a, b)$都为矩阵，结果为两个矩阵对应项相乘后得到的新矩阵。所以两个矩阵的shape必须一样。

$a.dot(b)$ $(a, b)$都为矩阵,结果为矩阵的点乘，$a.shape[1] == b.shape[0]$

### 矩阵的秩与正交化

# 向量

### 向量的运算

> 点乘

结果是个标量，是一个向量在另一个向量上的投影。

> 叉乘

结果是个向量，垂直于前两个向量。

> 向量的模

