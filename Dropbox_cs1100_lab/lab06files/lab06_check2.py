# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 00:22:26 2022

@author: ryani
"""

def ok_to_add(a, x, y, z):
    if not (0<y<9 and 0<z<9):
        print('This number cannot be added')
    else:
        c=0
        d=0
        e=0
        for h in a[y]:
            if x==h:
                print('This number cannot be added')
                c=1
                break
        l=[]
        for j in a:
            for k in range(9):
                if k==z:
                    l.append(j[k])
        for m in range(len(l)):
            if x==l[m] and c!=1:
                print('This number cannot be added')
                d=1
                break
        p=[]    
        for n in range(9):
            for o in range(9):
                if (o//3)==(z//3):
                    if (n//3)==(y//3):
                        p.append(a[n][o])
        for b in p:
            if x==b and d!=1 and c!=1:
                print('This number cannot be added')
                e=1
                break
        if c!=1 and d!=1 and e!=1:
            a[y][z]=x

a = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]



number=input('number: ')
row=int(input('row: '))
column=int(input('column: '))

ok_to_add(a, number, row, column)
print('-'*24)
for x in range(len(a)):
    for d in range(len(a[x])):
        if d%3==2:
            e=' | '
        else:
            e=' '
        if x%3==2 and d==8:
            f='\n'+'-'*24
        else:
            f=''
        if d==8:
            g='\n'
        else:
            g=''
        if d==0:
            h='|'
        else:
            h=''
        print('{}{}{}{}{}'.format(h, a[x][d], e, f, g), end='')



