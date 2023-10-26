# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:28:22 2022

@author: ryani
"""

scores=input('Enter the scores file: ').strip()
print(scores)
sort=input('Enter the output file: ').strip()
print(sort)
a=open(scores)
b=[]
for x in a:
    x=x.strip()
    b.append(int(x))
b=sorted(b)
c=open(sort, 'w')
f=0
for e in b:
    c.write('{}{}: {}{}\n'.format(' '*(2-(len(str(f)))), f, ' '*(3-(len(str(e)))), e))
    f+=1
c.close()

