# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:11:27 2022

@author: ryani
"""

def find_min(x):
    i=[]
    for y in x:
        for z in y:
            i.append(z)
    a=min(i)
    return(a)
if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )