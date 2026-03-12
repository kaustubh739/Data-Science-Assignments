import pandas as pd

data = {'Grade': ['A+','A','B+','B','C']}

df = pd.DataFrame(data)

print(df)

df_new = df['Grade'].replace({'A+':'Excellent','A':'Very Good','B+':'Good','B':'Average','C':'Poor'})

print(df_new)