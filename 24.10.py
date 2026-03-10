import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)

'''sns.boxplot(x='Name',y='English',data=df)

plt.title('Boxplot for english marks')
plt.show()'''

sns.boxplot(y=df['English'],color='skyblue')
plt.title("Boxplot for english marks")
plt.xlabel('Name')
plt.ylabel('marks')
plt.show()

