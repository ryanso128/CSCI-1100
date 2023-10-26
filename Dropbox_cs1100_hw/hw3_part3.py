# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:18:46 2022

@author: ryani

calculates the number of bears, berry area, and tourist for the next 10 years

"""
#improt math

import math

#define the minimum and maximum of bear, berry area and tourist in 10 years

def minmax(l):
    n=min(l)
    x=max(l)
    return n, x

#calculates the number of tourist, and the next year's bears and berry area

def find_next(bear, berry, tourist):
    i=0
    bearlist=[]
    berrylist=[]
    tourlist=[]
    while i<10:
        year=(i+1)
        if bear<=10 and bear>=4:
            tourist=10000*int(bear)
        elif bear>10 and bear<=15:
            tourist=(10000*10)+(20000*(int(bear)-10))
        else:
            tourist=0
        print('{}\t     {}\t       {:.1f}\t  {}'.format(year, bear, berry, tourist))
        bearlist.append(bear)
        berrylist.append(berry)
        tourlist.append(tourist)
        #uses given equations to calculate number of bears and berry area for next
        #year
        
        bear_next = berry/(50*(bear+1)) + bear*0.60 - (math.log(1+tourist,10)*0.1)
        berry_next = (berry*1.5) - (bear+1)*(berry/14) - \
            (math.log(1+tourist,10)*0.05)
        bear=math.floor(bear_next)
        
        #checks if the values are less than 0
        
        if bear<0:
            bear=0
        berry=berry_next
        if berry<0:
            berry=0
        i+=1
    return bearlist, berrylist, tourlist


#ask user for number of bears and berry area

bear=input('Number of bears => ').strip()
print(bear)
bear=int(bear)
berry=input('Size of berry area => ').strip()
print(berry)
berry=float(berry)
print('Year     Bears     Berry     Tourists')    

#set tourist equal to 0 and use the find_next function
  
tourist=0
x=find_next(bear, berry, tourist)


#uses mixmax defined function to find min and max of the 10 years 

br=minmax(x[0])
by=minmax(x[1])
tr=minmax(x[2])

#prints

print('\n'
      'Min:\t {}\t       {:.1f}\t  {}\n'
      'Max:\t {}\t       {:.1f}\t  {}'
      .format(br[0], by[0], tr[0], br[1], by[1], tr[1]))
    






