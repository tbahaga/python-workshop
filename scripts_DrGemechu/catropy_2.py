import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
temp_data = 25 + 5*np.random.rand(1,24,46)
time =['2022-08-03']
lat = np.linspace(0,15,24)
lon = np.linspace(33,48,46)
temp_data = xr.DataArray(temp_data, coords=[time, lat, lon], dims=['time','lat','lon'])
fig = plt.figure(figsize = (10,4))
ax = fig.add_subplot(1,1,1, projection = ccrs.PlateCarree())
ax.set_extent([33,48,0,15])
#ax.set_global()
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.RIVERS, linestyle=':', color='tab:blue')
cont=ax.contourf(lon,lat, temp_data[0,:,:], cmap='rainbow')
plt.colorbar(cont, orientation='vertical')

ax.gridlines(draw_labels=True)
ax.stock_img()
plt.title("Hypothetical data example")
plt.savefig("hypothetical.png")
plt.show()
