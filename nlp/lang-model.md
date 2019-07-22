# 从语言模型到朴素贝叶斯

### 朴素贝叶斯

###### 贝叶斯公式

$$P(Y, X) = P(Y|X)P(X) = P(X|Y)P(Y)$$

Y="属于某类" X="具有某些特征"

sklearn.feature_extraction.text.CountVectorizer()

###### 举例：垃圾邮件判断

将垃圾邮件内容转换成词，判断垃圾邮件中含有这些词的概率。




