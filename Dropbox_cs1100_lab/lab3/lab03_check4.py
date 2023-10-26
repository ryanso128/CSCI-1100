# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:44:46 2022

@author: ryani
"""

bpop=int(input('Number of bunnies ==> '))
print(bpop)
fpop=int(input('Number of foxes ==> '))
print(fpop)
i=0
while i<5:
    print('Year {}: {} {}'.format(i+1, bpop, fpop))
    bpop_next=int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    fpop_next=int(0.4 * fpop + 0.02 * fpop * bpop)
    bpop=bpop_next
    fpop=fpop_next
    i+=1
    