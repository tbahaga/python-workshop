#Convention for import to get shortened namespace
import numpy as np
# http://code.google.com/p/netcdf4-python/
from netCDF4 import Dataset  
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# Open sample Sample RegCM data in netCDF format
file_loc  ="../../NMA_engagement/RegCM_Training/RegCM_codes/RegCM-master/REGCM_RUN/historical/input/"
ds = Dataset(file_loc +"test_003_DOMAIN000.nc","r")
# Read data from this group
topo            = ds.variables['topo'][:]
lat             = ds.variables['xlat'][:]
lon             = ds.variables['xlon'][:]
mask            = ds.variables['mask'][:]

#topo after mask 
topo = np.ma.masked_where(mask <0.5, topo)
# Adds standard background map
#ax.stock_img()

## Set up Coordinate System for Plot and Transforms
# Set up a globe with a specific radius
globe = ccrs.Globe(semimajor_axis=6371000.)
data_projection = ccrs.PlateCarree()
fig = plt.figure(1,figsize=(10, 8))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 0.02], \
        bottom=.07, top=.90,hspace=0.09, wspace=0.01)
ax = plt.subplot(gs[0], projection=data_projection)

##Plot titles
plt.title(r'terrain height',loc='left')
plt.title(f'1990', loc='right')
#ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
## Plot Background
## Sets the extent using a lon/lat box
tick_points=np.arange(min(lon[0,:]),max(lon[0,:]),10)
ax.set_extent([min(lon[0,:]),max(lon[0,:]), min(lat[:,0]),\
        max(lat[:,0])])
ax.gridlines(draw_labels=True, xlocs=tick_points)

## Add variety of features
#ax.add_feature(cfeature.LAND)
#ax.add_feature(cfeature.OCEAN, color='blue')
ax.add_feature(cfeature.COASTLINE, linewidth=4)

## Can also supply matplotlib kwargs
ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle='-', linewidth=2)
ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle=':')
ax.add_feature(cfeature.LAKES.with_scale('50m'), alpha=0.5, color='blue')
ax.add_feature(cfeature.RIVERS.with_scale('50m'),linestyle=':',color='blue')
##Addis addis
addis_ababa     = [38.77000,8.99592]      #1.  Ethiopia
ax.plot(addis_ababa[0],addis_ababa[1], marker='o', color='tab:blue', transform=data_projection)

##Add text
ax.text(addis_ababa[0]-2,addis_ababa[1]-0.5, "Addis Ababa",transform=data_projection)
##plot colorful contours
cf=ax.contourf(lon[0,:],lat[:,0], topo,transform=data_projection,cmap='rainbow')
#Label bar
length=np.arange(0,3000,500)
cax = plt.subplot(gs[1])
cb = plt.colorbar(cf, cax=cax, orientation='horizontal', extendrect='False', ticks=length)
cb.set_label(r'm', size='large')

ax.set_axis_on()
ax.get_axisbelow()
fig.savefig('Ethiopia.png')
plt.show()
