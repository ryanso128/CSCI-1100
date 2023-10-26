# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:49:00 2022

@author: ryani
"""
from PIL import Image
def make_square(x):
    b=x.size
    if b[0]>=b[1]:
        x=x.crop((0,0,b[1],b[1]))
    elif b[0]<b[1]:
        x=x.crop((0,0,b[0],b[0]))
    return x
