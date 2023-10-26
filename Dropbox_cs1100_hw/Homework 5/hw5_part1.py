# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:04:12 2022

@author: ryani
"""

import hw5_util

#This funtion relates to the get_nbrs function, asking if the input coords are 
#in bounds

def if_in_bound(x, y, z):
    if not (y>x[0]>=0 and z>x[1]>=0):
        x=0
    return x

#get the neighbors of inputted coords and ask if it is in bounds.

def get_nbrs(x, y, e, f):
    a=(x-1, y)
    b=(x, y-1)
    c=(x, y+1)
    d=(x+1, y)
    a=if_in_bound(a, e, f)
    b=if_in_bound(b, e, f)
    c=if_in_bound(c, e, f)
    d=if_in_bound(d, e, f)
    return a, b, c, d

#ask the user to input a number from 1 to 3. Anything else and it will keep
#looping until a valid number is inputted.

n=int(input('Enter a grid index less than or equal to 3 (0 to end): ').strip())
print(n)
while n<1 or n>3:
    n=int(input('Enter a grid index less than or equal to 3 (0 to end): ').strip())
    print(n)
    
#after getting the grid, ask if the grid wants to be printed.

a=hw5_util.get_grid(n)
printed=input('Should the grid be printed (Y or N): ')
print(printed)
printed=printed.lower()

#If the user wants it to be printed, it will print formatted correctly

if printed=='y':
    print('Grid {}'.format(n))
    for x in a:
        for z in x:
            print('{}{}'.format(' '*(4-len(str(z))), z), end='')
        print('\n', end='')
        
#print the number of rows and colums in the given grid

print('Grid has {} rows and {} columns'.format(len(a), len(a[0])))

#after getting the start locations, use the get_nbrs and get the neighbors.

b=hw5_util.get_start_locations(n)
for w in b:
    v=list(get_nbrs(int(w[0]), int(w[1]), len(a), len(a[0])))
    u=v.count(0)
    for q in range(u):
        v.remove(0)
    v=str(v)
    
    #change the list into a string and remove pieces of it to get desired format
    
    v=v.replace('[',' ').replace(',', ' ').replace(']', ' ').replace('  ', ',').replace('),(', ') (').replace(',', ', ').strip(' ')
    print('Neighbors of {}: {}'.format(w, v))

#get path  and for each coord in the get path list, find its neighbor and
#then match it with the previous coord in the path list. Append into another list

c=hw5_util.get_path(n)
j=[]
for t in range(len(c)-1):
    s=get_nbrs(c[t+1][0], c[t+1][1], len(a), len(a[0]))
    for r in s:
        if c[t]==r:
            j.append(c[t])
            break

#check if the original path list is the same as the checked path list. If not, 
#find the index where it isn't and print the 2 coords where they dont match

i=0
while i<len(j):
    if c[i]!=j[i]:
        print('Path: invalid step from {} to {}'.format(c[i], c[i+1]))
        h=1
        break
    else:
        h=0
    i+=1

#if the previous was false, then print valid path and the amount you went up and
#down

if h==0:
    neg=[]
    pos=[]
    o=0    
    for p in range(len(c)-1):
        o=a[c[p+1][0]][c[p+1][1]]-a[c[p][0]][c[p][1]]
        if o>0:
            pos.append(o)
        elif o<0:
            neg.append(o)
    m=sum(pos)
    l=abs(sum(neg))
    print('Valid path\n'
          'Downward {}\n'
          'Upward {}'
          .format(l, m))