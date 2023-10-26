# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:30:08 2022

@author: ryani
"""
a=[]
b=[]
c=[]
for y in range(9):
    for z in range(9):
        c.append(y)
        c.append(z)
        b.append(c)
        c=[]
    a.append(b)
    b=[]

for x in range(len(a)):
    for d in range(len(a[x])):
        if d%3==2:
            e='  '
        else:
            e=' '
        if x%3==2 and d==8:
            f='\n'
        else:
            f=''
        if d==8:
            g='\n'
        else:
            g=''
        print('{},{}{}{}{}'.format(a[x][d][0], a[x][d][1], e, f, g), end='')

i=0
for h in a[3]:
    print('{},{} '.format(h[0], i), end='')
    i+=1
print('\n')

l=[]
for j in a:
    for k in j:
        if k[1]==5:
            l.append(k)
for m in l:
    print('{},{} '.format(m[0], m[1]), end='')

p=[]    
for n in a:
    for o in n:
        if (o[1]//3)==1:
            if (o[0]//3)==1:
                p.append(o)
                