import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel("Data_titanic.xls")
print("data type = ", type(data))

print("data shape = ", data.shape) #Taille du dataframe
print("head5 data=", data.head(5)) #Première ligne du dataframe

data_drop = data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'], axis=1)
print("head5 data_drop = ", data_drop.head(5))
print("describe drop_data=", data_drop.describe())

data_dropna = data_drop.dropna(axis=0)
print("describe data_dropna=", data_dropna.describe())
print("nb per class = ", data_dropna['pclass'].value_counts())

data_dropna['pclass'].value_counts().plot.bar()
plt.show()
data['age'].hist()
plt.show()

print(data_dropna.groupby(['sex']).mean())
print(data_dropna.groupby(['sex', 'pclass']).mean())

plt.subplot(2,1,1)
data['pclass'].value_counts().plot.bar()
plt.subplot(2,1,2)
data['age'].hist()
plt.show()
