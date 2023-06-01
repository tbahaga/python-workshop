import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
data = xr.open_dataset("isunspots.nc", decode_times=False)
units, reference_date = data.time.attrs['units'].split('since')
data['time'] = pd.date_range(start=reference_date, periods=data.sizes['time'], freq='MS')
time = data['time']
yearlymean = data.groupby(time.dt.year).mean()
monthlymean = data.groupby(time.dt.month).mean()
#FFT
from scipy.fftpack import fft
#Sampling rate
datasp=data.sunspot[~np.isnan(data.sunspot)]
timesp=data.time[~np.isnan(data.sunspot)]
datafft = np.fft.fft(datasp)
datafreq = np.fft.fftfreq(timesp.shape[-1])
#plt.hist(np.abs(datafft))
#plt.plot(np.abs(datafreq), np.abs(datafft))
period = 1/np.abs(datafreq)
plt.stem(np.abs(datafreq), np.abs(datafft), 'b', markerfmt=" ", basefmt = "-b")
plt.show()
plt.close('all')

plt.plot(period, np.abs(datafft), 'o-')

#monthlymeanfft=np.fft.fft(monthlymean.sunspot)
#monthlymeanfreq=np.fft.fftfreq(monthlymean.month.shape[-1])

#sr=200
#N = len(monthlymeanfft)
#n = np.arange(N)
#T = N/sr
#freq = n/T
#period=(1/freq)
#plt.stem(freq, np.abs(monthlymeanfft), 'b', markerfmt=" ", basefmt = "-b")
#plt.hist(np.abs(monthlymeanfft))
#plt.plot(period, np.abs(monthlymeanfft))
plt.show()
plt.close('all')
monthlymeanifft = np.fft.ifft(datafft)
plt.plot(timesp, datasp, 'b*',label='original')
plt.plot(timesp, monthlymeanifft, 'r-',label='ifft')
plt.legend()
plt.show()
#CFT
widths = np.arange(1, 1000)

cwtsunspot=signal.cwt(datasp, signal.ricker, widths)

plt.contourf(timesp, widths, cwtsunspot, cmap='rainbow')
plt.show()
plt.close('all')

widths = np.arange(1, 12)
cwtsunspot=signal.cwt(monthlymean.sunspot, signal.ricker, widths)
plt.contourf(monthlymean.month, widths, cwtsunspot, cmap='rainbow')
plt.show()
plt.close('all')

plt.plot(monthlymean.month, monthlymean.sunspot)
plt.show()
plt.close('all')
plt.plot(yearlymean.year, yearlymean.sunspot)
plt.show()

