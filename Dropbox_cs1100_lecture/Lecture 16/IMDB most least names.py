# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:17:45 2022

@author: ryani
"""

file=input('Enter the name of the IMDB file ==> ').strip()
print(file)
counts=dict()
for line in open(file, encoding='ISO-8859-1'):
    words=line.strip().split('|')
    name=words[0].strip()
    if name in counts:
        counts[name]+=1
    else:
        counts[name]=1
x=max(counts.values())
least=0
for names in counts:
    occurances=counts[names]
    if occurances==x:
        largest=names
    if occurances==1:
        least+=1
print('{} appears most often: {} times'.format(largest, x))
print('{} people appear once'.format(least))

#names=sorted(counts)
#limit=min(100, len(names))
#for index in range(limit):
#    name=names[index]
#    print('{} appeared in {} movies'.format(name, counts[name]))
    


