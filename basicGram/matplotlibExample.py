import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from docutils.nodes import label, figure

"""
#1.绘制子图
x = np.linspace(1, 100, 100)
y = np.random.randint(20, 60, size=100)
plt.figure(num="figure", figsize=(6, 4),facecolor='yellow', edgecolor='green')
#figure方法可以用来自定义图像的显示样式，num是窗口id，figsize是一个整数元组，表示绘图窗口的大小，dpi是分辨率，figureclass用于自定义Figure实例
plt.plot(x, y, c="red", label="y_line")
plt.legend()        #用于指示图例位置

#subplot方法用于对不同子图所在的比例和顺序进行布局控制
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
plt.title("子图绘制")
plt.subplot(2, 1, 1)
plt.plot([0.5, 1], [0.5, 1])
plt.subplot(2, 2, 3)
plt.plot([0.5, 1], [0.5, 1])
plt.subplot(2, 2, 4)
plt.plot([0.5, 1], [0.5, 1])


"""
#2.鸢尾花可视化属性分析
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#设置坐标轴的标签
def SetLabels(xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
data = pd.read_csv("iris.data", header=None)
#修改列名
data.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#去掉种类中的多余部分，即-之前的部分，例：Iris-setosa--->setosa
data['class'] = data['class'].apply(lambda x: x.split('-')[1])
#数据转换，把种类映射成数据类别
dict = {'setosa':0, 'versicolor':1, 'virginica':2}
data['Category'] = data['class'].map(dict)

fig = plt.figure()

plt.subplot2grid((3,2), (0, 0))
plt.scatter(data['sepal_len'], data['sepal_wid'], c=data.Category)
SetLabels('sepal_len', 'sepal_wid')
plt.title("萼片长度和宽度的种类分布图")

plt.subplot2grid((3,2), (0, 1))
plt.scatter(data.petal_len, data.petal_wid, c=data.Category)
SetLabels('petal_len', 'petal_wid')
plt.title("花瓣长度和宽度的种类分布图")

plt.subplot2grid((3,2), (1, 0))
plt.scatter(data.petal_len, data.sepal_len, c=data.Category)
SetLabels('petal_len', 'sepal_len')
plt.title("花瓣长度和萼片长度的种类分布图")

plt.subplot2grid((3,2), (1, 1))
plt.scatter(data.petal_wid, data.sepal_wid, c=data.Category)
SetLabels('petal_wid', 'sepal_wid')
plt.title("花瓣宽度和萼片宽度的种类分布图")

plt.subplot2grid((3,2), (2, 0))
plt.scatter(data.petal_len, data.sepal_wid, c=data.Category)
SetLabels('petal_len', 'sepal_wid')
plt.title("花瓣长度和萼片宽度的种类分布图")

plt.subplot2grid((3,2), (2, 1))
plt.scatter(data.petal_wid, data.sepal_len, c=data.Category)
SetLabels('petal_wid', 'sepal_len')
plt.title("花瓣宽度和萼片长度的种类分布图")

plt.tight_layout
plt.show()
