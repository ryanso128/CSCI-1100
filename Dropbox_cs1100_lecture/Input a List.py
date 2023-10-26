# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:01:15 2022

@author: ryani
"""

list=[]
i=0
end=False
avg=0
while not end:
    value=int(input('Enter a value (0 to end): ').strip())
    print(value)
    if value==0:
        end=True
    else:
        list.append(value)
        avg+=list[i]
        i+=1
print('Min: {}\n'
      'Max: {}\n'
      'Avg: {:.1f}'
      .format(min(list), max(list), avg/len(list)))
    