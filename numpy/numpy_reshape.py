from numpy import array

data = array([11,22,33,44,55])
print(data.shape)

data = data.reshape(data.shape[0],1)
print(data.shape)