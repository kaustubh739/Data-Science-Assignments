import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

marks = df[df['Name'] == 'Amit'][['Math','Science','English']].values.flatten()

Subjects = ('Math','Science','English')

plt.plot(Subjects,marks,marker = 's')

plt.xlabel('Subjects')
plt.ylabel('marks')
plt.title('Amit Report')
plt.grid(True)
plt.show()

print(df)