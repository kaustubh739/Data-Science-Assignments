import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'City' : ['Pune','Mumbai','Delhi','Pune','Delhi']}

df = pd.DataFrame(data)
encoder = LabelEncoder()

df['city_encoded'] = encoder.fit_transform(df['City'])
print(df)

print("Mapping:", dict(zip(encoder.classes_, encoder.transform(encoder.classes_))))

#print(df)
