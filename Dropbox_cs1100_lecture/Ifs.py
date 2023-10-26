# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:27:58 2022

@author: ryani
"""

x=input('Enter the first number: ').strip()
print(x)
y=input('Enter the second number: ').strip()
print(y)
x=float(x)
y=float(y)
if (x>10) and (y>10):
    print('Both are above 10.')
elif (x<=10) and (y<=10):
    print('Both are below 10.')
print('Average is {:.2f}'.format((x+y)/2))    