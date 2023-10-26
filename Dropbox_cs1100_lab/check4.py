# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:59:53 2022

@author: ryani
"""

first=input('Please enter your first name: ')
print(first)
last=input('Please enter your last name: ')
print(last)
h='Hello,'
if len('Hello,')>=len(first) and len('Hello,')>=len(last):
    x=len('Hello,')
elif len(first)>=len(last):
    x=len(first)
elif len(last)>=len(first):
    x=len(last)
stars='*'*x
a=h+' '*(x-len(h))
b=first+' '*(x-len(first))
c=last+' '*(x-len(last))
print('***{}***\n'
      '** {} **\n'
      '** {} **\n'
      '** {} **\n'
      '***{}***\n'
      .format('*'*x, a, b, c, '*'*x))    
