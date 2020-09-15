'''Example of python code that finds numerically the zero pi / 2 range of x * sinx integral using
trapezoidal numerical integration method.'''

from math import sin,pi

f=lambda x: x*sin(x)

a=0
b=pi/2
n=5
h=(b-a)/n
s=0.5*(f(a)+f(b))
for i in range(1,n):
    s+=f(a+i*h)
integral=h*s
print("integral= %f" %integral)