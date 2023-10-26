# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 01:10:14 2022

@author: ryani

User inputs a password and gives a score based on it's length, number of digits, use of capitalization, punctuation.
It also gives negative scores if it is a license plate or a common password

"""

#imports top 100 most common passwords
import hw4_util
    
#defines the letters, digits, and punctuation

Letters=['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
Digits='0123456789'
Punctuation=['!@#$', '%^&*']

#gives a score based on the length. 

def length(x):
    y=0
    if 6<=len(x)<=7:
        y=1
    elif 8<=len(x)<=10:
        y=2
    elif len(x)>10:
        y=3
    return y

#gives a score based on the diverse use of cases

def case(x):
    a=0
    b=0
    c=0
    for i in Letters[0]:
        a+=x.count(i)
    for j in Letters[1]:
        b+=x.count(j)
    if a==1 or b==1:
        c=1
    elif a>=2 and b>=2:
        c=2
    return c

#gives a score based on the number of digits used in the password
      
def digits(x):
    j=0
    a=0
    for y in Digits:
        a+=x.count(y)
    if a==1:
        j=1
    elif a>=2:
        j=2
    return j
    
#gives a score based on the number of punctuation used in the password

def punctuation(x):
    f=0
    g=0
    for k in Punctuation[0]:
        f+=x.count(k)
    for l in Punctuation[1]:
        g+=x.count(l)
    h=0
    i=0
    if f>0:
        h=1
    if g>0:
        i=1
    return h, i

#checks if it is similar to a NY license plate and gives a score

def NY_License(x):
    x=x.lower().replace('', ' ').split()
    i=0
    b=0
    while i<len(x):
        j=0
        k=0
        while j<len(Letters[1]):
            if x[i]==Letters[1][j]:
                x[i]=x[i].replace(Letters[1][j], 'h')
                break
            j+=1
        while k<len(Digits):
            if x[i]==Digits[k]:
                x[i]=x[i].replace(Digits[k], '0')
                break
            k+=1
        i+=1
    x=''.join(x)
    a=x.find('hhh0000')
    if a>-1:
        b=-2
    return b
            
#checks if the user's password is in the top 100 most common passwrods and gives a score
    
def Common_Password(x):
    x=x.lower()
    n=hw4_util.part1_get_top()
    i=0
    o=0
    while i<len(n):
        if n[i]==x:
            o=-3
        i+=1
    return o

#adds up all the scores and rates it based on the total score recieved 
    
def score (a, b, c, d, e, f, g):
    g=a+b+c+d+e+f+g
    if g<=0:
        h='rejected'
    elif 1<=g<=2:
        h='poor'
    elif 3<=g<=4:
        h='fair'
    elif 5<=g<=6:
        h='good'
    elif 7<=g:
        h='excellent'
    return g ,h

#asks user to input a password

password=input('Enter a password => ')
print(password)

#inputs password into all the functions lsited above

a=length(password)
b=case(password)
c=digits(password)
d=punctuation(password)
e=NY_License(password)
f=Common_Password(password)
g=score(a, b, c, d[0], d[1], e, f)

#asks if each criteria was necessary to print out. Then prints out total score and the rating of the password

if a>0:
    print('Length: +{:.0f}'.format(a))
if b>0:
    print('Cases: +{:.0f}'.format(b))
if c>0:
    print('Digits: +{:.0f}'.format(c))
if d[0]>0:
    print('!@#$: +{:.0f}'.format(d[0]))
if d[1]>0:
    print('%^&*: +{:.0f}'.format(d[1]))
if e<0:
    print('License: {:.0f}'.format(e))
if f<0:
    print('Common: {:.0f}'.format(f))
print('Combined score: {:.0f}'.format(g[0]))
print('Password is {}'.format(g[1]))
    
   