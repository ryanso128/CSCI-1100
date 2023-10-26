# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:11:31 2022

@author: ryani

given a week the user has inputed, it asks the user what it wants to do and
which state they want to check. if the user gives a input that is out of the 
list or is unrecognized, it will give an error. when the user inputs a negative
week, it will end the code.

"""

import hw4_util

#test if the given state is part of the list of states

def unknown(y):
    x=hw4_util.part2_get_week(index)
    for z in range(len(x)):
        if y==x[z][0]:
            j=0
            break
        else:
            j=1
    return j

#does the calculations for number of cases per 100,000 people

def daily(x, y):
    i=0
    k=0
    j=0
    while i<len(x):
        if y==x[i][0]:
            while j<7:
                k+=x[i][j+2]
                j+=1
            break
        i+=1
    l=(k/7)/(float(x[i][1])/100000)
    return l

#does the calculations for percent of positive cases out of all cases

def pct(x, y):
    i=0
    k=0
    l=0
    while i<len(x):
        if state==x[i][0]:
           k=x[i][2]+x[i][3]+x[i][4]+x[i][5]+x[i][6]+x[i][7]+x[i][8]
           l=x[i][9]+x[i][10]+x[i][11]+x[i][12]+x[i][13]+x[i][14]+x[i][15]
        i+=1
    m=(k/(k+l))*100
    return m

#gives states that are considered quarantined

def quar(x):
    i=0
    j=[]
    g=[]
    k=0
    l=0
    m=0
    n=0
    while i<len(x):
        k=x[i][2]+x[i][3]+x[i][4]+x[i][5]+x[i][6]+x[i][7]+x[i][8]
        l=x[i][9]+x[i][10]+x[i][11]+x[i][12]+x[i][13]+x[i][14]+x[i][15]
        m=(k/7)/(float(x[i][1])/100000)
        n=(k/(k+l))*100
        if m>10 or n>10:
            j.append(x[i][0])
            g.append(m)
        i+=1
    return j, g

#returns the state with the highest cases per 100,000 people

def high(x):
    i=0
    j=[]
    k=0
    m=0
    while i<len(x):
        k=x[i][2]+x[i][3]+x[i][4]+x[i][5]+x[i][6]+x[i][7]+x[i][8]
        m=(k/7)/(float(x[i][1])/100000)
        j.append((m, x[i][0]))
        i+=1
    n=0
    o=0
    p=0
    while n<len(j):
        if o<j[n][0]:
            o=j[n][0]
            p=j[n][1]
            n+=1
        elif int(o)>=j[n][0]:
            n+=1
    return p

#asks user for the week they want to index

print('...')
index=int(input('Please enter the index for a week: ').strip())
print(index)

#loops all functions until user inputs a negative week

while index>0:
    
    #if the user inputs a week that is out of the list's range and is positive,
    #give the error message
    
    if index>29:
        print('No data for that week')
        print('...')
        index=int(input('Please enter the index for a week: ').strip())
        print(index)
        
    #if the user gives a week in the given list, continue
    
    else:
        while 29>index>0:
            x=hw4_util.part2_get_week(index)
            
            #asks user what they want to do with the index
            
            request=input('Request (daily, pct, quar, high): ').strip()
            print(request)
            request=request.lower()
            
            #goes to daily function and if the state isn't part of list,
            #print out the state is not found
            
            if request=='daily':
                state=input('Enter the state: ').strip()
                state=state.upper()
                print(state)
                z=unknown(state)
                if z==1:
                    print('State {} not found'.format(state))
                elif z==0: 
                    y=daily(x, state)
                    print('Average daily positives per 100K population: {:.1f}'.format(y))
            
            #go to pct function. if the state isn't part of the list, 
            #print out the state is not found
            
            elif request=='pct':
                state=input('Enter the state: ').strip()
                state=state.upper()
                print(state)
                z=unknown(state)
                if z==1:
                    print('State {} not found'.format(state))
                else: 
                    y=pct(x, state)
                    print('Average daily positive percent: {:.1f}'.format(y))
            
            #gives a list of all quarantined states given a week
            
            elif request=='quar':
                y=quar(x)
                print('Quarantine states:')
                hw4_util.print_abbreviations(y[0])
                
            #given a week, give the highest number of case per 100,000 people
            #and the state corresponded to it
                
            elif request=='high':
                y=quar(x)
                z=max(y[1])
                a=high(x)
                print('State with highest infection rate is {}\n'
                      'Rate is {:.1f} per 100,000 people'.format(a, z))
            
            #if the user inputs a request that isn't one of the 4, print an 
            #error
            
            else: 
                print('Unrecognized request')
                
            #ask the user for the index again to loop this code
            
            print('...')
            index=int(input('Please enter the index for a week: ').strip())
            print(index)

          
        
