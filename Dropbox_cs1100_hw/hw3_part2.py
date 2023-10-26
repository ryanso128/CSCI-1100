# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:32:32 2022

@author: ryani

simulate a pikachu with user inputting number of turns, encounters, and type of
pokemon. 

"""

#the given area the pikachu can be in is 150x150 square

def bounds (b):
    if 0<=b<=150:
        b=b
    elif b<0:
        b=0
    elif b>150:
        b=150
    return b

#this fuction tells pikachu to move based on user input

def move_pokemon(x, y, z):
    z=z.lower()
    if z=='n':
        x-=5
        x=bounds(x)
    elif z=='s':
        x+=5
        x=bounds(x)
    elif z=='w':
        y-=5
        y=bounds(y)
    elif z=='e':
        y+=5
        y=bounds(y)
    else:
        x+=0
    return x, y

#this function tells pikachu to move based on the type of pokemon it encounters

def battle(x, y, z, t):
    t=t.lower()
    z=z.lower()
    
    #if ground, then lose
    if t=='g':
        if z=='n':
            x+=10
            x=bounds(x)
        elif z=='s':
            x-=10
            x=bounds(x)
        elif z=='w':
            y+=10
            y=bounds(y)
        elif z=='e':
            y-=10
            y=bounds(y)
        n='Lose'
        m='runs away'
    
    #if water, then win
    
    elif t=='w':
        if z=='n':
            x-=1
            x=bounds(x)
        elif z=='s':
            x+=1
            x=bounds(x)
        elif z=='w':
            y-=1
            y=bounds(y)
        elif z=='e':
            y+=1
            y=bounds(y)
        n='Win'
        m='wins and moves'
    
    #if neither, nothing happens
    
    else:
        n='No Pokemon'
        m=0
    return x, y, n, m
       
#takes user input with the number of turns, name, and how many enounters 

turn=int(input('How many turns? => ').strip())
print(turn)
name=input('What is the name of your pikachu? => ').strip()
print(name)
encounters=int(input('How often do we see a Pokemon (turns)? => ').strip())
print(encounters)

#start of simulation with pikachu being in the center, (75, 75)

print('\nStarting simulation, turn 0 {} at (75, 75)'.format(name), end='\n')

#the while loop asks user to move pikachu n, s, e, and w and asking what
#pikachu will encounter. Water, ground, or somethign else

i=0
cords=(75, 75)
result=[]
while i<(turn//encounters) and turn!=0 and (turn//encounters)!=0:
    j=0    
    
    #asks user to input the direction pikachu will take
    
    while j<encounters:
        direction=input('What direction does ' + name + ' walk? => ').strip()
        print(direction, end='\n')
        cords=move_pokemon(cords[0], cords[1], direction)
        j+=1
   
    #battles and will move based on the type of pokemon 
   
    print('Turn {}, {} at ({}, {})'.format((i+1)*encounters, name, cords[0], cords[1]), end='\n')
    typing=input('What type of pokemon do you meet (W)ater, (G)round? => ').strip()
    print(typing, end='\n')
    after=battle(cords[0], cords[1], direction, typing)
    result.append(after[2])
    cords=(after[0], after[1])
    if typing.lower()=='w' or typing.lower()=='g':
        print('{} {} to ({}, {})'.format(name, after[3], cords[0], cords[1]), end='\n')
    else:
        i+=0
    i+=1

#if there are extra turns to take but no more encounters, the turns happen here

if (turn%encounters)>0:
      k=0    
      while k<(turn%encounters):
          direction=input('What direction does ' + name + ' walk? => ').strip()
          print(direction, end='\n')
          cords=move_pokemon(cords[0], cords[1], direction)
          k+=1  

#prints out where the pikachu will end up and the end

print('{} ends up at ({}, {}), Record: {}'.format(name, cords[0], cords[1], result))