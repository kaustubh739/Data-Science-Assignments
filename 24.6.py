import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science'] + df['English']

df['Status'] = df['Total'].apply (lambda X : 'Pass' if X>=250 else 'Fail')

#print((df['Status'] == 'Pass').sum())

print(df[df['Status'] == 'Pass']['Status'].count())