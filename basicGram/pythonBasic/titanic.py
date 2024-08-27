import pandas as pd
import numpy as np
import random as rnd
#seaborn是matplotlib的扩展包
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv('train.csv')
train_df.head(5)    #输出前五行
train_df.tail(5)    #输出后五行

train_df.describe() #整体统计信息

#根据船舱类别判断平均生存率
train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean()\
            .sort_values(by='Survived', ascending=False)

#根据性别判断平均生存率
train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean()\
            .sort_values(by='Survived', ascending=False)

#年龄与生还概率,绘图，
g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Age', bins=20)

train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)
test_df = pd.read_csv('test.csv')
test_df = test_df.drop(['Ticket', 'Cabin'], axis=1)
combine = [train_df, test_df]

#在上段内容中，部分内容仍未字母，可通过以下方式将这些特征转化为数字
for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
test_crosstab = pd.crosstab(train_df['Title'], train_df['Sex'])
