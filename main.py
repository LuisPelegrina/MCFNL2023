import numpy as np 
import matplotlib.pyplot as plt

t=np.linspace(0,10,1001)

t0=3
s0=0.5
gauss = np.exp(-(t-t0)**2/(2*s0**2))

plt.plot(t, gauss)
plt.grid()
plt.show()