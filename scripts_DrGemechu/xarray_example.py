# Convention for import to get shortened namespace
import numpy as np
import xarray as xr
# Create some sample "temperature" data
data = 283 + 5 * np.random.randn(5, 3, 4)
data
temp = xr.DataArray(data)
temp
temp = xr.DataArray(data, dims=['time', 'lat', 'lon'])
temp
# Use pandas to create an array of datetimes
import pandas as pd
times = pd.date_range('2018-01-01', periods=5)
times


# Sample lon/lats
lons = np.linspace(-120, -60, 4)
lats = np.linspace(25, 55, 3)

temp = xr.DataArray(data, coords=[times, lats, lons],
        dims=['time', 'lat', 'lon'])
temp

temp.attrs['units'] = 'kelvin'
temp.attrs['standard_name'] = 'air_temperature'

temp
# For example, convert Kelvin to Celsius
temp - 273.15
temp.sel(time='2018-01-02')
from datetime import timedelta
temp.sel(time='2018-01-07', method='nearest', tolerance=timedelta(days=2))

# Cell content replaced by load magic replacement.
temp.interp(lon=-105, lat=40)

temp.sel(time=slice('2018-01-01', '2018-01-03'), lon=slice(-110, -70), lat=slice(25, 45))temp.sel(time=slice('2018-01-01', '2018-01-03'), lon=slice(-110, -70), lat=slice(25, 45))

# As done above
temp.loc['2018-01-02']

temp.loc['2018-01-01':'2018-01-03', 25:45, -110:-70]


