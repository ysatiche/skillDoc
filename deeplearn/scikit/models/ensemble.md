# ensemble 介绍

Gradient Tree Boosting或 Gradient Boosted Regression Trees(GBRT)是一个boosting的泛化表示，它使用了不同的loss函数。

优点：

1. 天然就可以处理不同类型的数据（=各种各样的features）
2. 预测能力强
3. 对空间外的异常点处理很健壮（通过健壮的loss函数）

sklearn.ensemble 通过GBRT提供分类与回归的功能。

