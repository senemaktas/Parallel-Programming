# -*- coding: utf-8 -*-
import numpy

#import sys
#n = int(sys.argv[1])

n=100
dot = numpy.array([0.])
x = numpy.linspace(0,100,n)
y = numpy.linspace(20,300,n)
dot = numpy.array([numpy.dot(x,y)])
print("skaler çarpım =", dot)
