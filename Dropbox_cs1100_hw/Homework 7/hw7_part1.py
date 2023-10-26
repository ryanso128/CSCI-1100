# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:19:22 2022

@author: ryani

given a dictionary, words and keystrokes, find whether the words are valid
in the dictionary or some adjustments must be made in order to return a valid 
word. otherwise return not found

"""

def in_dicitonary(word, dic, key):
    word=word.strip()
    alpha='abcdefghijklmnopqrstuvwxyz'
    
    #code for if the word is found in dictionary, instantly return FOUND
    
    in_dic=word in dic
    if in_dic==True:
        return '{}{} -> FOUND'.format(' '*(15-len(word)),word)
    possible=set()
    word=list(word)
    
    #code for if each letter was dropped. If in dictionary, add it to the possible set
    #with the number of how common it appears.
    
    for letter in range(len(word)):
        ori=word[letter]
        word[letter]=''
        new_word=''.join(word)
        in_dic=new_word in dic
        if in_dic==True:
            possible.add((dic[new_word], new_word))
        word[letter]=ori
        
    #code for if every single letter in the alphabet was added to each letter
    #in between. If true, add it to the possible set with the number
    
    for place in range(len(word)+1):        
        for char in alpha:
            word.insert(place, char)
            new_word=''.join(word)
            in_dic=new_word in dic
            if in_dic == True:
                possible.add((dic[new_word], new_word))
            word.pop(place)
    
    #code for swapping characters with their neighbors. If valid in dictionary,
    #add it to the set
    
    for num in range(len(word)-1):
        char1=word[num]
        char2=word[num+1]
        word[num]=char2
        word[num+1]=char1
        word=''.join(word)
        in_dic=word in dic
        if in_dic == True:
            possible.add((dic[word], word))
        word=list(word)
        word[num]=char1
        word[num+1]=char2
    
    #repalces each letter in the word with a potential keystroke and checks
    #if valid in the dictionary. if valid, add it to the set with the number
        
    for num in range(len(word)):
        for keyboard in key[word[num]]:
            original=word[num]
            word[num]=keyboard
            word=''.join(word)
            in_dic=word in dic
            if in_dic == True:
                possible.add((dic[word], word))
            word=list(word)
            word[num]=original
    word=''.join(word)
    
    #depending on the length of the set, return differnt strings.
    
    #if 0, then no words were found so return not found
    
    if len(possible)==0:
        return '{}{} -> NOT FOUND'.format(' '*(15-len(word)),word)
    possible=sorted(list(possible), reverse=True)
    
    #if 1 word was found, return just the one word
    
    if len(possible)==1:
        return '{}{} -> FOUND  {}:  {}'.format(' '*(15-len(word)),word, len(possible), possible[0][1])
    
    #if 2 words were found, return the 2 words
    
    elif len(possible)==2:
        return '{}{} -> FOUND  {}:  {} {}'.format(' '*(15-len(word)),word, len(possible), possible[0][1], possible[1][1])
    
    #if 3 or more, return the 3 most common words.
    
    else:
        return '{}{} -> FOUND{}{}:  {} {} {}'.format(' '*(15-len(word)),word, ' '*(3-len(str(len(possible)))), len(possible), possible[0][1], possible[1][1], possible[2][1])
    
#guard

if __name__=='__main__':
    
    #ask user for dictionary, input, and keyboard files
    
    dict_file=input('Dictionary file => ').strip()
    print(dict_file)
    input_file=input('Input file => ').strip()
    print(input_file)
    key_file=input('Keyboard file => ').strip()
    print(key_file)
    
    #add a dictionary dictionary and a keyboard dictionary
    
    dic=dict()
    key=dict()
    
    #open all three files
    
    dict_file=open(dict_file).read().strip().split('\n')
    input_file=open(input_file).read().strip().split('\n')
    key_file=open(key_file).read().strip().split('\n')
    
    #format the dictionary and keyboard file so they can fit into their respective
    #dictionary
    
    for word in dict_file:
        word=word.strip().split(',')
        dic[word[0]]=word[1]
    for letter in key_file:
        letter=letter.strip().split()
        first=letter.pop(0)
        key[first]=letter
        
    #for each word in the input, put it through the function in_dictionary 
    #which will autocorrect the word and print out the word with potential
    #autocorrct words.
    
    for word in input_file:
        print(in_dicitonary(word, dic, key))
        