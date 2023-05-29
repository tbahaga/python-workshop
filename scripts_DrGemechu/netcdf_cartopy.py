#The second NMA training
#prepared by Gemechu Fanta (PhD)

#Convention for import to get shortened namespace
import numpy as np
# http://code.google.com/p/netcdf4-python/
from netCDF4 import Dataset  
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy.ma as ma
# Open sample Sample RegCM data in netCDF format
file_loc  ="../../NMA_engagement/RegCM_Training/RegCM_codes/RegCM-master/REGCM_RUN/historical/input/"
#file_loc  ="./"
ds = Dataset(file_loc +"test_003_DOMAIN000.nc","r")
# Read data from this group
topo            = ds.variables['topo'][:]
lat             = ds.variables['xlat'][:]
lon             = ds.variables['xlon'][:]
landuse         = ds.variables['landuse'][:]
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
ax.set_extent([min(lon[0,:]) ,max(lon[0,:]) , min(lat[:,0]) ,\
        max(lat[:,0])])
#ax.gridlines(draw_labels=True, xlocs=tick_points)

## Add variety of features
##Plot titles
plt.title(r'terrain height',loc='left')
plt.title(r'forecast time',loc='center')
plt.title(f'1990', loc='right')
#ax.add_feature(cfeature.LAND)
#ax.add_feature(cfeature.OCEAN)
#ax.add_feature(cfeature.COASTLINE)

## Can also supply matplotlib kwargs
ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':', alpha=0.9)
#ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle=':')
#ax.add_feature(cfeature.LAKES.with_scale('50m'), alpha=0.5)
ax.add_feature(cfeature.RIVERS.with_scale('50m'),linestyle=':', edgecolor='tab:green')
##Addis addis
addis_ababa     = [38.77000,8.99592]      #1.  Ethiopia
bahir_dar      = [37, 10]  
hawassa = [38, 7]
nairobi = [36.8, -1.3]
ax.plot(addis_ababa[0],addis_ababa[1], marker='o', color='tab:blue', transform=data_projection)
ax.plot(bahir_dar[0], bahir_dar[1], marker='*', color='green',transform=data_projection)
ax.plot(38.47, 7, marker='o', color='Red',transform=data_projection)
ax.plot(nairobi[0], nairobi[1], marker='*', color='Red',transform=data_projection)

##Add text
ax.text(addis_ababa[0]-2,addis_ababa[1]-1, "Finfine",transform=data_projection)
ax.text(bahir_dar[0], bahir_dar[1], "Bahir Dar",transform=data_projection)
ax.text(38.47, 7, "Hawassa",transform=data_projection)
ax.text(nairobi[0], nairobi[1],'Nairobi', transform=data_projection)
##plot colorful contours
#cf=ax.contour(lon[0,:],lat[:,0], topo,transform=data_projection,cmap='Paired')
landuse = ma.masked_greater(landuse, 12)
cf=ax.contour(lon[0,:],lat[:,0], topo,transform=data_projection,cmap='nipy_spectral')
#Label bar
length=np.arange(0,3000,500)
cax = plt.subplot(gs[1])
cb = plt.colorbar(cf, cax=cax, orientation='horizontal', extendrect='False')
cb.set_label(r'm', size='large')

ax.set_axis_on()
ax.get_axisbelow()
fig.savefig('Ethiopia.png')
plt.show()
