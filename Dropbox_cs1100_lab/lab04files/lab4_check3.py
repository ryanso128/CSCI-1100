# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:19:52 2022

@author: ryani
"""
def resize(x):
    a=x.size
    c=256/a[1]
    b=x.resize((int(a[0]*c),256))
    return b
from PIL import Image
back=Image.new('RGB', (1000, 360), 'Black')
i=0
d=[]
while i<6:
    e=Image.open('{}.jpg'.format(i+1))
    e=resize(e)
    d.append(e)
    i+=1



back.paste(d[0], (31, 20))
back.paste(d[1], (31+10+148, 20+40))
back.paste(d[2], (31+20+148*2, 20))
back.paste(d[3], (31+30+148*3, 20+40))
back.paste(d[4], (31+40+148*4, 20))
back.paste(d[5], (31+50+148*5, 20+40))
back.show()
