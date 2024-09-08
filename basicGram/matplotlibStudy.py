import matplotlib.pyplot as plt
import numpy as np
from docutils.nodes import label
from numpy.ma.core import around
from mpl_toolkits.mplot3d import Axes3D #3d图像需要引入

"""
###########Part1 常用2D图形
#1.绘制一个简单的图形
plt.plot([1, 2, 3], [4, 5, 6])
# 显示图形
plt.show()

#2.绘制散点图
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)

#3.随机生成两组数据
x1 = np.random.randint(0, 5, 5)
y1 = np.random.randint(0, 5, 5)
x2 = np.random.randint(5, 10, 5)
y2 = np.random.randint(5, 10, 5)
#4.绘制两种不同颜色和样式的散点图
plt.scatter(x1, y1, marker = 'x', color='red', s = 40)
plt.scatter(x2, y2, marker = 'o', color='green', s = 80)

#5.绘制线型图
x = [0, 1, 2, 3, 4, 5, 6]
y = [0.3, 0.4, 2, 5, 3, 4.5, 4]
plt.plot(x, y)

x = np.arange(10)   #随机生成10个x轴坐标
y1 = x * 1.5
y2 = x * x
y3 = x * 3.5 + 5
y4 = 10 - x * 4.5
#6.绘制定义的4个方法
plt.plot(x, y1, 'go-', x, y2, 'rx', x, y3, '*',x, y4, 'b-.')

#7.绘制柱状图
x = np.arange(10)
y = np.random.randint(0, 30, 10)
plt.bar(x, y)

n = 10
x = np.arange(n) + 1
y1 = np.random.uniform(0.5, 1.0, n)
y2 = np.random.uniform(0.5, 1.0, n)
plt.bar(x, y1, width=0.35, facecolor='blue', edgecolor='white')
plt.bar(x + 0.35, y2, width=0.35, facecolor='red', edgecolor='white')

#8.绘制直方图
x = np.random.randn(1000)
plt.hist(x, bins=50)

x = np.random.randn(1000)
plt.hist(x, 60, facecolor='red', edgecolor='black', alpha=1, histtype='bar')
#此处不能传入normed参数，因为用于标识是否将直方图的频率normalize到一个单位范围（即归一化直方图），否则会报Rectangle.set() got an unexpected keyword argument 'normed'
#如果你正在使用的是matplotlib.pyplot.hist()并想要设置归一化的直方图，你应该使用histtype='normed'（注意在较新版本的matplotlib中，应使用histtype='density'来获取归一化直方图）。

#9.绘制饼状图
data = [15, 15, 40, 30]
plt.pie(data)

data = [15, 30, 45, 20]
labels = ['A', 'B', 'C', 'D']
explodes = (0, 0.1, 0, 0)
plt.pie(data, explode=explodes, labels=labels, autopct='%1.2f%%', radius=1, pctdistance=0.5, labeldistance=1.2)


###############Part2 常用3D图形
#1.3D散点图
fig = plt.figure()  绘制画布
ax = fig.add_subplot(111, projection='3d')
x = np.random.randint(0, 100, 500)
y = np.random.randint(0, 100, 500)
z = np.random.randint(0, 100, 500)
ax.scatter(x, y, z)

#2.3D曲线图
x = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
y = np.sin(x)
z = np.cos(x)
fig = plt.figure()  
# ax = Axes3D(fig) 旧版，无法出图
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

#3.3D曲面
def fun(x, y):
    return np.power(x, 2) + np.power(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
x,y = np.meshgrid(x, y)
z = fun(x, y)
ax.plot_surface(x, y, z)

#4.3D柱状图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2]
for i in x:
    y = [1, 2]
    z = abs(np.random.normal(1, 10, 2))
ax.bar(y, z, i, zdir = 'y')


########Part3 图形设置
#1.可以通过matplotlib.pyplot.colors()获取颜色
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   #字体
plt.rcParams['axes.unicode_minus'] = False
x1 = np.random.rand(100)
y1 = np.random.rand(100)
x2 = np.random.rand(100)
y2 = np.random.rand(100)
x3 = np.random.rand(60)
y3 = np.random.rand(60)

plt.scatter(x1, y1, c = 'r')
plt.scatter(x2, y2, c = '#0000FF')
plt.scatter(x3, y3, c = (0.4, 0.4, 0.2))

#2.添加标题和注释
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(10)
y = np.random.randint(0, 30, 10)
plt.bar(x, y)
plt.annotate('第二个柱状图', xy = (1, 20), xytext = (2, 25), arrowprops=dict(facecolor='red', shrink=0.05))   #注释
plt.title('柱状图')        #标题

********plt.rcParams是matplotlib对象的一个字典，用于配置全局信息

#3.设置图例和标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
x = np.linspace(1, 10, 50)
y1 = [(i ** 2) for i in x]
y2 = [(i * 4 + 20) for i in x]
plt.plot(x, y1, label = 'y = x*x', linestyle = '-')
plt.plot(x, y2, label = 'y = x*4 + 6', linestyle = '--')
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('二元方法')
#是Matplotlib库中用于添加图例（legend）的函数。通过 plt.legend()可以将图例添加到您创建的图表中，以提高图表的可读性。
#例：plt.legend(loc='best', prop={'size': 12}, title='图例标题')
plt.legend()


########Part4 文件操作 Part5图像操作
"""








plt.show()