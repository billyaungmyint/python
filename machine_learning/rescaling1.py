import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(r'..\data\pima-indians-diabetes.csv',names=names)
print(df.values)
print()
array1 = df.values
X = array1[:,0:8]
Y = array1[:,8]
# print(X)
# print(Y)
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)
np.set_printoptions(precision=3)
print(rescaledX)