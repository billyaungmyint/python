import numpy as np
import pandas as pd

array1 = np.array([[1,2,3] , [4,5,6]])
rownames = ['a' , 'b']
colnames = ['one' , 'two' , 'three']

df1 = pd.DataFrame(array1 , index = rownames , columns= colnames)
print(df1)
print()
print(df1['one'])
print(df1.one)
print()
print(df1.iloc[[1]])
