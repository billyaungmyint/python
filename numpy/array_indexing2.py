from numpy import array

data = array([11,22,33,44,55])
data2 =array([
    [11,22,33,44,55],
    [66,77,88,99,100100],
    [111,222,333,444,555]
])
print('print entire array')
print(data2)
print()
print('print the first and second column values. 0 - 2 but 2-1 = 1 so it prints 2 columns , 0 and 1.')
print(data2[:,0:2])
print()
print('print the 3rd column values')
print(data2[:,2])
print()
print('print the second row of first and second columns')
print(data2[1 , 0:2])
