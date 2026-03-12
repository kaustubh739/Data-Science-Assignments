import pandas as pd
import numpy as np

data = {'Marks':[85,np.nan,90,np.nan,95]}

df = pd.DataFrame(data)

#df.fillna(df.mean(numeric_only=True),inplace=True)

df_interpolated = df.interpolate(method='linear')

print(df_interpolated)