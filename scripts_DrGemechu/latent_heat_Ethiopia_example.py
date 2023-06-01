# coding: utf-8
import numpy as np 
import pandas as pd 
import xarray as xr
import matplotlib.pylab as plt
data = xr.open_dataset("latent_heat_flux_Ethiopia.nc", decode_times=False)
units, reference_date = data.time.attrs['units'].split('since')
data['time'] = pd.date_range(start=reference_date, periods=data.sizes['time'], freq='MS')
time = data['time']
yearlymean = data.groupby(time.dt.year).mean()
monthlymean = data.groupby(time.dt.month).mean()
plt.plot(yearlymean.year, yearlymean.lhtfl) 
plt.xlabel('Years')
plt.ylabel('Latent heat flux (W/m$^{2}$)')
plt.show() 
plt.close('all')
plt.plot(monthlymean.month, monthlymean.lhtfl)
plt.xticks(monthlymean.month,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.xlabel('Months')
plt.ylabel('Latent heat flux (W/m$^{2}$)')
plt.show() 
mu = np.mean(data.lhtfl, axis=0)
sigma = np.std(data.lhtfl, axis=0)
z= (data.lhtfl - mu)/sigma
y=(1/(np.sqrt(2*np.pi)))*np.exp((-z**2)/2)
plt.scatter(z, y)
plt.show()
