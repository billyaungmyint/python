import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
y = np.array([2,4,6])

plt.scatter(x,y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()