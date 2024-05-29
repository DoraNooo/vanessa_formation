import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_excel("titanic.xls")
print(type(data))
# print(data)

print(data.shape) #Taille du dataframe
print(data.head()) #Première ligne du dataframe

data = data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'], axis=1)

print(data.head())

print(data.describe())

data = data.dropna(axis=0)

print(data.describe())


plt.figure('Premiere fênetre')
print(data['pclass'].value_counts())
plt.subplot(2,1,1)
data['pclass'].value_counts().plot.bar()
plt.title('graphique 1')
plt.subplot(2,1,2)
data['age'].hist()
plt.legend()
plt.title('graphique 2')
plt.show()

print(data.groupby(['sex']).mean())
print(data.groupby(['sex','pclass']).mean())

dataset = {f"experience{i}": np.random.randn(100) for i in range(4)}
print(dataset)