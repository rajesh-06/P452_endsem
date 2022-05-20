import math as m
import matplotlib.pyplot as plt
import mm1
import numpy as np
import copy

def explicitPDE(u, L, delx, delt, time):

    n = int(L/delx)+1
    k=0.1
    alpha = k*delt/(delx**2)
    
    A = mm1.zeromatrix(n,n)
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == j:
                A[i][i] = 1 - (2*alpha)
            elif i == (j-1) or j == (i-1):
                A[i][j] = alpha
    #print(A)
    i = 1
    while i*delt < time:
        temp = mm1.mat_vec_mult(A,u)
        u = copy.deepcopy(temp)
        i = i+1
        u[0]=0
        u[-1]=0
    return u

def func(x):
    return 20*abs(m.sin(m.pi*x))

del_t = 0.008
del_x = 0.1
L = 2
n = n = int(L/del_x)+1
steps = [0,10,20,50,100,200,500]
time = [del_t*steps[i] for i in range(len(steps))]


#x-axis
x=[del_x*i for i in range(n)]

#define u matrix(initial conditions)
u = [0 for i in range(n)]
for i in range(len(u)):
    u[i]=func(x[i])

for i in range(len(time)):
    u1 = explicitPDE(u, L, del_x, del_t, time[i])
    plt.plot(x,u1,label='Time ='+str(steps[i]))

plt.xlabel("X-axis (unit length)")
plt.ylabel("Temperature($^o$C)")
plt.grid()
plt.legend()
plt.show()

"""
At time = 0, the temperature is plot has 2 peaks equally spaced in the plot which means that temperature is high at 2 points in the rod and gradually as time goes places where maxima was there it begins to cool down by transferring heat to the neighbour position where temperature is less, i.e., at the center. That's why we are getting an increasing temperature at the centre as time goes.
"""