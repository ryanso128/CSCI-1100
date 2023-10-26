# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:42:58 2022

@author: ryani
"""

base10size=input('Disk size in GB => ')
print(base10size)
base2size=int((int(base10size)*10**9)/(2**30))
lost_size=int(int(base10size)-base2size)
print('{} GB in base 10 is actually {:.0f} GB in base 2, {:.0f} GB less than advertised.'.format(int(base10size), base2size, lost_size))
print('Input: ', '*'*int(base10size))
print('Actual:', '*'*base2size)