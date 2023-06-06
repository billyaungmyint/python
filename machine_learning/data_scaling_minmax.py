# https://machinelearningmastery.com/standardscaler-and-minmaxscaler-transforms-in-python/
# example of a normalization
from numpy import array
from sklearn.preprocessing import MinMaxScaler
# define data
data = array([[100, 0.001],[8, 0.05],[50, 0.005],[88, 0.07],[4, 0.1]])
print(data)
# define min max scaler
scaler = MinMaxScaler()
# transform data
scaled = scaler.fit_transform(data)
print(scaled)