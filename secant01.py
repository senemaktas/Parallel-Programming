# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:31:55 2017

@author: dell
"""

f= lambda x:x*x-50
a=50
b=3
tol=1
while tol>=10**(-4):
#for i in range(10):
    bn=(b-((f(b)*(b-a))/(f(b)-f(a))))
    a=b
    b=bn
    print(b)
    tol=(abs(f(bn)))