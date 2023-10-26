# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:29:42 2022

@author: ryani

User inputs the radius of the gum balls and how many sales happen per week.
It calculates the number of gum balls on the length, the length of each side, 
the number of expected sales, the number of extra balls needed to fill up the
machine, amount of space wasted when there are an expected amount of balls and
when the extra balls are placed.

"""

import math

#a fuction to calculate the volume of a sphere
def find_volume_sphere(radius):
    return((4/3)*math.pi*radius**3)

#a function to calculate the volume of a cube
def find_volume_cube(side):
    return(side**3)

#asks user to input the radius and the number of weekly sales
radius=input('Enter the gum ball radius (in.) => ').strip()
print(radius)
radius=float(radius)
sales=input('Enter the weekly sales => ').strip()
print(sales)
sales=float(sales)

#calculates the number of balls on the length of the cube
edgeballs=math.ceil((1.25*sales)**(1/3))

#calculates the length of the cube using previous value
sidelen=radius*2*edgeballs

#calculates the number of extra balls using the edgeballs variable
extraballs=(find_volume_cube(edgeballs))-(1.25*sales)

#finds the volume of a single gum ball
x=find_volume_sphere(radius)

#calculates the wasted space when putting enough gum balls for the week
wastedspace=(find_volume_cube(sidelen))-(x*math.ceil(1.25*sales))

#calculates the wasted space if the whole cube was filled with gum balls
extraballspace=(find_volume_cube(sidelen))-(x*extraballs+x*1.25*sales)
print('\n', end='')

#prints the text
print('The machine needs to hold {} gum balls along each edge.\n'
      'Total edge length is {:.2f} inches.\n'
      'Target sales were {}, but the machine will hold {:.0f} extra gum balls.\n'
      'Wasted space is {:.2f} cubic inches with the target number of gum balls,\n'
      'or {:.2f} cubic inches if you fill up the machine.'
      .format(edgeballs, sidelen, math.ceil(sales*1.25), math.floor(extraballs), wastedspace, extraballspace))

