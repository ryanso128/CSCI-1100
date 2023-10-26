# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:23:52 2022

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
    file2=open('allclubs.txt').read().strip().split('\n')
    file1=open(file1).read().strip().split('|')
    set1=[file1[0],convert_set(file1[1].split())]
    clubset=[]
    for club in file2:
        club=club.split('|')
        club[1]=club[1].split()
        club[1]=convert_set(club[1])
        clubset.append(club)
    orderedclubs=[]
    for clubs in clubset:
        compare=clubs[1]&set1[1]
        orderedclubs.append((len(compare), clubs[0]))
    orderedclubs=sorted(orderedclubs, reverse=True)
    i=0
    while i<5:
        print(orderedclubs[i+1][1])
        i+=1
    