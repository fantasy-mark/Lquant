### 利用生成器返回DataFrame元素

```python
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.DataFrame([[18, 'male'], [16, 'female']], index=['mark', 'sophie'], columns=['age', 'sex'])

def show(df):
    for columns in df:
        for item in df[columns]:
            yield item

list(show(df.T))
```




    [18, 'male', 16, 'female']





### 注意参数如何传入, super函数的写法, 利用getattr动态调用函数



```python
# -*- coding: utf-8 -*-

class Tortoise:
    # 先填无星参数的坑, * 收集剩余的位置参数, ** 收集剩余的关键字参数, 详见P99
    def callback(self, prefix, attr, *args):
        method = getattr(self, prefix+attr, None)
        if callable(method): return method(*args)

    def iget(self, attr, *args):
        return self.callback('get_', attr, *args)
    
    def iset(self, attr, *args):
        return self.callback('set_', attr, *args)

class Turtle(Tortoise):
    def __init__(self):
        super(Turtle, self).__init__()
        self.data = 0.0
    def get_age(self, name, df):
        index = {'mark':0,'sophie':1}[name]
        self.data = df.iat[index, 0]
        return self.data
    def get_sex(self, name, df):
        index = {'mark':0,'sophie':1}[name]
        self.data = df.iat[index, 1]
        return self.data
        
    def set_age(self, name, value, df):
        index = {'mark':0,'sophie':1}[name]
        df.iat[index,0] = value
    def set_sex(self, name, value):
        index = {'mark':0,'sophie':1}[name]
        df.iat[index,1] = value

A = Turtle()
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mark</th>
      <td>12</td>
      <td>male</td>
    </tr>
    <tr>
      <th>sophie</th>
      <td>16</td>
      <td>female</td>
    </tr>
  </tbody>
</table>
</div>




```python
A.iset('age', 'mark', 12, df)
```


```python
A.iget('age', 'mark', df)
```




    12




```python

```
