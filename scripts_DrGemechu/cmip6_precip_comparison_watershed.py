import os
from datetime import datetime
import regionmask
import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#import tensorflow as tf
import xarray as xr
import geopandas as gp
import gc
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
#Load the data
datapath  = '../data/cmip6/'
#Use xarray to open the dataset
dataset1 = xr.open_dataset(datapath+"ERA5_2000-2014.nc")
pr_era5 = dataset1.tp
lon       = dataset1.longitude
lat       = dataset1.latitude
time = pd.to_datetime(dataset1.time, format='%d.%m.%Y %H:%M:%S')
pr_era5.reindex(time=time)

del(dataset1)
gc.collect()

dataset2 = xr.open_dataset(datapath+"pr_Amon_MPI-ESM1-2-HR_2000-2014.nc")

pr_mpi    = dataset2.pr
lon      = dataset2.longitude
lat      = dataset2.latitude
del(dataset2)
gc.collect()

dataset3 = xr.open_dataset(datapath+"pr_Amon_EC-Earth3-AerChem_2000-2014.nc")

pr_ecearth = dataset3.pr
lon    = dataset3.longitude
lat    = dataset3.latitude



del(dataset3)
gc.collect()

dataset4 = xr.open_dataset(datapath+"pr_Amon_HadGEM3-GC31-LL_2000-2014.nc")

pr_hadgem = dataset4.pr
lon    = dataset4.longitude
lat    = dataset4.latitude



del(dataset4)
gc.collect()

dataset5 = xr.open_dataset(datapath+"pr_Amon_CNRM-CM6-1-HR_2000-2014.nc")

pr_cnrm = dataset5.pr
lon    = dataset5.longitude
lat    = dataset5.latitude



del(dataset5)
gc.collect()

####################################################
#Mask by shapefile (Blue Nile)
####################################################
shape_file=gp.read_file(datapath+"bn_basin.shp", rows=1)
#Rename the longitudes and latitudes as lon and lat (to confirm to the shapefile names
pr_era5=pr_era5.rename({'longitude': 'lon', 'latitude':'lat'})
pr_mpi=pr_mpi.rename({'longitude': 'lon', 'latitude':'lat'})
pr_ecearth=pr_ecearth.rename({'longitude': 'lon', 'latitude':'lat'})
pr_hadgem=pr_hadgem.rename({'longitude': 'lon', 'latitude':'lat'})
pr_cnrm=pr_cnrm.rename({'longitude': 'lon', 'latitude':'lat'})

mask = regionmask.mask_geopandas(shape_file, pr_era5)

del(shape_file)
gc.collect()

pr_era5_m =pr_era5.where(mask==False)
pr_mpi_m =pr_mpi.where(mask==False)
pr_ecearth_m =pr_ecearth.where(mask==False)
pr_hadgem_m =pr_hadgem.where(mask==False)
pr_cnrm_m =pr_cnrm.where(mask==False)

del(pr_era5)
del(pr_mpi)
del(pr_ecearth)
del(pr_cnrm)
del(mask)
gc.collect()
#make time mean
pr_era5_mean=np.mean(pr_era5_m, axis=0)
pr_mpi_mean=np.mean(pr_mpi_m, axis=0)
pr_ecearth_mean=np.mean(pr_ecearth_m, axis=0)
pr_hadgem_mean=np.mean(pr_hadgem_m, axis=0)

del(pr_era5_m)
del(pr_mpi_m)
del(pr_ecearth_m)
del(pr_hadgem_m)

gc.collect()

#pr_era5_m[0,:,:].plot()
#plt.show()
#quit()

xtick_points=np.linspace(25,50, 10)
ytick_points=np.arange(0, 21, 10)

fig, axes = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection':ccrs.Mercator()}, figsize=(10, 14))
ax=axes.flatten()
#Graph 1
ax[0].add_feature(cfeature.COASTLINE)
ax[0].add_feature(cfeature.BORDERS)
ax[0].add_feature(cfeature.RIVERS, color='blue')
ax[0].set_extent([25,50,0,21])
ax[0].gridlines(draw_labels=True,  ylocs=ytick_points)
ax[0].set_title('(a) ERA5', fontsize=14)
ax[0].spines[['right', 'top']].set_visible(False)

mesh=ax[0].contourf(lon, lat, pr_era5_mean*1000, cmap='rainbow', transform=ccrs.PlateCarree())

#Graph 2
ax[1].contourf(lon, lat, pr_era5_mean*1000, cmap='rainbow', transform=ccrs.PlateCarree())
ax[1].set_title('(b) MPI', fontsize=14)
ax[1].add_feature(cfeature.COASTLINE)
ax[1].add_feature(cfeature.BORDERS)
ax[1].add_feature(cfeature.RIVERS, color='blue')
ax[1].set_extent([25,50,0,21])
ax[1].gridlines(draw_labels=True,  ylocs=ytick_points)
ax[1].spines[['right', 'top']].set_visible(False)


#Graph 3
ax[2].contourf(lon, lat, pr_ecearth_mean*8640, cmap='rainbow', transform=ccrs.PlateCarree())
ax[2].set_title('(c) ECEARTH', fontsize=14)
ax[2].add_feature(cfeature.COASTLINE)
ax[2].add_feature(cfeature.BORDERS)
ax[2].add_feature(cfeature.RIVERS, color='blue')
ax[2].set_extent([25,50,0,21])
ax[2].gridlines(draw_labels=True,  ylocs=ytick_points)
ax[2].spines[['right', 'top']].set_visible(False)

#Graph 4
ax[3].contourf(lon, lat, pr_hadgem_mean*8640, cmap='rainbow', transform=ccrs.PlateCarree())
ax[3].set_title('(d) HADGEM', fontsize=14)
ax[3].add_feature(cfeature.COASTLINE)
ax[3].add_feature(cfeature.BORDERS)
ax[3].add_feature(cfeature.RIVERS, color='blue')
ax[3].set_extent([25,50,0,21])
ax[3].gridlines(draw_labels=True,  ylocs=ytick_points)
ax[3].spines[['right', 'top']].set_visible(False)

fig.subplots_adjust(bottom=0.12, top=0.92, left=0.1, right=0.99, wspace=0.20, hspace=0.25)
cbar_ax = fig.add_axes([0.2, 0.10, 0.6, 0.02])
cax = fig.colorbar(mesh, cax=cbar_ax, orientation='horizontal')
#ccax = fig.colorbar(contour)
cax.set_label('precipitation (mm/day)', fontsize=18)

plt.savefig('precip_cmip_spatial.png')
plt.show()
