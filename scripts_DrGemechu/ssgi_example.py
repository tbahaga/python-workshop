import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt 
import xarray as xr
import numpy as np
loc='~/Greater_Horn_Africa_urban_climate/data/GPCP/'
data = xr.open_dataset(loc+'GPCP__V2_3__PRECIP__2.5x2.5.nc')
precip = data.precip
lat    = data.lat
lon    = data.lon
mask_lon=np.ones(precip.shape)* np.asarray(lon.squeeze())[np.newaxis,np.newaxis, :]
mask_lat=np.ones(precip.shape)* np.asarray(lat.squeeze())[np.newaxis,:, np.newaxis]
precip=np.ma.masked_where(mask_lon>42,precip)
precip=np.ma.masked_where(mask_lon<33,precip)
precip=np.ma.masked_where(mask_lon<33,precip)
precip=np.ma.masked_where(mask_lat<5,precip)
#precip=np.ma.masked_where(precip < 8, precip)
precip=np.ma.masked_outside(precip,2,12)
fig = plt.figure(figsize = (10,4))
ax = fig.add_subplot(1,1,1, projection = ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.RIVERS, color='blue')
ax.set_extent([30,52,0,18])
xtick_points=np.linspace(min(lon),max(lon), 10)
ytick_points=np.arange(min(lat), max(lat), 10)
ax.gridlines(draw_labels=True,  ylocs=ytick_points)

cv=ax.contourf(lon, lat, precip[5,:,:], cmap='Reds', transform=ccrs.PlateCarree())
plt.colorbar(cv)
#ax.set_global()
ax.stock_img()
plt.savefig('ema.png')
plt.show()
