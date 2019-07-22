# nlp基本处理

### 字符串操作

> 去空格

```
s = ' hello world!'
print(s.strip())
print(s.lstrip(' hello'))
print(s.rstrip())
```

> 查找字符

```
str = 'street'
strKey = 's'
pos = str.index(strKey)
```

> 比较字符串

```
str1 = 'strchr'
str2 = 'strch'
## 下面两个结果不一样
print(cmp(str1, str2))
print(cmp(str2, str1))
```

> 大小写

```
str.upper()
str.lower()
```

> 翻转字符串

```
str = str[::-1]
```

> 查找字符串

```
str.find(strKey)
```

### 正则表达式

> 练习网址

https://alf.nu/RegexGolf

> 学习网址

https://regexr.com/

> python中使用正则

```
#encoding: UTF-8
import re

# 将正则表达式编译成pattern对象
pattern = re.compile(r'hello.*\!')

# 使用pattern匹配文本，将得到匹配结果，无法匹配的返回None
match = pattern.match('hello, hanxiaoyang! how are you.')

if match:
  print(match.group())

# re.compile(pattern, flag) flag 可选
```

```
import re

p = re.compile(r'\d+')
print(p.split('one1two2three3))
# ['one','two','three','']
```

### 结巴分词

> 基本用法

```
import jieba

seg = jieba.cut('我在学习自然语言处理', cut_all=True)
### seg = ['我', '在', '学习','自然','自然语言','语言','处理']
seg = jieba.cut('我在学习自然语言处理', cut_all=False)
### seg = ['我', '在', '学习','自然语言','处理']
### 如果有词包的话结果不一样

```

> 用户自定义词典

1, 可以用jieba.load_userdict(file_name)加载用户字典
2, 少量词汇可以手动添加(用add_word(word, freq=None, tag=None)或suggust_freq(segment, tune=True))

> 基于 TF-IDF算法的关键词抽取

```
import jieba.analysis
### allowPOS为返回词的词性
jieba.analysis.extract_tags(sentence, topK=20, withWeight=False, allowPOS={})
```

关键词停用词(stop_words)

> 基于textrank算法的关键词抽取

> 词性标注

```
import jieba.posseg as pseg

```

> 并行分词

```
import sys
import time
import jieba

## windows不一样能跑
jieba.enable_parallel()
jieba.diable_parallel()
```
### 其他分词系统

收费的 http://ictclas.nlpir.org/ 分词效率高 https://github.com/NLPIR-team/NLPIR

百度 https://github.com/baidu/lac