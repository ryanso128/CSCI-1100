# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:51:07 2022

@author: ryani
"""
def first_day_greater(x, y):
    d=0
    for z in range(len(x)):
        if x[z]>y[z]:
            d=z
            break
        else:
            d=-1
    return d
if __name__ == "__main__":
    L1 = [ 15.1, 17.3, 12.3, 16.4 ]
    L2 = [ 15.0, 17.7, 12.5, 16.9 ]
    print("Test 1: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.6, 17.9, 18.2, 16.5, 12.7 ]
    print("Test 2: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.9, 18.8, 11.4 ]
    print("Test 3: {}".format( first_day_greater(L1,L2) ))