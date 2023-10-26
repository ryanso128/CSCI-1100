# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:04:12 2022

@author: ryani

Given starting locations, create a path to the highest elevation, ask if it 
is a global maximum, local maximum, or no maximum based on how high you can 
move per turn.

"""

import hw5_util

#find the highest point

def global_max(x):
    c=[]
    g=[]
    
    i=0
    for a in x:
        for b in a:
            c.append(b)
    d=max(sorted(c))
    for e in x:
        h=0
        for f in e:
            if f==d:
                g.append(i)
                g.append(h)
                break
            h+=1
        i+=1
    return d, g

#ask if the coord is in bound

def if_in_bound(x, y, z):
    if not (y>x[0]>=0 and z>x[1]>=0):
        x=0
    return x

#find the neigbors given the grid and coord

def get_nbrs(x, y, e, f):
    a=[]
    b=[]
    a.append((x-1, y))
    a.append((x, y-1))
    a.append((x, y+1))
    a.append((x+1, y))
    for lst in a:
        if if_in_bound(lst, e, f)!=0:
            b.append(lst)
    return b

#find if there is a higher elevation than the one given or if it is the max

def maximum(grid, max_nbr, globalmax, rows, columns):
    if max_nbr==1:
        y=2
        return y
    elif max_nbr==2:
        y=0
        return y
    nbrs=get_nbrs(max_nbr[1][0], max_nbr[1][1], rows, columns)
    nbr_nbr=[]
    for a in range(len(nbrs)):
        nbr_nbr.append(grid[nbrs[a][0]][nbrs[a][1]])
    for x in nbr_nbr:
        if max_nbr[0]>x:
            y=True
        else:
            y=2
    if max_nbr[0]==globalmax[0] and y==True:
        y=1        
    else:
        y=0
    return y
    
#find the steepest slope with this function

def get_max_nbrs(grid, x, y, row, column, step):
    nbrs=get_nbrs(x, y, row, column)
    nbr_nbr=[]
    total_nbr=0
    j=0
    for a in range(len(nbrs)):
        if (grid[nbrs[a][0]][nbrs[a][1]]-grid[x][y])>step or (grid[nbrs[a][0]][nbrs[a][1]]-grid[x][y])<=0:
            nbr_nbr.append(0)
        else:
            nbr_nbr.append(grid[nbrs[a][0]][nbrs[a][1]])
    for c in nbr_nbr:
        total_nbr+=c
    if total_nbr==0:
        j=1
        return j
    max_nbr=max(sorted(nbr_nbr))
    for b in nbrs:
        if grid[b[0]][b[1]]==max_nbr:
            coords=b
            break
    return max_nbr, coords, nbr_nbr  

#find the most gradual slope with this function

def get_min_nbrs(grid, x, y, row, column, step):
    nbrs=get_nbrs(x, y, row, column)
    nbr_nbr=[]
    total_nbr=0
    coords=0
    j=0
    for a in range(len(nbrs)):
        if (grid[nbrs[a][0]][nbrs[a][1]]-grid[x][y])>step or (grid[nbrs[a][0]][nbrs[a][1]]-grid[x][y])<=0:
            nbr_nbr.append(10000)
        else:
            nbr_nbr.append(grid[nbrs[a][0]][nbrs[a][1]])
    for c in nbr_nbr:
        total_nbr+=c
    if total_nbr==30000:
        j=1
        return j
    if total_nbr%10000==0:
        j=2
        return j
    min_nbr=min(sorted(nbr_nbr))
    for b in nbrs:
        if grid[b[0]][b[1]]==min_nbr:
            coords=b
            break
    return min_nbr, coords, nbr_nbr    

#creates a grid and then replaces each value in the grid with either a number 
#or a period

def path_grid(length, width, coords):    
    grid=[]
    grid_width=[]
    grid_coord=[]
    for x in range(length):
        for y in range(width):
            grid_coord.append(x)
            grid_coord.append(y)
            grid_width.append(grid_coord)
            grid_coord=[]
        grid.append(grid_width)
        grid_width=[]
    j=0
    for c in grid:
        k=0
        for d in c:
            i=0
            for e in coords:                
                if e[0]==d[0] and e[1]==d[1]:
                    i+=1
            if i==0:
                i='.'
            grid[j][k]=i
            k+=1
        j+=1
    return grid

#main code starts

if __name__=='__main__':
    
    #keeps asking for a valid grid number
    
    n=int(input('Enter a grid index less than or equal to 3 (0 to end): ').strip())
    print(n)
    while n<1 or n>3:
        n=int(input('Enter a grid index less than or equal to 3 (0 to end): ').strip())
        print(n)
    
    #ask for the highest elevation one can take
    
    step=int(input('Enter the maximum step height: '))
    print(step)
    
    #get grid
    
    a=hw5_util.get_grid(n)
    
    #ask if the grid should be printed
    
    printed=input('Should the path grid be printed (Y or N): ')
    print(printed)
    printed=printed.lower()
    
    #prints the number of rows and columns
    
    print('Grid has {} rows and {} columns'.format(len(a), len(a[0])))
    
    #get starting locations
    
    b=hw5_util.get_start_locations(n)
    
    #get globla max and print it
    
    c=global_max(a)
    print('global max: ({}, {}) {}'.format(c[1][0], c[1][1], c[0]))
    print('===')
    places_walked=[]
    
    #main part of the for loop
    #loops for every single start location
    
    for x in b:
        print('steepest path')
        print('({}, {}) '.format(x[0], x[1]), end='')
        
        #find the steepest slope
        
        max_nbr=get_max_nbrs(a, x[0], x[1], len(a), len(a[0]), step)
        
        #every time get_max_nbr is used, append it to places_walked
        
        places_walked.append((max_nbr[1][0], max_nbr[1][1]))
        
        #ask if it is the maximum
        
        maxmax=maximum(a, max_nbr, c, len(a), len(a[0]))
        
        #print the max_nbr but formatted until it returns true
        
        print('({}, {}) '.format(max_nbr[1][0], max_nbr[1][1]), end='')        
        s=0
        
        #in the while loop, it does everything until maximum returns true
        
        while maxmax!=True:
            max_nbr=get_max_nbrs(a, max_nbr[1][0], max_nbr[1][1], len(a), len(a[0]), step)            
            maxmax=maximum(a, max_nbr, c, len(a), len(a[0]))
            if max_nbr!=1:
                places_walked.append((max_nbr[1][0], max_nbr[1][1]))
                print('({}, {}) '.format(max_nbr[1][0], max_nbr[1][1]), end='')
            
            #for formatting, enter every 5 prints
            
            if s%5==2:
                print('\n', end='')
            if max_nbr==1:
                break
            s+=1
        
        #if maximum function returns a number, the while loop will end 
        #depending on the number, it will print no max, local max, and local max
        
        if maxmax==2:
            print('\nno maximum', end='')
        elif maxmax==0:
            print('\nlocal maximum', end='')
        elif maxmax==1:
            print('\nglobal maximum', end='')
        
        print('\n...')
        
        #everything is done the same for the gradual step as the top
        
        print('most gradual path')
        print('({}, {}) '.format(x[0], x[1]), end='')
        min_nbr=get_min_nbrs(a, x[0], x[1], len(a), len(a[0]), step)
        places_walked.append((min_nbr[1][0], min_nbr[1][1]))
        maxmax=maximum(a, min_nbr, c, len(a), len(a[0]))
        print('({}, {}) '.format(min_nbr[1][0], min_nbr[1][1]), end='')        
        s=0
        while maxmax!=True:
            min_nbr=get_min_nbrs(a, min_nbr[1][0], min_nbr[1][1], len(a), len(a[0]), step)
            
            maxmax=maximum(a, min_nbr, c, len(a), len(a[0]))
            if s%5==3:
                print('\n', end='')
            if min_nbr!=1 and min_nbr!=2:
                places_walked.append((min_nbr[1][0], min_nbr[1][1]))
                print('({}, {}) '.format(min_nbr[1][0], min_nbr[1][1]), end='')            
            if min_nbr==1 or min_nbr==2:
                break
            s+=1
        if maxmax==2:
            print('\nno maximum')
        elif maxmax==0:
            print('\nlocal maximum')
        elif maxmax==1:
            print('\nglobal maximum')
        print('===')

#using the path grid, print the grid with the grid coords replaced with numbers

print('Path grid')
grid=path_grid(len(a), len(a[0]), places_walked)
for ab in grid:
    for bc in ab:
        print('  {}'.format(bc), end='')
    print('\n', end='')


