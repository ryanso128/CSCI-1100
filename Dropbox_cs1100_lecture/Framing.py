# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:48:37 2022

@author: ryani
"""

def frame_string(word):
    x=len(word)
    print('*'*(x+6),'\n',
          '** '+word+' **\n',
          '*'*(x+6), sep='', end='')


frame_string('Spanish Inquisition')
print('\n')
frame_string('Ni')