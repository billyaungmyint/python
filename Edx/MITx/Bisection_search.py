# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:11:53 2022

@author: Dreambuilds
"""

x = 25
epsilon = 0.01
numGussess = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 -x) >= epsilon:
    print('low = ' +  str(low) + ' high = ' + str(high))
    numGussess += 1
    if ans**2  < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
    
print('numGussess : ' + str(numGussess))
print(str(ans) + ' is close to square root of ' + str(x))

