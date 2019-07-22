# 集成学习

> hard voting 少数服从多数

> soft voting 权值

> 创建差异性

每一个子模型只看样本数据的一部分

放回取样（Bagging）不放回取样（pasting）

```
from sklearn.tree import DecisionTreeClassfier
from sklearn.ensemble import BaggingClassifier

bagging_clf = BaggingClassifier(DecisionTreeClassifier(),
n_estimators=500, max_sample=100,bootstrap=True)
```

> 返回取样的问题

大概平均有37%的样本没有取到(out of bag) oob_score_

> random subspaces


> random patches

即在行上随机采样，又在列上随机取样

> 随机森林

```

```

> extra-trees

决策树在节点划分上，使用随机的特征和随机的阈值

> ada boosting

不同的决策树是对之前决策树的修正（通过提高之前没有被覆盖的点的权重）

> gradient boosting


