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

#marks = df['Math'].values.flatten()

#student = df[['Amit','Sagar','Pooja']] exceptes only 

plt.bar(df['Name'], df['Math'], color="skyblue", edgecolor="black") 
plt.xlabel('Student') 
plt.ylabel('Math Marks') 
plt.title('Math Marks per Student') 

plt.show()
'''plt.hist(df['Math'],bins = 5, color = "skyblue",edgecolor = 'black')

plt.xlabel('marks')
plt.ylabel('frequency')
plt.title('Math Marks')

plt.show()'''