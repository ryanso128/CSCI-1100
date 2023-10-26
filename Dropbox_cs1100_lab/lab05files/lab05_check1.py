# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:02:23 2022

@author: ryani
"""
import lab05_util
def print_info(x):
    restaurants = lab05_util.read_yelp('yelp.txt')
    x=restaurants[x]
    y=x[3].split('+')
    i=0
    j=0
    while i<len(x[-1]):
        j+=x[-1][i]
        i+=1
    if len(y)<3:
        z=y[1].split(',')
        print('{} ({})\n'
              '         {}\n'
              '         {}, {}\n'
              'Average score: {:.1f}'
              .format(x[0],x[5], y[0], z[0], z[1], j))
    else:
        z=y[2].split(',')
        print('{} ({})\n'
              '         {}\n'
              '         {}\n'
              '         {}, {}\n'
              'Average score: {:.1f}'
              .format(x[0], x[5], y[1], y[0], z[0], z[1], j))
        


print_info(42) 