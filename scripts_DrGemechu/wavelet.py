import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import pywt
data = pd.read_csv('03-01-2017.csv')
signal = data['Electrode'] 
samplingRate = len(signal) # 80608 
L = np.arange(1,np.floor(samplingRate/2),dtype='int') 
fhat = np.fft.fft(signal,samplingRate)
PSD = fhat*np.conj(fhat)/samplingRate

plt.plot(PSD[L],color='r',LineWidth=2,label="FFT of noisy signal") 
plt.legend()
plt.show()
plt.close('all')
# creating a morlet wavelet
steps = np.linspace(-1,1,samplingRate) 
f = 150 # frequency 
s = 7/(2*np.pi*f) # this is the standard deviation of the gaussain

c_signal = np.cos(2*np.pi*f*steps) *signal
plt.plot(c_signal,color='r',LineWidth=2,label="Sine wave ") 
plt.legend()
plt.show()
plt.close('all')

gausian_win = np.exp(-(pow(steps, 2))/(2*pow(s,2)))*signal

plt.plot(gausian_win,color='r',LineWidth=2,label="Gaussian window") 
plt.legend()
plt.show()
plt.close('all')
morlet = np.multiply(c_signal,gausian_win)*signal

plt.plot(morlet,color='r',LineWidth=2,label="Morlet Wavelet") 
plt.legend()
plt.show()
plt.close('all')
import pywt
# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt(signal, 'db2')
print(coeffs2)
LL, LH = coeffs2
freq=range(len(LL))
plt.plot( freq,LL,'r*', freq, LH, 'bo-')
plt.show()
