import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(0,10,1001)

x0=3
s0=1
c=1

tRange=np.linspace(0,5,101)

for t in tRange:
    gauss = np.exp(-(x-x0-c*t)**2/(2*s0**2))
    plt.plot(x,gauss)
    plt.grid()
    plt.ylim(-0.1,1.1)
    plt.xlim(x[0],x[-1])
    plt.pause(0.1)
    plt.cla()
