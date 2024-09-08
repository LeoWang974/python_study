import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt

"""


#本篇使用优化模块
#找到函数的局部或全局最小值以及求方程解的问题都属于优化问题
#1.leastsp拟合方法/最小二乘拟合
#拟合是指将离散值通过调整函数系数使得函数与离散值点集差距最小，且有一定的泛化能力
def func_leastsq(x, p):
    a, b = p[0], p[1]
    return a*x +b   #需要拟合的数据
def residuals(p, x, y):
    return y - func_leastsq(x, p)   #实验数据x,y和拟合函数的差，p为拟合方法需要找到的系数
def func(x, n):
    return x**n  # 定义函数 x^n
x = np.linspace(-2, 2, 100)
a, b = 2, 0  # 真实函数参数
y0 = func_leastsq(x, [a, b])  # 真实数据值
y1 = y0 + 0.2 * np.random.randn(len(x))  # 加入噪声之后的实验数据值
p0 = np.random.randn(len(x))  # 参数的初始化值
result = leastsq(residuals, p0, args=(y1, x))  # args为需要拟合的实验数据
print("真实参数:", [a, b])
print("拟合参数", result[0])

plt.plot(x, y0, 'r.', label="Real data")
plt.plot(x, y1, label="Data with noisy")
plt.plot(x, func(x, result[0]), 'b+', label="Fitting data")
plt.legend()
plt.show()

#2.函数最小值方法
x = np.linspace(-10,18)
y = np.sin(x)+x/10
plt.plot(x,y,'r')  # 可视化函数f(x) = sin(x) +  x/10的图形
plt.title('$sin(x)+x/10$')
def func_min(x):
     return np.sin(x)+x/10  # 定义fmin、fmin_powell、fmin_bfgs三种方法需要的函数

local_min1 = fmin(func_min, 10)  # 调用fmin方法求函数最小值
local_min2 = fmin_powell(func_min, 5)  # 调用fmin_powell方法求函数最小值
local_min3 = fmin_bfgs(func_min, 0)  # 调用fmi_bfgs方法求函数最小值
plt.scatter(local_min1, func_min(local_min1),linewidths=9)  # 在上面的可视化图形中标出最小值
plt.scatter(local_min2, func_min (local_min2),linewidths=9)
plt.scatter(local_min3, func_min (local_min3),linewidths=9)

#使用brute求全局最小值
x = np.linspace(-10,18)
y = np.sin(x)+x/10  # 可视化函数f(x) = sin(x) +  x/10的图形
plt.plot(x,y,'r')
plt.title('$sin(x)+x/10$')
def func_min (x):
     return np.sin(x)+x/10# 定义函数
grid = (-10, 18, 0.1)
global_min = brute(func_min, (grid,))  # 调用brute方法求函数最小值
#plt.scatter(global_min,f(global_min),linewidths=9)

#3.fsolve方法，用于求方程与方程组的解
#求解一元方程组
x = np.linspace(-10,1)
y1, y2 = 2*np.sin(x), np.exp(x)+0.5  # 定义方程组函数
plt.plot(x,y1,'r',x,y2,'b--')
plt.title('$sin(x)$ and $e^x-0.5$')

def func_eq(x):
    return np.array(2*np.sin(x)-np.exp(x)-0.5)

res = fsolve(func_eq,[-9, -6, -3]) # 调用fsolve方法
print('求解的方程的根 = ', res)
print('方程的根对应的函数值 = ', 2*np.sin(res))
plt.scatter(res, 2*np.sin(res), linewidths=9)
plt.show()

#求解非线性方程组
def  func_eqs(x):
    x0, x1 = float(x[0]), float(x[1])
    return np.array([3*x0+2*x1-3, x0-2*x1-5])  # 定义方程组
sol2_fsolve = fsolve( func_eqs,[0,0]) # 调用fsolve方法
print('方程组的根 = ',sol2_fsolve)
"""


