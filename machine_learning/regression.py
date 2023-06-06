import matplotlib.pyplot as plt
import numpy as np

Advert = np.array([1,2,3,4,5,6])
Sales = np.array([1,2,3,4,5,6])

# 1 is linear , 2 is quadratic ...
# m , b = np.polyfit(Advert,Sales,1)
# formula is y = mx + b
# m is coeff and b is y intercept
# estimated_Sales = m * Advert + b
# print('coeff is ' + str(m))
# print('y intercept is ' + str(b))
#plt.plot(Advert , Sales , label = 'Actual Data')
# plt.plot(Advert , estimated_Sales , 'r' , label = 'Estimated Data')
# plt.legend()
# plt.show()
m = np.polyfit(Advert, Sales, 1)
poly1d_fn = np.poly1d(m)
plt.plot(Advert , Sales , 'yo' , Advert , poly1d_fn(Advert))
plt.show()

