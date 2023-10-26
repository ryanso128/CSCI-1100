# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:53:10 2022

@author: ryani
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
frac=float(input('Enter the fraction: ').strip())
print(frac)
b=[]
for x in range(len(co2_levels)):
    co2_levels[x] = co2_levels[x]*(1+frac)
print('First: {:.2f}\nLast: {:.2f}'.format(co2_levels[0], co2_levels[-1]))

    

    
