# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:30:41 2022

@author: ryani
"""
co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
  348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
compare=0
avg=0
for f in co2_levels:
    avg=sum(co2_levels)/len(co2_levels)
    compare+=(f>avg)
print('''Average: {:.2f}
Num above average: {}'''.format(avg, compare))


