# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:16:47 2022

@author: ryani
"""

def convert_set(file):
    vwords=set()
    for words in file:
        for char in words:
            if char.isalpha()==False:
                words=words.replace(char, '')
        if len(words)>=4:
            vwords.add(words)
    return vwords

if __name__=='__main__':
    file1=input('Enter file 1: ')
    file2=input('Enter file 2: ')
    file1=open(file1).read().lower().replace('|', ' ').split()
    file2=open(file2).read().lower().replace('|', ' ').split()
    set1=convert_set(file1)
    set2=convert_set(file2)
    inter=set1&set2
    print(inter)
    exc1=set1-set2
    print(exc1)
    exc2=set2-set1
    print(exc2)