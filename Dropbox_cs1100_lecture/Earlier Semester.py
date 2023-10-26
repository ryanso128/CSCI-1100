# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:15:40 2022

@author: ryani

compares which semester comes first given the sesason and year
"""
#checks which year is smaller or which season is sooner with the same year
def earlier_semester(x,y):
    if x[1]<y[1] or (x[1]==y[1] and x[0]>y[0]):
        j='True'
    else:
        j='False'
    return j
        
#variables ar given  
w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)

#print statmements ar given and prints out whcih semester is earlier
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))