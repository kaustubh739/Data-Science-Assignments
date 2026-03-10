import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)

#df_new = df.groupby('Gender').mean(numeric_only = True)

df['Average'] = df[['Math','Science','English']].mean(axis=1)

gender_avg = df.groupby('Gender')['Average'].mean()

print(gender_avg)