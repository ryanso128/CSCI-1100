# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:09:44 2022

@author: ryani
"""
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
from Date import Date
d=Date()
file=open('birthdays.txt').read().strip().split('\n')
file.sort()
new_file=[]
for days in file:
    days=days.split()
    days=Date(days[0], days[1], days[2])    
    new_file.append(days)
    
print('Oldest:', new_file[0])
print('Youngest:', new_file[-1])
month_count=[0]*12
for date in file:
    date=date.split()
    month_count[int(date[1])-1]+=1
print('Most Birthdays: {}'.format(month_names[max(month_count)]))

