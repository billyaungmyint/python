# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:57:35 2022

@author: Dreambuilds
"""

s = "azcbobobegghakl"
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print("Longest substring in alphabetical order is: " + str(longest))