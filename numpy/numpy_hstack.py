from numpy import array
from numpy import hstack

a1 = array([1,2,3])
print(a1)

a2 = array([4,5,6])
print(a2)

a3 = hstack((a1,a2))
print(a3)
print(a3.shape)