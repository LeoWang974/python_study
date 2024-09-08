import numpy as np
from docutils.nodes import label
from scipy.integrate import *
from scipy import linalg
import matplotlib.pyplot as plt

#简单实例，求解矩阵行列式
A = np.random.randint(0, 9, (3, 3))     #随机生成一个值在0~9之间的3阶矩阵
print(A)
x = linalg.det(A)       #求得矩阵的行列式
print(x)


#############integrate模块用于求数值积分和常微分方程
#1.常用积分方法
#1.1给定函数对象求积分，以∫(0~2) x^ndx和圆为例
def func(x, n):
    return x**n
down_limit = 0
up_limit = 2
#n的值通过args参数来进行传递，quad用于求一重积分
result1 = quad(func, down_limit, up_limit, args=(1,))
print(result1)
result2 = quad(func, down_limit, up_limit, args=(2,))
print(result2)

#定义单位半圆曲线函数（y>0）
def hemiCircle(x):
    return (1 - x**2)**0.5
#根据函数x^2+y^2+z^2=1(z>=0),定义通过(x,y)坐标计算球面上点z的值的函数
def hemiSphere(x, y):
    return (1 - x**2 - y**2)**0.5
#X-Y平面与x^2+y^2+z^2=1表示的球体相交结果为单位圆，因此积分区间为单位圆，可以对x轴从-1到1进行积分，对y轴从-hemi_circle(x)到hemi_circle(x)进行积分
result = dblquad(hemiSphere, -1, 1, lambda x:-hemiCircle(x), lambda x:hemiCircle(x))  #dblquad用于解二重积分
print('dblquad result = ',result)
print('球体面积计算结果 = ', np.pi*4/3/2)

#1.2对固定采样样本数值求积分
#采样又称取样，是指把时间域或空间域的连续量转换成离散量的过程
#此次使用trapz法即梯形法来求积分
#trapz(y, x=None, dx=1.0, axis=-1)，其中积分的数值序列y是trapz方法调用的必要参数，以y=x^2为例
def func(x, n):
    return x**n
N = 2000
x = np.linspace(0, 2, N)    #取2000个离散值
y = func(x, 2)
result = trapz(y, x)
print('result: ', result)

#2.求解常微分方程
def pend(y, t, b, c):
    theta, omega = y    #向量[theta, omega]用y表示
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt
b, c = 0.25, 5.0
#假设摆锤近似垂直，theta(0)=pi-0.1;并且最初是精致的，所以Omega(0)=0
y0 = [np.pi - 0.1, 0.0] #设置初始值
t = np.linspace(0, 10, 101) #在0~10的范围内产生101个均匀间隔样本

sol = odeint(pend, y0, t, args=(b, c))  #得到的sol是（101，2）的多维数组，第一列是theta，第二列是moega
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()


