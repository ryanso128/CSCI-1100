# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:17:37 2022

@author: ryani
"""
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

x=parse_line("Here is some random text, like 5/4=3./12/3/4")

print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
print(parse_line(" Again some spaces\n/12/12/12"))

