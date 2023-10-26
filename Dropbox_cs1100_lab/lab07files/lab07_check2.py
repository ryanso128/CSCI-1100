# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:08:26 2022

@author: ryani
"""

def get_line(fname, parno, lineno):
    file=open('{}.txt'.format(fname).rstrip())
    para=file.read().split('\n\n')
    line=para[parno-1].lstrip('\n')
    line=line.split('\n')
    print(line[lineno-1])
    


fn=int(input('Please enter the file number ==> ').strip())
pn=int(input('Please enter the paragraph number ==> ').strip())
ln=int(input('Please enter the line number ==> ').strip())

get_line(fn, pn, ln)

