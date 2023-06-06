from numpy import array

data = array([11,22,33,44,55])
data2 =array([
    [11,22],
    [33,44],
    [55,66]
])


print(data)
print(data[1])
print(data[-1])

print()


print(data2)
print(data2[1,1])
print(data2[-1,1])