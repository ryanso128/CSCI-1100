# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:16:08 2022

@author: ryani
"""

names=input('Data file names: ').strip()
print(names)
prefix=input('Prefix: ').lower().capitalize().strip()
print(prefix)
nameset=open(names, errors='ignore')
last_names=set()
i=0
for x in nameset:
    word=x.strip().split('|')
    lastname=word[0].split(',')
    last_names.add(lastname[0])
    if lastname[0]==prefix:
        i+=1
print(len(last_names), 'last names')
print(i, 'start with', prefix)