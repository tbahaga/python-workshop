# coding: utf-8
import pandas as pd 
import xarray as xr 
df = xr.read_dataset("latent_heat_flux_Ethiopia_yearmean.nc")
df = xr.load_dataset("latent_heat_flux_Ethiopia_yearmean.nc")
df = xr.load_dataset("latent_heat_flux_Ethiopia_yearmean.nc",decode_times=False)
df
time = df.time
time
lhf = df.lhtfl 
lhf 
import seaborn as sns
import matplotlib.pyplot as plt
nx = sns.boxplot(df) 
time.shape
data = [lhf]
nx = sns.boxplot(data=data)
plt.show() 
boxplot = sns.boxplot(data=data).set(xlabel='', ylabel='T($^{o}C$)')
boxplot = sns.stripplot(data=data, marker='o', alpha=0.5,color='red')
plt.show()
boxplot = sns.boxplot(data=data).set(xlabel='', ylabel='T($^{o}C$)')
boxplot = sns.stripplot(data=data, marker='o', alpha=0.5,color='red')
plt.xtick([0,1],[ERA5])
plt.xticks([0,1],[ERA5])
plt.xticks([0,1],['ERA5'])
plt.xticks([0],[ERA5])
plt.xticks([0],['ERA5'])
plt.show()
boxplot = sns.boxplot(data=data).set(xlabel='', ylabel='T($w/m^{2}$)')
boxplot = sns.stripplot(data=data, marker='o', alpha=0.5,color='red')
plt.xticks([0],['ERA5'])
plt.show()
