import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

df['total'] = df['Math'] + df['Science'] + df['English']

plt.bar(df['Name'],df['total'])

plt.xlabel('Student Names')
plt.ylabel('Marks')
plt.title("Student's Report")

plt.show()

print(df)

