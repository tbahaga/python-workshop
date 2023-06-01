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
# Open sample Sample RegCM data in netCDF format
file_loc  ="../../NMA_engagement/RegCM_Training/RegCM_codes/RegCM-master/REGCM_RUN/historical/output/"
ds = Dataset(file_loc +"test_003_ATM.1990010100.nc","r")
# Read data from this group
topo            = ds.variables['ta'][:] - 273.15
ptop            = ds.variables['ptop'][:]
ps              = ds.variables['ps'][:]
ts              = ds.variables['ts'][:]
kz              = ds.variables['kz'][:]
u               = ds.variables['ua'][:]
v               = ds.variables['va'][:]
rh              = ds.variables['rh'][:]
lat             = ds.variables['xlat'][:]
lon             = ds.variables['xlon'][:]
mask            = ds.variables['mask'][:]
# Adds standard background map
#ax.stock_img()
#Mask ocean
lsmaskrh= np.ones(rh.shape) * mask.squeeze()[np.newaxis,:, :]
rhmask=np.ma.masked_where(lsmaskrh==0, rh, copy=True)
#pressure
print('kz=',kz[0])
print('ps=',ps.shape)
print('ptop=',ptop)
press = []
for i in np.arange(0,18,1):
     press.append(i)
     press.append(ptop + kz[i]*(ps[i,:,:] - ptop))
print(press)
#print(press[11])
#exit()
#
## Set up Coordinate System for Plot and Transforms
# Set up a globe with a specific radius
globe = ccrs.Globe(semimajor_axis=6371000.)
data_projection = ccrs.PlateCarree()
fig = plt.figure(1,figsize=(10, 8))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 0.02], \
        bottom=.10, top=.90,hspace=0.20, wspace=0.01)
ax = plt.subplot(gs[0], projection=data_projection)

##Plot titles
#plt.title(f'',loc='center')
plt.title(r'RH (%) & temp. (deg C) ',loc='left')
plt.title(f'Jan 01, 1990 at 12:00 noon', loc='right')
#ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
## Plot Background
## Sets the extent using a lon/lat box
tick_points=np.arange(min(lon[0,:]),max(lon[0,:]),10)
ax.set_extent([min(lon[0,:]),max(lon[0,:]), min(lat[:,0]),\
        max(lat[:,0])-2])
ax.gridlines(draw_labels=True, xlocs=tick_points)

## Add variety of features
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)

## Can also supply matplotlib kwargs
ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle='-')
ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle='-')
ax.add_feature(cfeature.LAKES.with_scale('50m'), alpha=0.5)
ax.add_feature(cfeature.RIVERS.with_scale('50m'),linestyle=':', edgecolor='tab:green')
##Addis addis
addis_ababa     = [38.77000,8.99592]      #1.  Ethiopia
#ax.plot(addis_ababa[0],addis_ababa[1], marker='*', color='tab:green', transform=data_projection)
##Add text
#ax.text(addis_ababa[0]-2,addis_ababa[1]-1, "Finfine",transform=data_projection)
##plot colorful contours
cf=ax.contour(lon[0,:],lat[:,0], ts[1,:,:],transform=data_projection,cmap='nipy_spectral')
cff=ax.contourf(lon[0,:],lat[:,0], rhmask[1,12,:,:],transform=data_projection,cmap='gist_rainbow')
ccf=ax.quiver(lon[0,:],lat[:,0], u[1,12,:,:],v[1,12,:,:],transform=data_projection,regrid_shape=15,color='g')
#Label bar
length=np.linspace(1,21,2)
cax = plt.subplot(gs[1])
cb = plt.colorbar(cff, cax=cax, orientation='horizontal', extendrect='True')
ax.clabel(cf, inline=1, inline_spacing=1, fontsize=8, colors='black', fmt='%1.0f', manual=True)
cb.set_label(r'relative humidity', size='large')

ax.set_axis_on()
ax.get_axisbelow()
fig.savefig('Ethiopia_temperature.png')
plt.show()
