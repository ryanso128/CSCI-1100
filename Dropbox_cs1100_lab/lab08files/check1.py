# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:13:13 2022

@author: ryani
"""

file=input('File name: ')
file=open(file).read().lower().replace('|', ' ').split()
vwords=set()
for words in file:
    for char in words:
        if char.isalpha()==False:
            words=words.replace(char, '')
    if len(words)>=4:
        vwords.add(words)
print(vwords)
