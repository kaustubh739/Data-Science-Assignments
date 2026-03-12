import pandas as pd

data =  {'Age':[18,22,25,30,35]}

df = pd.DataFrame(data)

print(df)

df_Normalized = ((df['Age']-df['Age'].min())/(df['Age'].max()-df['Age'].min()))

print(df_Normalized)