# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:10:01 2022

@author: ryani

User inputs a sentence and the program encrypts the sentence and then decrypts
and tells the user whether the decryption was successful or not. 

"""
#a function to encrpyt the string
def encrypt(string):
    a=string.replace(' a', '%4%')
    b=a.replace('he', '7!')
    c=b.replace('e', '9(*9(')
    d=c.replace('y', '*%$')
    e=d.replace('u', '@@@')
    f=e.replace('an', '-?')
    g=f.replace('th', '!@+3')
    h=g.replace('o', '7654')
    i=h.replace('9', '2')
    j=i.replace('ck', '%4')
    return j

#a function to decrypt the previous function
def decrypt(string):
    a=string.replace('%4', 'ck')
    b=a.replace('2', '9')
    c=b.replace('7654', 'o')
    d=c.replace('!@+3', 'th')
    e=d.replace('-?', 'an')
    f=e.replace('@@@', 'u')
    g=f.replace('*%$', 'y')
    h=g.replace('9(*9(', 'e')
    i=h.replace('7!', 'he')
    j=i.replace('%4%', 'a')
    return j

#asks user to input string
encode=input('Enter a string to encode ==> ').strip()
print(encode, '\n')

#encrypts and then decrypts the string
x=encrypt(encode)
y=decrypt(x)

#calculates how much longer is the encrypted string is
z=len(x)-len(encode)

#checks if decrypted and the original string is the same
if y==encode:
    m=' '
else:
    m=' not '
    
#prints
print('Encrypted as ==> {}\n'
      'Difference in length ==> {}\n'
      'Deciphered as ==> {}\n'
      'Operation is{}reversible on the string.'
      .format(x, z, y, m))