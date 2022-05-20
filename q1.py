import math as m
import mm1
import matplotlib.pyplot as plt

def rand_walk(length, step):
    x1 = 0
    y1 = 0
    xdata = [x1]  # x cordinate of the random walk
    ydata = [y1]  # y cordinate of the random walk
    for i in range(step - 1):
        theta = 2 * m.pi * mm1.mlcg_random_number(572,16381)#mlcg random number generator 
        x1 += length * m.cos(theta)
        y1 += length * m.sin(theta)
        xdata.append(x1)
        ydata.append(y1)
    return xdata, ydata  # returning the coordinte of each steps in a list


def creat_walk(length, step, walk):
    x = []  #
    y = []
    r_x = []
    r_y = []
    for i in range(walk):# for 500 walks
        x1, y1 = rand_walk(length, step)
        x.append(x1)
        y.append(y1)
        r_x.append(x1[-1])
        r_y.append(y1[-1])
    return x, y, r_x, r_y#

mm1.seed = 3
x,y,rx,ry=creat_walk(1,200, 500)#rx and ry are the final position of each walk step size 1 and number of steps 200

def distance(x,y):
	return (x**2+y**2)**0.5

ave_d=0
for i in range(500):
	ave_d+=distance(rx[i],ry[i])

print("The value of R_rms =",ave_d/500)
print("The value of sqrt(N) or sqrt(200) =",m.sqrt(200))

#plot for 1 random walk
plt.plot(x[0],y[0],"ro-",label="Random walk for 200 steps")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

#--------------output----------------
"""
The value of R_rms = 12.525064564833617
The value of sqrt(N) or sqrt(200) = 14.142135623730951
"""