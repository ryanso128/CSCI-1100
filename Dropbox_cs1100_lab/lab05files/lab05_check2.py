# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:02:23 2022

@author: ryani
"""
import lab05_util
def print_info(x):
    if x<0:
        print('error')
    else:    
        restaurants = lab05_util.read_yelp('yelp.txt')
        x=restaurants[x]
        y=x[3].split('+')
        a=sorted(x[-1])
        i=0
        j=0
        while i<len(x[-1]):
            j+=a[i]
            i+=1
        if len(a)>3:        
            b=(j-max(a)-min(a))/(len(a)-2)
        else:
            b=j/3
    
        if len(y)<3:
            z=y[1].split(',')
            print('{} ({})\n'
                  '         {}\n'
                  '         {}, {}\n'
                  'Average score: {:.1f}'
                  .format(x[0],x[5], y[0], z[0], z[1], b))
        else:
            z=y[2].split(',')
            print('{} ({})\n'
                  '         {}\n'
                  '         {}\n'
                  '         {}, {}\n'
                  'Average score: {:.1f}'
                  .format(x[0], x[5], y[1], y[0], z[0], z[1], j))
        if b<=2:
            print('THis restruant is rated bad, based on {} reviews'.format(len(a)))
        elif 2<b<=3:
            print('THis restruant is rated average, based on {} reviews'.format(len(a)))
        elif 3<b<=4:
            print('THis restruant is rated above average, based on {} reviews'.format(len(a)))
        elif 4<b<=5:
            print('THis restruant is rated very good, based on {} reviews'.format(len(a)))
    
        
idd=int(input('Enter restruant id => '))
idd-=1
print_info(idd)

