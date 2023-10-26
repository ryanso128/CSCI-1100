# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:36:22 2022

@author: ryani
"""

def convert2fahren(Celsius):
    return Celsius*1.8+32

print('0 -> {:.1f}'.format(convert2fahren(0)) )
print('32 -> {:.1f}'.format(convert2fahren(32)) )
print('100 -> {:.1f}'.format(convert2fahren(100)) )