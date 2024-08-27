import datetime

import numpy as np
import pandas as pd
import random


"""
#simple example
#使用pandas进行分组求和
N = 1000000
uniques_keys = [pd.util.testing.rands(3) for i in range(200)]   #有错
keys = [random.choice(uniques_keys) for i in range(N)]
values = np.random.rand(N).tolist()
vs = pd.Series(values)
ks = pd.Series(keys)
dt = datetime.datetime.now()
print(vs.groupby(ks, sort=False).sum())
tend = datetime.datetime.now() - dt
print("Pandas program running time:", tend.total_seconds()*1000, "毫秒")


s1 = pd.Series([75, 90, 61])
print(s1)

s2 = pd.Series([75, 90, 61], index=['张三', '李四', '王五'])  #指定index数组
print(s2)

#通过字典创建Series对象
data = {'张三':75, '李四':90, '陈五':61}
s3 = pd.Series(data)
print(s3)

#显式指定index，若字典内容不存在，则使用NaN填充
data = {'张三':75, '李四':90, '陈五':61}
s3 = pd.Series(data, index=['小明', '李四', '陈五'])
print(s3)

#series前者是data，后者是index
#根据index来计算，无法计算的使用NaN填充
sr1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
sr2 = pd.Series([1, 5, 8, 9], ['a', 'c', 'e', 'f'])
print(sr2 - sr1)

#创建DataFrame对象
df1 = pd.DataFrame([
    pd.Series(['张三', '一班', 91, 71, 80], index=['Name', '班级', '语文', '数学', '英语']),
    pd.Series(['李四', '一班', 91, 71, 80], index=['Name', '班级', '语文', '数学', '英语']),
    pd.Series(['王五', '一班', 91, 71, 80], index=['Name', '班级', '语文', '数学', '英语'])
], index=[0, 1, 2])

print(df1)

#####DataFrame数据分析
#1.数据缺失处理
df = pd.DataFrame(np.random.randn(5, 3),
index = ['a', 'c', 'e', 'f', 'h'],
columns = ['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df.dropna())  #丢弃缺失行
print(df.fillna(0))#换数填充

#2.统计分析
#可以使用count sum mean mode std min max等函数进行计算
"""

