# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:53:35 2022

@author: ryani

User inputs sentence and counts the number of happy and sad words. Then its
takes those inputs and decides whether it is happy, sad, or neutral.

"""
#counts number of happy words
def number_happy(sentence):
    a=sentence.count('laugh')
    b=sentence.count('happiness')
    c=sentence.count('love')
    d=sentence.count('excellent')
    e=sentence.count('good')
    f=sentence.count('smile')
    return (a+b+c+d+e+f)

#counts number of sad words
def number_sad(sentence):
    a=sentence.count('bad')
    b=sentence.count('sad')
    c=sentence.count('terrible')
    d=sentence.count('horrible')
    e=sentence.count('problem')
    f=sentence.count('hate')
    return(a+b+c+d+e+f)

#asks user to input sentence
sentence=input('Enter a sentence => ').strip()
print(sentence)

#puts all the letters in the sentence into lowercase
lower=sentence.lower()

#uses the functions above and calculates the number of happy and sad words
x=number_happy(lower)
y=number_sad(lower)

#adds a sentiment value by addind "+" and "-" signs
sentiment='+'*x+'-'*y

#checks whether the sentiment is more postitive or negative tells the program
#to input happy, sad, or neutral into the print.
if x>y:
    z='happy'
elif x<y:
    z='sad'
elif x==y:
    z='neutral'
print('Sentiment: {}\n'
      'This is a {} sentence.'
      .format(sentiment, z))