# 概念简介

> 损失函数

损失函数是用来估量模型的预测值与真实值的不一致程度，它是一个非负实值函数，通常用 L(Y, f(x))来表示，损失函数越小，模型的鲁棒性越好。当参数影响的损失函数值最小时，即损失函数与参数的关系表达式的一阶导数为0时（可能是局部最优）

> 梯度下降法

梯度下降法是一种基于搜索的最优化方法，作用是<font color=#D4B51B>最小化一个损失函数</font>。梯度上升法是最大化一个效用函数。

> 学习率


$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$