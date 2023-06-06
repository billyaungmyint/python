# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:20:35 2022

@author: Dreambuilds
"""
print('Please think of a number between 0 and 100!')
low = 0
high = 100
mid = (low + high) / 2
correct = False

while correct == False:
    print('Is your secret number ' + str(mid) + '?' + '\n')
    ans = input(
        'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if ans == 'h':
        high = int(mid)
        mid = int((high + low) / 2)
        correct = False
    elif ans == 'l':
        low = int(mid)
        mid = int((high + low) / 2)
        correct = False
    elif ans == 'c':
        print('Game over. Your secret number was : ' + str(mid))
        correct = True
    else:
        print('Sorry, I did not understand your input.')
        correct = False

