# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:30:11 2022

@author: ryani

Compares Dale's, Erin's, and Sam's height and lists them higheset to lowest
"""
#takes inputs and list them from lowest to highest
def list(x, y, z):
    i=0
    a=[]
    while i<3:
        a.append(x)
        x=y
        y=z
        i+=1
    y=sorted(a)
    return y
#asks user for the heights of Dale, Erin, and Sam
hd=input('Enter Dale\'s height: ').strip()
print(hd)
he=input('Enter Erin\'s height: ').strip()
print(he)
hs=input('Enter Sam\'s height: ').strip()
print(hs)
#sets a variable to the list of ordered heights
a=list(hd, he, hs)
#takes the height and matches them to the correct person with a loop
i=0
b=[]
while i<3:
    if a[i]==hd:
        b.append('Dale')
    elif a[i]==he:
        b.append('Erin')
    elif a[i]==hs:
        b.append('Sam')
    i+=1
#prints out the names ordered from highest to lowest in a column 
print('{}\n'
      '{}\n'
      '{}'.format(b[2], b[1], b[0]))


