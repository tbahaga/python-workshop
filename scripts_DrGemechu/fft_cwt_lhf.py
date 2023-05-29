import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
data = xr.open_dataset("latent_heat_flux_Ethiopia.nc", decode_times=False)
units, reference_date = data.time.attrs['units'].split('since')
data['time'] = pd.date_range(start=reference_date, periods=data.sizes['time'], freq='MS')
time = data['time']
yearlymean = data.groupby(time.dt.year).mean()
monthlymean = data.groupby(time.dt.month).mean()
#FFT
from scipy.fftpack import fft
#Sampling rate
datalh=data.lhtfl[~np.isnan(data.lhtfl)]
timelh=data.time[~np.isnan(data.lhtfl)]
datafft = np.fft.fft(datalh)
datafreq = np.fft.fftfreq(timelh.shape[-1])
#plt.hist(np.abs(datafft))
#plt.plot(np.abs(datafreq), np.abs(datafft))
period = 1/np.abs(datafreq)
plt.stem(np.abs(datafreq), np.abs(datafft), 'b', markerfmt=" ", basefmt = "-b")
plt.show()
plt.close('all')

plt.plot(period, np.abs(datafft))
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
plt.plot(timelh, datalh, 'b*',label='original')
plt.plot(timelh, monthlymeanifft, 'r-',label='ifft')
plt.legend()
plt.show()
#CFT
widths = np.arange(1, 100)

cwtlh=signal.cwt(datalh, signal.ricker, widths)

plt.contourf(timelh, widths, cwtlh, cmap='rainbow')
plt.show()
plt.close('all')

widths = np.arange(1, 12)
cwtlh=signal.cwt(monthlymean.lhtfl, signal.ricker, widths)
plt.contourf(monthlymean.month, widths, cwtlh, cmap='rainbow')
plt.show()
plt.close('all')

plt.plot(monthlymean.month, monthlymean.lhtfl)

plt.show()

