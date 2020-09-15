# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:31:47 2018

@author: dell
"""

import random
import matplotlib.pyplot as plt
print(random.randint(0,100))
x=[random.randint(0,9) for p in range(0,9)]
y=[random.randint(0,9) for p in range(0,9)]
plt.plot(x,y)
plt.show()