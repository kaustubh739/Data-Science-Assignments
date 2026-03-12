import pandas as pd

data = {'Department' : ['HR','IT','Finance','HR','IT']}

df = pd.DataFrame(data)

print(df)

df_encoded = pd.get_dummies(df,columns=['Department'],dtype=int)

print(df_encoded)
