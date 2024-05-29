import pandas as pd


data_sex = pd.read_excel("titanic_sex.xls")
data = pd.read_excel("titanic_no_sex.xls")

print(data.describe())
print(data_sex.describe())

new_data = pd.merge(data,data_sex, left_on='name', right_on='name',how='left')
new_data['sex'] = new_data['sex'].fillna('male')

# data.insert(1,'sex',np.nan)

print(data.describe())
new_data.to_excel('res2.xls')