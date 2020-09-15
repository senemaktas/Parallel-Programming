# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:21:20 2017

@author: dell
"""

n=0
toplam=0
son=1000
while n < son:
    toplam=toplam+((-1)**n)/(2*n+1)
    n=n+1
print("pi sayısı = ",4*toplam)    