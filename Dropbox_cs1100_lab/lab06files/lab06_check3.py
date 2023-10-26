# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 00:22:26 2022

@author: ryani
"""

import lab06_util
def ok_to_add(a, x, y, z):
    c=False
    d=False
    e=False
    if not (0<y<9 and 0<z<9):
        c=True
    else:
        i=[]
        for h in a[y]:
            i.append(h)
        i.pop(y)
        for ab in i:
            if ab==x:
                c=True
        l=[]
        for j in a:
            for k in range(9):
                if k==z:
                    l.append(j[k])
        l.pop(z)
        for m in range(len(l)):
            if x==l[m] and c!=True:
                d=True
                break
        p=[]    
        for n in range(9):
            for o in range(9):
                if (o//3)==(z//3):
                    if (n//3)==(y//3):
                        p.append(a[n][o])
        p.pop(y//3+z//3)
        for b in p:
            if x==b and d!=True and c!=True:
                e=True
                break 
        if a[y][z]==x and not (c==True or d==True or e==True):
            c==False
            d==False
            e==False
    return c, d, e

def verify_board(a):
    for x in a:
        for y in x:
            if y=='.':
                return False
    for d in range(9):
        for e in range(9):
            b=ok_to_add(a, a[d][e], d, e)
            if b[0]==True or b[1]==True or b[2]==True:
                return False
    for f in range(9):
        for g in range(9):
            h=ok_to_add(a, a[f][g], f, g)
            if h[0]==True and h[1]==True and h[2]==True:
                return False
    print('Solved')
    return True

b = input('Unsolved board: ')
a=lab06_util.read_sudoku(b)
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

while verify_board(a)==False:
    
    number=input('number: ')
    row=int(input('row: '))
    column=int(input('column: '))

    c=ok_to_add(a, number, row, column)
    if c[0]!=True and c[1]!=True and c[2]==False:
        a[row][column]=number
    else: 
        print('This number cannot be added')
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
    if verify_board(a)==True:
        break



