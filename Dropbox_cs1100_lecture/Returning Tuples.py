# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:55:32 2022

@author: ryani
"""

def add_tuples(x, y, z):
    a=x[0]+y[0]+z[0]
    b=x[1]+y[1]+z[1]
    return (a, b)

print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))