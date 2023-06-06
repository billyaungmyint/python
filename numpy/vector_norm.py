from math import inf
from numpy import array
from numpy.linalg import norm

a = array([1,2,4])
print(a)

#L2 norm , distance of the vector coordinate from origin
l2 = norm(a)
print(l2)

# l1 norm , |1| + |2| + |4|
l1 = norm(a,1)
print(l1)

# maxnorm , highest vector
maxnorm = norm(a , inf)
print(maxnorm)

