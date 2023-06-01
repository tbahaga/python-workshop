import numpy as np
import pandas as pd 
import matplotlib.pylab as plt
ds = pd.read_csv("130308_tec.dat", delim_whitespace=True)
#print(ds.columns[0])
#print(ds['%#YYMM'])
time_ym = ds['%#YYMM']
time_sec = ds['UTSEC']
time_day = ds['DD']
ds['time']=pd.to_datetime(time_sec, unit='s', origin=pd.Timestamp('2013-03-08'))
#print(ds['time'].dt.hour)

ds_diurnal = ds.groupby(ds['time'].dt.hour).mean()
#print(ds_diurnal)
VTEC = ds_diurnal['VTEC']
plt.plot(ds_diurnal.index[VTEC > 0], VTEC[VTEC>0] ,'r*-')
plt.show()
