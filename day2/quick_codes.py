import xarray as xr

ds=xr.open_dataset(ncfiles_list[0])

ds


import glob


ncfiles_list=glob.glob('/srv/repo/IBF_workshop_data/kmj_daily_rainfall_chrips/*.nc')

ncfiles_list
