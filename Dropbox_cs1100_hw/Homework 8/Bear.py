# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:10:18 2022

@author: ryani

this is the bear class. it takes a coodinate, and direction it is traveling

"""

class bear(object):
    def __init__(self, x, y, direction):
        #x location
        self.x=x
        #y location
        self.y=y
        #direction it is traveling
        self.direction=direction
        #checks if it is sleeping
        self.sleep=False
        #check for how many more turns it needs to sleep
        self.sleep_turns=0
        #checks it to stop
        self.stop=False
        
    #if asked to print the bear class, print out a formated string depedning
    #on whether it is asleep or not
    
    def __str__(self):
        if self.sleep!=False:
            return 'Bear at ({},{}) moving {} - Asleep for {} more turns'\
                .format(self.x, self.y, self.direction, self.sleep_turns)
        return 'Bear at ({},{}) moving {}'.format(self.x, self.y, self.direction)
    
    #change the x and y coords based on the direction it is moving in
    
    def moving(self):
        direction=self.direction
        if 'N' in direction:
            self.x-=1
        if 'W' in direction:
            self.y-=1
        if 'S' in direction:
            self.x+=1
        if 'E' in direction:
            self.y+=1