import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)

marks = df[df['Name']=='Sagar'][['Math','Science','English']].values.flatten()

subjects = ['Math','Science','English']

plt.pie(marks,labels=subjects, autopct='%1.1f%%',startangle=90)
plt.title("Pie Chart")

plt.show()

print(df)