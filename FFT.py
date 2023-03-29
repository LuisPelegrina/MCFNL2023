import numpy as np 
import matplotlib.pyplot as plt

from numpy.fft import fft, fftfreq, fftshift 

t=np.linspace(0,1e-8,1001)

t0=4e-9
s0=1e-9
dt=t[1]-t[0]
gauss = np.exp(-(t-t0)**2/(2*s0**2))

plt.figure()
plt.plot(t, gauss)
plt.grid()

plt.figure()

freq = fftshift(fftfreq(len(gauss),dt))
gaussF = fftshift(fft(gauss))
plt.plot(freq,np.abs(gaussF))
plt.grid()
plt.show()