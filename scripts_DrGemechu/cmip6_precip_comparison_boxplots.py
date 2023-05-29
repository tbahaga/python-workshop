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
mask_mpi = regionmask.mask_geopandas(shape_file, pr_mpi)
mask_ecearth = regionmask.mask_geopandas(shape_file, pr_ecearth)
mask_hadgem = regionmask.mask_geopandas(shape_file, pr_hadgem)
mask_cnrm = regionmask.mask_geopandas(shape_file, pr_cnrm)

pr_era5_m =pr_era5.where(mask==False)
pr_mpi_m =pr_mpi.where(mask==False)
pr_ecearth_m =pr_ecearth.where(mask==False)
pr_hadgem_m =pr_hadgem.where(mask==False)
pr_cnrm_m =pr_cnrm.where(mask==False)
#pr_era5_m[0,:,:].plot()
#plt.show()
#quit()


pr_era5_mean = np.mean(np.mean(pr_era5_m, axis=2), axis=1)
pr_mpi_mean = np.mean(np.mean(pr_mpi_m, axis=2), axis=1)
pr_ecearth_mean = np.mean(np.mean(pr_ecearth_m, axis=2), axis=1)
pr_hadgem_mean = np.mean(np.mean(pr_ecearth_m, axis=2), axis=1)
pr_cnrm_mean = np.mean(np.mean(pr_cnrm_m, axis=2), axis=1)

df=([pr_era5_mean*1000, pr_mpi_mean*86400,pr_ecearth_mean*86400,pr_hadgem_mean*86400,pr_cnrm_mean*86400])

fig, ax = plt.subplots()
boxplot = sns.boxplot(data=df, ax=ax).set(xlabel='', ylabel='precip  ($mm/day$)')
ax.xaxis.grid(True)
ax.yaxis.grid(True)
#boxplot = sns.stripplot(data=df, marker='o', alpha=1.0,color='black')
#plt.setp(boxplot.get_xticklabels(), rotation=15)
plt.xticks([0,1,2,3,4],["ERA5", "MPI","ECEARTH","HADGEM","CNRM"],rotation=25)
plt.text(1, 3.8, "2000-2014", horizontalalignment='left', size='medium', color='black', weight='semibold', fontsize=14, zorder=0)

plt.savefig('precip_cmip_boxplot.png')
plt.show()
