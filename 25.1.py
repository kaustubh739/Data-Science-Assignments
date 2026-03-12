import pandas as pd

data = {'Salary' : [25000, 27000, 29000, 31000, 50000, 100000]}

df = pd.DataFrame(data)

print(df.describe())

Q1 = df.Salary.quantile(0.25)
Q3 = df.Salary.quantile(0.75)

print(Q1,Q3)

IQR = Q3 - Q1
print(IQR)

lower_limit = Q1 - 0.5*IQR
upper_limit = Q3 + 0.5*IQR
print(lower_limit,upper_limit)

print(df[(df['Salary']<lower_limit) | (df['Salary']>upper_limit)])

df_no_outlier = df[(df['Salary'] >= lower_limit) & (df['Salary'] <= upper_limit)]

print(df_no_outlier)