import pandas as pd
from sklearn.model_selection import train_test_split

data = {'Age':[22,25,47,52,46,56],'Purchased':[0,1,1,0,1,0]}

df = pd.DataFrame(data)

X = df[['Age']]
Y = df['Purchased']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

print("Dimension of X_train : ",X_train.shape)
print("Dimension of X_test : ",X_test.shape)
print("Dimension of Y_train : ",Y_train.shape)
print("Dimension of Y_test : ",Y_test.shape)

