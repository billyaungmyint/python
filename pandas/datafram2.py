import numpy as np
import pandas as pd

array1 = np.array([[1,2,3] , [4,5,6],[7,8,9],[10,11,12]])
rownames = ['a' , 'b','c','d']
colnames = ['one' , 'two' , 'three']

df1 = pd.DataFrame(array1 , index = rownames , columns= colnames)
print(df1)
print()
# print(df1.index)
# print(df1.values)
# print(df1.shape)
# print(df1.describe())
# print(df1.dtypes)
print(df1.iloc[1])
print(df1.iloc[1][0])
print()
print(df1.loc['b'])
print(df1.loc['b'][0])
print()
print(df1['one']['b'])
print()
print(df1.index)
print(df1['three']['b'])