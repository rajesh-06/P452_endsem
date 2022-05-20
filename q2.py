import math as m
import matplotlib.pyplot as plt
import mm1
import numpy as np
import copy

A=mm1.readfile('esem4fit.txt',0)
A=mm1.transpose(A)
X,Y=A
def p0(x):
	return 1
def p1(x):
	return x
def p2(x):
	return 0.5*(3*x**2-1)
def p3(x):
	return 0.5*(5*x**3-3*x)
def p4(x):
	return 0.125*(35*x**4-30*x**2+3)
def p5(x):
	return 0.125*(63*x**5-70*x**3+15*x)
def p6(x):
	return (231*x**6-315*x**4+105*x**2-5)/16
p=[p0,p1,p2,p3,p4,p5,p6]

sig = [1 for i in range(len(X))]
b,chi2=mm1.poly_fit_special(X,Y,sig, p)


print("Fitting coefficients in orthonormal legendre basis are:")
print(b)


#plotting
plt.plot(X,Y, 'ro',label="data")
plt.plot(X,mm1.special_func_value(X,p,b), '-',label="fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.legend()
plt.show()

#------------output--------------
"""

Fitting coefficients in orthonormal legendre basis are:
[0.07003196671971398, 0.00430168583786432, -0.010166710608800474, 0.013083743602879214, 0.11411855049286529, -0.006726972223322476, -0.012384559712646202]

"""