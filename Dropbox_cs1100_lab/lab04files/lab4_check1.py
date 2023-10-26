# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:14:08 2022

@author: ryani
"""
#import lab04files
from PIL import Image
import lab4_check2
im = Image.new('RGB', (512,512), 'white')

a=Image.open('ca.jpg')
a=lab4_check2.make_square(a)
a = a.resize((256, 256))

b=Image.open('im.jpg')
b=lab4_check2.make_square(b)
b = b.resize((256, 256))

c=Image.open('hk.jpg')
c=lab4_check2.make_square(c)
c = c.resize((256, 256))

d=Image.open('bw.jpg')
d=lab4_check2.make_square(d)
d = d.resize((256, 256))

im.paste(a, (0, 0))
im.paste(b, (256, 0))
im.paste(c, (0, 256))
im.paste(d, (256, 256))

im.show()
