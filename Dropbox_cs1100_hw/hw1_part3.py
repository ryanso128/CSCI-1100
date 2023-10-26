# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:44:51 2022

@author: ryani

Creates a box using user inputed character, width and height, and displays the 
the dimensions in the center.
"""

character=input('Enter frame character ==> ').strip()
print(character)
height=input('Height of box ==> ').strip()
print(height)
width=input('Width of box ==> ').strip()
print(width)
d=int(float(width)%2)
y=width+'x'+height
a=((int(width)/2)-(int((len(y)+3-d)/2)))
b=((int(width)/2)-(int((len(y)+1)/2)))
print('\n','Box:', sep='')
print(character*int(width),'\n',
      (character+(' '*(int(width)-2))+character+'\n')*int((int(height)-3)/2),
      character+(' '*int(a))
      +y+
      (' '*int(b))+character,'\n',
      (character+(' '*(int(width)-2))+character+'\n')*int((int(height)-2)/2), 
      (character*int(width)), sep='')