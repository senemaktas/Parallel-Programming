# -*- coding: utf-8 -*-
"""
Pyton'da fonksiyonlar sonra kullanılmak üzere array'e konabililer.

@author: dell
"""

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

func=[add,mul]
print(func[0](2,3))
print(func[1](4,5))

a=func[0](3,4)
b=func[1](a,5)
print(b)