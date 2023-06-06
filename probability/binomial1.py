import numpy as np
from scipy.stats import binom

p = 0.3
k = 100

success = np.random.binomial(k,p)
print(success)
print()

mean , var , _ , _ = binom.stats(k,p, moments = 'mvsk')
print('Mean=%.3f , Variance=%.3f' % (mean , var))
