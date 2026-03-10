import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)

df['Total'] = df['Math']+df['Science']+df['English']

def Check_Status(X):
    if X >= 250:
        return 'Pass'
    else:
        return 'Fail'
    
df['status'] = df['Total'].apply(lambda X : 'Pass'if X>=250 else 'Fail') # Ternary expression

#df['status'] = df['Total'].map(Check_Status) # map = it will map with all subjects.

print(df)
