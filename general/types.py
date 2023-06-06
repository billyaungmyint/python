import pandas as pd

print(type('Hello'))
print(type(12))
print(type([1,2,3]))
print(type({"Hello" : 123 , "Goodbye" : 345}))

x = pd.DataFrame([[1,2,3] , [4,5,6]])
print(x)
print(type(x))