# coding: utf-8
import numpy as np 
import pandas as pd 
import xarray as xr
import matplotlib.pylab as plt
data = xr.open_dataset("isunspots.nc", decode_times=False)
units, reference_date = data.time.attrs['units'].split('since')
data['time'] = pd.date_range(start=reference_date, periods=data.sizes['time'], freq='MS')
time = data['time']
yearlymean = data.groupby(time.dt.year).mean()
monthlymean = data.groupby(time.dt.month).mean()
plt.plot(yearlymean.year, yearlymean.sunspot) 
plt.xlabel('Years')
plt.ylabel('Sunspots')
plt.show() 
plt.close('all')
plt.plot(monthlymean.month, monthlymean.sunspot)
plt.xticks(monthlymean.month,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.xlabel('Months')
plt.ylabel('Sunspota')
plt.show() 
mu = np.mean(data.sunspot, axis=0)
sigma = np.std(data.sunspot, axis=0)
z= (data.sunspot - mu)/sigma
y=(1/(np.sqrt(2*np.pi)))*np.exp((-z**2)/2)
plt.scatter(z, y)
plt.show()
plt.close('all')

from scipy.interpolate import lagrange
import warnings
warnings.filterwarnings("ignore",category =RuntimeWarning)
data2=data.dropna('time', how='all')
#f=lagrange(np.asarray(data2['time']).astype('int64'), np.asarray(data2['sunspot']).astype('int64'))
f=lagrange(np.asarray(data2['time']).astype('int64'), np.asarray(data2['sunspot']).astype('int64'))
plt.plot(time, data2['sunspot'], 'b*', label='Monthly sunspot')
plt.plot(time.astype('int64'), f(time.astype('int64')), 'r-', label='lagrange interpolation')
plt.savefig("lagrange_sunspot.png")
plt.legend()
plt.show()
