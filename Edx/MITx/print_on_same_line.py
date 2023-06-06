# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:05:19 2022

@author: Dreambuilds
"""

# Notice how if we have two print statements                
print("Hi")
print("there")

# The output will have each string on a separate line:                
#Hi
#there
                
# Now try adding the following:
print("Hi",end='')
print("there")
print("Hi",end='*')
print("there")   
                
# The output will place the subsequent string on the same line
# and will connect the two prints with the character given by end
#Hithere
#Hi*there   