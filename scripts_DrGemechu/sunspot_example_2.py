import numpy as np 
import pandas as pd 
import xarray as xr
import matplotlib.pylab as plt
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline 

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

f=lagrange(np.asarray(monthlymean.month).astype("float64"), np.asarray(monthlymean.sunspot).astype("float64"))

plt.plot(monthlymean.month,monthlymean.sunspot, 'r*', label='data')
plt.plot(np.arange(0, len(f(np.asarray(monthlymean.month).astype("float64")))), f(np.asarray(monthlymean.month).astype("float64")), 'b-', label=f)
plt.legend()
plt.show() 
plt.close('all')


g=CubicSpline(time, data.sunspot, bc_type='natural')
print(g)
quit()
