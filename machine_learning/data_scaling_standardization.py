# example of a standardization
from numpy import array
from sklearn.preprocessing import StandardScaler
# define data
data = array([[100, 0.001],[8, 0.05],[50, 0.005],[88, 0.07],[4, 0.1]])
print(data)
# define standard scaler
scaler = StandardScaler()
# transform data
scaled = scaler.fit_transform(data)
print(scaled)

