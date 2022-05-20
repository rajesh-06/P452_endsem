import math as m
import matplotlib.pyplot as plt
import mm1
import numpy as np
import copy

def pde_explicit(L, delx, delt,funx, time):
    # u matrix
    n = int(L/delx)+1
    u0 = [0 for i in range(n)]
    #print(u0)
    u0[-1]= funx(L)
    u0[0] = funx(0)
    for i in range(len(u0)):
        u0[i]=funx(i*delx)
    #A matrix
    print(u0)
    A = mm1.zeromatrix(n,n)
    alpha = delt/(delx**2)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == j:
                A[i][i] = 1 - (2*alpha)
            elif i == (j-1) or j == (i-1):
                A[i][j] = alpha
    #print(A)
    i = 1
    while i*delt < time:
        unew = mm1.mat_vec_mult(A,u0)
        u0 = copy.deepcopy(unew)
        i = i+1
        #print(i)
    return u0

def func(x):
    return 20*abs(m.sin(m.pi*x))
x=[0.1*i for i in range(21)]
data=pde_explicit(2,0.1,0.0008,func,20)
print(data)
# u0=[]
# for i in range(len(x)):
#     u0.append(func(x[i]))
# time=[0,10,20,50,100,200,500]
# for i in range(len(time)):
#     data=pde_explicit(2,0.1,0.0008,func,time[i])
#     data=mm1.transpose(data)
#     plt.plot(x,data[0],label=str(time[i]))
# plt.plot(x,data[0])
# plt.plot(x,u0)
#plt.show()