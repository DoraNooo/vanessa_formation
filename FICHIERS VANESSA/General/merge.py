import matplotlib.pyplot as plt
import pandas as pd


data_sex = pd.read_excel("titanic_sex.xls")
data = pd.read_excel("titanic_no_sex.xls")

print(data.describe())
print(data_sex.describe())

new_data = pd.merge(data,data_sex, left_on='name', right_on='name')

print(new_data.describe())

new_data.to_excel('res.xls')