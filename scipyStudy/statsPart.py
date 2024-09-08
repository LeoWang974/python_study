import numpy as np
from mkl_random.mklrand import RandomState
from scipy.stats import *
from sqlalchemy.sql.functions import random
from sympy.geometry.entity import scale


#本篇使用概率统计模块
#1.连续型随机变量
#loc为期望值，即对称轴位置，scale为标准差（方差^0.5）,默认loc=0，scale=1，即标准正态分布
print('rvs = ', norm.rvs(size=10)) #产生十个正态分布的随机变量
print('pdf = ', norm.pdf(0)) #根据x求概率分布值
print('cdf = ', norm.cdf(1, loc=1, scale=1))    #根据x求累计概率分布值
print('ppf = ', norm.ppf(0.5, loc=1, scale=1))  #根据累计概率分布值反求x值
print('sf = ', norm.sf(0))  #随机变量的生存函数
print('stats = ', norm.stats()) #随机变量的期望值和方差
print('mean = ', norm.mean()) #随机变量的期望值
print('std = ', norm.std()) #随机变量的方差

x = norm.rvs(loc=1.0, scale=2.0, size=100)  #求正态分布的最佳拟合参数fit
print('fit = ', norm.fit(x))


#2.离散型随机变量
#二项分布
n = 100 #次数
p = 0.5 #概率
f = binom(n, p)
print('stats = ', f.stats())    #二项分布的期望与方差
print('mean = ', f.mean())

_lambda = 10    #λ值
time = 10000    #观察时间
t = np.random.rand(_lambda*time)*time
count, time_edges = np.histogram(t, bins=time, range=(0, time))#统计某时间内事件发生的次数
sol = poisson(count)
print('pmf = ', sol.pmf(1))  #pmf概率质量函数
print('cdf = ', sol.cdf(1))

#3.常用统计方法
rndm = np.random.RandomState(1234)
a = np.arange(10)
print('describe_a = ',describe(a))
b = [[1, 2], [3, 4]]
print('describe_b = ',describe(b))
print('gmean = ', gmean([1, 4]))    #计算沿指定轴的几何平均值
print('hmean = ', hmean([1, 4]))    #计算沿指定轴的调和平均值
for n in range(2, 8):
    x = rndm.normal(size = 10**n)
    m, k = moment(x, 3), kstat(x, 3)
    print('mk = ', "%.3g %.3g %.3g "%(m, k, m-k))

