# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:19:42 2022

@author: ryani
"""

def get_line(fname, parno, lineno):
    file=open('{}.txt'.format(fname).rstrip())
    para=file.read().split('\n\n')
    line=para[parno-1].lstrip('\n')
    line=line.split('\n')
    return line[lineno-1]

def is_digit(x):
    y=x.isdigit()
    return y

def parse_line(text):
    split=text.split('/')
    if len(split)<4:
        return 'None'
    else:
        a=split.pop(-3)
        b=split.pop(-2)
        c=split.pop(-1)
        joinstr='/'.join(split)
        if is_digit(a)==False or is_digit(b)==False or is_digit(c)==False:
            return 'None'
        else:
            return int(a), int(b), int(c), joinstr    


fn=int(input('Please enter the file number ==> ').strip())
pn=int(input('Please enter the paragraph number ==> ').strip())
ln=int(input('Please enter the line number ==> ').strip())

x=get_line(fn, pn, ln)
y=parse_line(x)
prgm=open('program.py', 'w')
while y[0]!=0 and y[1]!=0 and y[2]!=0:    
    prgm.write(y[3])
    prgm.write('\n')
    x=get_line(y[0], y[1], y[2])
    x=get_line(y[0], y[1], y[2])
    y=parse_line(x)
prgm.close()







