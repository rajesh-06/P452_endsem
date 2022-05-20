import math as m
import matplotlib.pyplot as plt
import mm1
import numpy as np
import copy


def potential(x):
	return 1/(1+x**2)**0.5#taken 1/(4*pi*epsilon_0) = 1
#wire is placed on x axis from -1 to 1 

res=[[],[],[]]

j=0
for i in range(4,7,1):#increasing the degree
	ans, res[j]=mm1.gaussian_quadrature(potential,i,-1,1)
	print("Potential at a unit distance from the centre for degree",i,"is",ans,"unit")
	j+=1
	print()

print("The analytical value of the potential is ",m.log(3+2*m.sqrt(2)))

#---------------output----------------------------------
# Potential at a unit distance from the centre for degree 4 is 1.5686274509803921 unit

# Potential at a unit distance from the centre for degree 5 is 1.5711711711711713 unit

# Potential at a unit distance from the centre for degree 6 is 1.5707317073170737 unit

# The analytical value of the potential is  1.5707963267948966