import pandas as pd

data = {'Marks':[45,67,88,32,76]}

df = pd.DataFrame(data)

print(df)

#df_new = df['Marks'].replace({45:'Fail',32:'Fail'})

df_new = df['Marks'].where(df['Marks']>=50,'Fail')

print(df_new)