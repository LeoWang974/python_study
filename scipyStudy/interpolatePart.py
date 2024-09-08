import matplotlib.pyplot as plt
import numpy as np
from scipy import  interpolate
from scipy.interpolate import griddata


"""
#使用插值可以通过已知的离散数据求未知数据，与拟合不同，插值要求曲线通过所有已知点，插值是离散函数逼近的重要方法
#利用插值可通过函数在有限个点处的取值情况估算出函数在其他点处的近似值
#1.一维插值方法
x = np.arange(0, 10)
print(x)
y = np.exp(-x/3.0)      #定义f(x)函数
print(y)
p = interpolate.interp1d(x, y)  #调用interp1d方法，求解得到p(x)函数
print(p)
xnew = np.arange(0, 9, 0.1)
ynew = p(xnew)
plt.plot(x, y, 'bo', xnew, ynew, 'r-')
plt.show()


"""

#2.多维插值方法
#多维插值主要用于图像重构，使用griddata使用多维散列取样点进行插值运算，其定义为
#griddata(points, values, xi, method='linear',fill_value=nan),其中points表示K维空间中的坐标，可以是形为(N,K)的数组，也可以是有K个数组的序列，N为数据的点数
#values是points中每个点对应的值，xi是需要进行插值运算的坐标，形状为(M,K),M为需要进行插值运算的坐标数量。method有nearest,linear,cubic分别指0，1，3阶插值
def func_ndmin(x, y):
    return x*(1-x)*np.cos(4*np.pi*x)*np.sin(4*np.pi*y**2)**2    #定义二维数组
#生成grid数据，复数定义了生成grid数据的步幅step，若省略复数，则默认step为5
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]   #np.mgrid用于生成网格型数据
points = np.random.rand(1000, 2)
values = func_ndmin(points[:,0], points[:,1])

grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

def func(x, n):
    return x**n  # 定义函数 xn

plt.subplot(221)
plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
plt.plot(points[:, 0], points[:, 1], 'k', ms=1)
plt.title('Original')

plt.subplot(222)
plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
plt.title('Nearest')

plt.subplot(223)
plt.imshow(grid_z1.T, extent=(0,1,0,1), origin='lower')
plt.title('Linear')

plt.subplot(224)
plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')
plt.title('Cubic')

plt.gcf().set_size_inches(6, 6)
plt.show()