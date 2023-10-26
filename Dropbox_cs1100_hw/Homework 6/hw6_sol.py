# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:03:53 2022

@author: ryani
"""

#for each input, removes all characters that aren't in the English alphabet

def char_remove(lst):
    newlst=[]
    for word in lst:
        for char in word:
            if char.isalpha()==False:
                word=word.replace(char, '')
        if word!='':
            newlst.append(word)
    return newlst

#compares 2 list and sees if one is in the other. Only append words that aren't 
#in both lists and that are in original list

def compare_words(lst, stop):
    newlst=[]
    for word in lst:
        x=True
        for words in stop:
            if word==words:
                x=False
        if x!=False:
            newlst.append(word)
    return newlst

#for wach word, finds the length and adds it to total. Then divides by the
#length of the list for the average word length

def avg_word_len(lst):
    tot=0
    for value in lst:
        tot+=len(value)
    return tot/len(lst)

#returns the ratio between the disctint total words to total words. 

def dist_total(sett, lst):
    return len(sett)/len(lst)

#finds the longest length word in a list

def longest_word(lst):
    maxx=0
    for words in lst:
        if len(words)>=maxx:
            maxx=len(words)
    return maxx

#finds the length of each word and indexes each word into its coorsponding place
#in the list

def word_index(wordlst, lst):
    for words in lst:
        wordlst[len(words)-1]=wordlst[len(words)-1]+words+' '
    for strings in wordlst:
        num=wordlst.index(strings)
        if strings=='':
            continue
        else:
            strings=strings.strip().split(' ')
            wordlst[num]=sorted(set(strings))
    return wordlst

#finds all pairs of words based on seperation. For the first nested for loop, 
#it finds all the foward pairs

def distinct_pair(lst, sepp):
    pairs=[]
    for words in lst:
         num=lst.index(words)
         i=0         
         while i<sepp+1 and num+i<len(lst):
             if words==words:
                 i+=1
                 continue
             s=sorted((words, lst[num+i]))
             pairs.append((s[0], s[1]))
             i+=1
   
    #and for this for loop it finds all the backwards pairs and adds them to a
    #list this will be turned into a set and sorted later. 
   
    for numm in range((len(lst)-1), -1, -1):
        j=0
        while j<sepp+1 and (len(lst)-1)-num<(len(lst)-1):
            if lst[numm]==lst[numm-j]:
                j+=1
                continue
            if numm-j<0:
                j+=1
                continue
            so=sorted((lst[numm], lst[numm-j]))
            pairs.append((so[0], so[1]))
            j+=1
    return pairs

#calculates the ratio of distinct pairs to total pairs

def distinct_pair_ratio(lst1, lst2):
    return len(lst1)/len(lst2)

def jaccard(set1 , set2):
    set1=set(set1)
    set2=set(set2)
    return len(set1&set2)/len(set1|set2)

if __name__=='__main__':
    file1=input('Enter the first file to analyze and compare ==> ').strip()
    print(file1)
    file2=input('Enter the second file to analyze and compare ==> ').strip()
    print(file2)
    sepp=int(input('Enter the maximum separation between words in a pair ==> ').strip())
    print(sepp)
    
    #open all files including the stop.txt
    
    a=open(file1)
    b=open(file2)
    stop=open('stop.txt')
    
    #read the file and then lower all the characters then split then into words
    #turning them into lists
    
    a=a.read().lower().split()
    b=b.read().lower().split()
    stop=stop.read().lower().split()
    
    #uses the character remove function for all the lists
    
    lista=char_remove(a)
    listb=char_remove(b)
    liststop=char_remove(stop)
    
    #compares list a and b to the stop list and outputs what isn't into both
    #stop and original list.
    
    compa=compare_words(lista, liststop)    
    
    #finds the average word length, part 1
    
    print('\nEvaluating document {}'.format(file1))
    avga=avg_word_len(compa) 
    print('1. Average word length: {:.2f}'.format(avga))
    
    #finds the ratio between distinct words to total words using fuction
    #dist_total
    
    seta=set(compa)    
    dista=dist_total(seta, compa)
    print('2. Ratio of distinct words to total words: {:.3f}'.format(dista))
    
    #finds how long the longest word is and then creates that many strings.
    #then it uses the word_index function returning a list of lists of strings with
    #words in their coorsponding index based on their length while sorted
    
    print('3. Word sets for document {}:'.format(file1))
    maxxa=longest_word(compa)    
    wordsa=maxxa*['']    
    wordsa=word_index(wordsa, compa)    
    i=1
    for things in wordsa:
        print('{}{}:{}{}:'.format(' '*(4-len(str(i))), i, ' '*(4-len(str(len(things)))), len(things)), end='')
        if things!='':
            if len(things)<=6:
                for values in things:
                    print(' ', values, sep='', end='')
            else:
                print('', things[0], things[1], things[2], '...', things[-3], things[-2], things[-1], end='')
        print('\n', end='')
        i+=1
    
    #use the compa to find pairs based on the seperation for each word using the 
    #distinct pairs fuction
    
    print('4. Word pairs for document {}'.format(file1))
    paira=distinct_pair(compa, sepp)
    lstpaira=paira
    paira=list(sorted(set(paira)))
    print('  {} distinct pairs'.format(len(paira)))
    if len(paira)<=10:
        for pair in paira:
            print('  {} {}'.format(pair[0], pair[1]))
    else:
        for pair in range(5):
            print('  {} {}'.format(paira[pair][0], paira[pair][1]))
        print('  ...')
        for pair in range(-5, 0, 1):
            print('  {} {}'.format(paira[pair][0], paira[pair][1]))
            
    pairatioa=distinct_pair_ratio(paira, lstpaira)
    print('5. Ratio of distinct word pairs to total: {:.3f}'.format(pairatioa))
    
    #everything done above is done again to the file2
    
    print('\nEvaluating document {}'.format(file2))
    compb=compare_words(listb, liststop)
    avgb=avg_word_len(compb)
    print('1. Average word length: {:.2f}'.format(avgb))
    setb=set(compb)
    distb=dist_total(setb, compb)
    print('2. Ratio of distinct words to total words: {:.3f}'.format(distb))
    print('3. Word sets for document {}:'.format(file2))
    maxxb=longest_word(compb)
    wordsb=maxxb*['']
    wordsb=word_index(wordsb, compb)
    j=1
    for thing in wordsb:
        print('{}{}:{}{}:'.format(' '*(4-len(str(j))), j, ' '*(4-len(str(len(thing)))), len(thing)), end='')
        if thing!='':
            if len(thing)<=6:
                for stuff in thing:
                    print(' ', stuff, sep='', end='')
            else: 
                print('',thing[0], thing[1], thing[2], '...', thing[-3], thing[-2], thing[-1], end='')
        print('\n', end='')
        j+=1
    print('4. Word pairs for document {}'.format(file2))
    pairb=distinct_pair(compb, sepp)
    lstpairb=pairb
    pairb=list(sorted(set(pairb)))
    print('  {} distinct pairs'.format(len(pairb)))
    if len(pairb)<=10:
        for pairs in pairb:
            print('  {} {}'.format(pairs[0], pairs[1]))
    else:
        for pairs in range(5):
            print('  {} {}'.format(pairb[pairs][0], pairb[pairs][1]))
        print('  ...')
        for pairs in range(-5, 0, 1):
            print('  {} {}'.format(pairb[pairs][0], pairb[pairs][1]))
    pairatiob=distinct_pair_ratio(pairb, lstpairb)
    print('5. Ratio of distinct word pairs to total: {:.3f}'.format(pairatiob))
    print('\n', end='')
    
    #start of summary comparasion 
    
    print('Summary comparison')
    
    #compares the average length of list 1 to list 2 and outputs which one is 
    #bigger
    
    if avga>avgb:
        print('1. {} on average uses longer words than {}'.format(file1, file2))
    else:
        print('1. {} on average uses longer words than {}'.format(file2, file1))
    
    #prints the overall similarity using jaccard's equation 
    
    jac=jaccard(compa, compb)
    print('2. Overall word use similarity: {:.3f}'.format(jac))
    
    #goes through each word length and outputs jaccard's equation for each 
    #length
    
    print('3. Word use similarity by length:')
    if len(wordsa)>len(wordsb):
        smaller=len(wordsb)
        bigger=len(wordsa)
    else:
        smaller=len(wordsa)
        bigger=len(wordsb)
    for lines in range(smaller):
        if wordsa[lines]=='' or wordsb[lines]=='':
            print('{}{}: 0.0000'.format(' '*(4-len(str(lines+1))), lines+1))
        else:
            print('{}{}: {:.4f}'.format((' ')*(4-len(str(lines+1))), lines+1, jaccard(wordsa[lines], wordsb[lines])))
    for line in range(bigger-smaller):
        print('{}{}: 0.0000'.format(' '*(4-len(str(line+smaller+1))), line+smaller+1))
    
    #uses jaccards equation and compares the pairs of both sets.
    
    distinctcomp=jaccard(paira, pairb)
    print('4. Word pair similarity: {:.4f}'.format(distinctcomp))
    
            
            
