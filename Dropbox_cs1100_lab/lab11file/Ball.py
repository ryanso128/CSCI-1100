# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:20:25 2022

@author: ryani
"""

class Ball(object):
    
    def __init__(self, x, y, dx, dy, radius, color):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.radius = radius
        self.color = color
    
    def __str__(self):
        return '{}{}'.format(self.x, self.y)
    
    
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
    
    def bounding_box(self):
        x0=self.x-self.radius
        y0=self.y-self.radius
        x1=self.x+self.radius
        y1=self.y+self.radius
        return  (x0, y0, x1, y1)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        x0=self.x-self.radius
        y0=self.y-self.radius
        x1=self.x+self.radius
        y1=self.y+self.radius
        if x0>maxx or y0>maxy or x1<0 or y1<0:
            return False
        return True
    
    def check_reverse(self, maxx, maxy):
        if self.x-self.radius<=0 or self.x+self.radius>=maxx:
            self.dx=-self.dx
            
        if self.y-self.radius<=0 or self.y+self.radius>=maxy:
            self.dy=-self.dy