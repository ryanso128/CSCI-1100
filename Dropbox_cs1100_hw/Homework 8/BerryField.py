# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:10:17 2022

@author: ryani

takes in a list of list of numbers, a list of classes of bears and list of classes
of tourists

"""

#imports necessary files

from Bear import bear
from Tourist import tourist
class berry(object):
    
    def __init__(self, field, bears, tourists):
        #takes the a list of lists
        self.field=field
        #takes a list of classes of bears
        self.bears=bears
        #takes a list of classes of tourists
        self.tourists=tourists
        
    def __str__(self):
        grid=''
        
        for rows in range(len(self.field)):
            for columns in range(len(self.field[0])):
                x=''
                #for each bear, check if the location of the grid is the same as
                #the location of the bear. if true, set x equal to B
                for bears in self.bears:
                    if bears.x==rows and bears.y==columns:
                        x='B'
                #for each tourists, check if the location of the grid is the same
                #as the location of the toursists. if x is already b, set it to x.
                #otherwise, set x to T
                for tourists in self.tourists:
                    if tourists.x==rows and tourists.y==columns:
                        if x=='B':
                            x='X'
                        else:
                            x='T'
                #if x is not a blank string, add it to grid, formatted
                if x!='':
                    grid+='{: >4}'.format(x)
                #else, add the berry to the grid, formatted
                else:
                    grid+='{: >4}'.format(self.field[rows][columns])
            grid+='\n'
        return grid
    
    #this is what grows the berries
    
    def growing(self):
        
        #for each berry that isn't a 0 or a 10, add one to it, growing it
        
        for rows in range(len(self.field)):
            for columns in range(len(self.field[0])):
                if 0<self.field[rows][columns]<10:
                    self.field[rows][columns]+=1
        
        #checks if its neighbors have 10 berries. If true, add 1. This only works
        #if the location of the berry is already 0
        
        for rows in range(len(self.field)):
            for columns in range(len(self.field[0])):
                if self.field[rows][columns]==0 and 0<=rows-1<=len(self.field)-1:
                    if self.field[rows-1][columns]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=columns+1<=len(self.field[0])-1:
                    if self.field[rows][columns+1]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=rows+1<=len(self.field)-1:
                    if self.field[rows+1][columns]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=columns-1<=len(self.field[0])-1:
                    if self.field[rows][columns-1]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=rows-1<=len(self.field)-1 and 0<=columns-1<=len(self.field[0])-1:
                    if self.field[rows-1][columns-1]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=rows-1<=len(self.field)-1 and 0<=columns+1<=len(self.field[0])-1:
                    if self.field[rows-1][columns+1]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=rows+1<=len(self.field)-1 and 0<=columns+1<=len(self.field[0])-1:
                    if self.field[rows+1][columns+1]==10:
                        self.field[rows][columns]+=1
                if self.field[rows][columns]==0 and 0<=rows+1<=len(self.field)-1 and 0<=columns-1<=len(self.field[0])-1:
                    if self.field[rows+1][columns-1]==10:
                        self.field[rows][columns]+=1
    
    #counts the number of berries on the field
    
    def count(self):
        total=0
        for rows in self.field:
            total+=sum(rows)
        return total