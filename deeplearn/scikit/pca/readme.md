# 主成分分析

> 特点

1. 非监督的机器学习
2. 用于数据的降维，去燥

> 过程

1. demean处理，将每个数据减去均值
2. 样本映射到轴的方向 $w = (w1, w2)$
$$Var(X_{project}) = \frac{1}{m}\sum_{i=1}^{m}(X_{project}^{(i)} - \bar{X}_{project})^{2} = \frac{1}{m}\sum_{i=1}^{m}||X^{(i)} w||^{2}$$

> 数学推导（梯度上升法）

目标函数


> scikt中的pca

```
pca = PCA(n_components=2)
pca.fit(X_train)
X_train_reduction = pca.transform(X_train)
```

pca中有个参数表示降到多少维合适
```
pca.explained_variance_ratio_
```
假设 `n_components=2`, 则 `pca.explained_variance_ratio_` 返回的值为一个两个元素的数组，假设值为 `(1.08e-02, 2.03e-04)` 每一个值代表的是当前维度对于总的数据的解释程度的占比。当两者相加太小时，说明  `n_components` 取值过低，需要添加新维度。我们可以通过如下方式，可视化占比

```
plt.plot([i for i in range(X_train.shape[1])], [np.sum(pca.explained_variance_ratio_[:i + 1]) for i in range(X_train.shape[1])])
plt.show()
```

所以，选择当 `n_components` 变大时，y轴没有明显上升时的数值，可以保证准确度和效率都比较优。

可以在初始化时，初始化解释精度
```
pca = PCA(0.95)
pca.fit(X_train)
```

> mnist数据集

从官方网站下载数据集

```
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')
```

> 降噪

```
pca.transform
pca.inverse_transform
```


> 思考

1. 为啥需要单位向量。
2. PCA怎么知道那几个变量是相关的呢？
3. PCA得到第一主成分时，如何去除相关变量