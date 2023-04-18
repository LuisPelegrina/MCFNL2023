import numpy as np 
import matplotlib.pyplot as plt

eps =1.0
mu = 1.0
c0=1/np.sqrt(eps*mu)

CFL=0.9
tFinal =20.0
L = 10.0

x = np.linspace(0,10,num=101)
xDual = (x[1:] + x[:-1])/2
dx = x[1]-x[0]

x0=2.5
s0=0.5

e= np.exp(-(x-x0)**2/(2*s0**2))
eNew = np.zeros(e.shape)

e[0]= 0.0
e[-1]= 0.0

eps = np.ones(x.shape)
eps[x>=L/2] =1.0

h= np.zeros(xDual.shape)
hNew=np.zeros(xDual.shape)
dt= CFL * dx / c0
tRange= np.arange(0,100,dt)

for t in tRange:
    eNew[1:-1] = (-dt / (dx * eps[1:-1]))*(h[1:] - h[:-1]) + e[1:-1]

    e[:] = eNew[:]

    eNew[0] = (-dt / (dx * eps[0]))*(h[0] - h[-1]) + e[0]
    eNew[-1] = e[0]

    e[:] = eNew[:]

    hNew[:] = (-dt / (dx*mu))*(eNew[1:] - eNew[:-1]) +h[:]
    
    h[:] = hNew[:]

    plt.vlines(L/2,-1,1)
    plt.plot(x,e,'.-')
    plt.plot(xDual,h,'.-')
    plt.grid()
    plt.ylim(-1.1,1.1)
    plt.xlim(x[0],x[-1])
    plt.pause(0.01)
    plt.cla()

print("END")