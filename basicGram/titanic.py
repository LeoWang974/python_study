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
#g.map(plt.hist, 'Age', bins=20)

train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)
test_df = pd.read_csv('test.csv')
test_df = test_df.drop(['Ticket', 'Cabin'], axis=1)
combine = [train_df, test_df]

#在上段内容中，部分内容仍未字母，可通过以下方式将这些特征转化为数字
for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
test_crosstab = pd.crosstab(train_df['Title'], train_df['Sex'])


for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess', 'Capt', 'Col',
                                                'Don', 'Dr', 'Major', 'Rev', 'Sir',
                                                 'Jonkheer', 'Done'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
#print(train_df[['Title', 'Survived']].groupby(['Title'],as_index=False).mean())

title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)
train_df = train_df.drop(['Name', 'PassengerId'], axis=1)
test_df = test_df.drop(['Name'], axis=1)
combine = [train_df, test_df]
train_df.head(3)


sex_mapping = {"male": 0, "female": 1}
for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)
    dataset['Sex'] = dataset['Sex'].dropna()

guess_ages = np.zeros((2, 3))
for dataset in combine:
    for i in range(0, 2):
        for j in range(0, 3):
            #此处有问题
            guess_df = dataset[(dataset['Sex'] == i) & (dataset['Pclass'] == j+1)]['Age'].dropna()
            age_guess = guess_df.median()
            guess_ages[i, j] = int(age_guess/0.5 + 0.5) * 0.5

    for i in range(0, 2):
        for j in range(0, 3):
            dataset.loc[(dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j+1), 'Age'] = guess_ages[i, j]

    dataset['Age'] = dataset['Age'].astype(int)
    freq_port = train_df.Embarked.dropna().mode()[0]
    for dataset in combine:
        dataset['Embarked'] = dataset['Embarked'].fillna(freq_port)
        train_df[['Embarked', 'Survived']].groupby(['Embarked'], as_index=False).mean().sort_values(by = 'Survived',
                                                                                               ascending=False)

print(guess_ages)
for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)

print(train_df)
