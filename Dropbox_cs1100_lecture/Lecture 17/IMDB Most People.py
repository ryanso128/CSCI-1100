# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:23:32 2022

@author: ryani
"""

if __name__=='__main__':
    file=input('Enter the name of the IMDB file ==> ').strip()
    print(file)
    x=open(file, encoding = "ISO-8859-1").read().strip().split('\n')
    y=dict()
    z=set()
    for movie in x:
        movie=movie.split('|')
        for things in movie:
            num=movie.index(things)
            movie[num]=things.strip()
        z.add((movie[1], movie[0]))
    z=sorted(list(z))
    for stuff in z:
        y[stuff[0]]=0
    for stuff in z:
        y[stuff[0]]+=1
    maxx=0
    maxxx=[]
    for stuzz in y:
        if y[stuzz]>maxx:
            maxx=y[stuzz]
            maxxx=[stuzz, y[stuzz]]
    print(maxxx[1])
    print(maxxx[0])
    least=0
    for sturr in y:
        if y[sturr]==1:
            least+=1
    print(least)
        
    
    