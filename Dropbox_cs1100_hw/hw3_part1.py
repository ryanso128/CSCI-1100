# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:07:58 2022

@author: ryani

Given a paragprah, what are the hard words in the text, the statistics and 
reability of the text.

"""
#import the file syllabes then change it to the letter s because it is easier 
#to write one letter than to write 9

import syllables as s

#ask user to input text

para=input('Enter a paragraph => ')
print(para)

#split up the text into different sections

x=para.split('. ')
y=para.split()

#value of the stat ASL

ASL=len(y)/len(x)

#check each word in text to see if they are hard with given conditions and set
#to variable PHW

i=0
PHW=[]
while i<len(y):
    d=s.find_num_syllables(y[i])
    a=not (y[i][-1]=='e' and y[i][-2]=='d')
    b=not (y[i][-1]=='e' and y[i][-2]=='d')
    c=not (y[i].count('-')>0)
    if d>=3 and a and b and c:
        PHW.append(y[i])
        i+=1
        a=0
        b=0
        c=0
    else:
        i+=1
        a=0
        b=0
        c=0

#percentage of words that are hard in given text

PHWp=(len(PHW)/len(y))*100

#find the average syllables and set variable to ASYL

j=0
e=0
while j<len(y):
    e+=s.find_num_syllables(y[j])
    j+=1
ASYL=e/len(y)

#set GFRI and FKRI values to their respective variables with given equations

GFRI=0.4*(ASL+PHWp)
FKRI=206.835-1.015*ASL-86.4*ASYL

#print out using format

print('Here are the hard words in this paragraph:\n'
      '{}\n'
      'Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}\n'
      'Readability index (GFRI): {:.2f}\n'
      'Readability index (FKRI): {:.2f}'
      .format(PHW, ASL, PHWp, ASYL, GFRI, FKRI))





