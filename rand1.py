# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt

print(random.randint(0,100))
x=[random.randint(0,9) for p in range(0,9)]
y=[random.randint(0,9) for p in range(0,9)]
plt.plot(x,y)
plt.show()
