# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:26:27 2022

@author: ryani
"""

values = [ 14, 10, 8, 19, 7, 13 ]
a=input('Enter a value: ')
print(a)
a=int(a)
values.append(a)
b=input('Enter another value: ')
print(b)
b=int(b)
values.insert(2, b)
print(values[3], values[-1])
c=max(values)-min(values)
print('Difference: {}'.format(c))
d=sum(values)/len(values)
print('Average: {:.1f}'.format(d))
values.sort()
e=(values[3]+values[4])/2
print('Median: ', e)
