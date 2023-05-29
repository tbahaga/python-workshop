from numpy import sin, cos, pi, linspace
f=lambda t: cos(pi*t) + 0.2*sin(5*pi*t+0.1) + 0.2*sin(30*pi*t) + 0.1*sin(32*pi*t+0.1) + 0.1*sin(47* pi*t+0.8)
t=linspace(0,4,400); signal=f(t)
from scipy.signal import wiener, medfilt
import matplotlib.pylab as plt
plt.plot(t,signal,'k', label='The signal')
plt.plot(t,wiener(signal,mysize=55),'r',linewidth=3, label='Wiener filtered')
plt.plot(t,medfilt(signal,kernel_size=55),'b',linewidth=3,
label='Medfilt filtered')
plt.legend()
plt.show()




