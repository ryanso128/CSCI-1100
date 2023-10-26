# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:10:18 2022

@author: ryani

this is the tourists class. it takes it's coordinates

"""
class tourist(object):
    
    def __init__(self, x, y):
        #x location
        self.x=x
        #y location
        self.y=y
        #asks if the tourists is still here
        self.left=False
        #keeps a counter for the number of turns it hasn't seen a bear
        self.bear_turns=0
        #keeps a counter for the number of bears it sees
        self.bear_num=0
    
    #print out a formated string whenever you print a tourists class
    
    def __str__(self):
        return 'Tourist at ({},{}), {} turns without seeing a bear.'\
            .format(self.x, self.y, self.bear_turns)
