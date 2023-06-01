#The second NMA training
#prepared by Gemechu Fanta (PhD)

#Set things up
#matplotlib inline
#Importing CartoPy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
# Works with matplotlib's built-in transform support.
#fig = plt.figure(figsize=(10, 4))
#ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

# Sets the extent to cover the whole globe
#ax.set_global()

# Adds standard background map
#ax.stock_img()
# Set up a globe with a specific radius
globe = ccrs.Globe(semimajor_axis=6371000.)

# Set up a Lambert Conformal projection
#proj = ccrs.LambertConformal(standard_parallels=[25.0], globe=globe)

fig = plt.figure(figsize=(15, 8))
#ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal())
#ax.stock_img()


#ax.set_extent([-130, -60, 20, 55])
#ax = fig.add_subplot(1, 1, 1, projection=proj)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
#ax.stock_img()
# Add variety of features
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)

# Can also supply matplotlib kwargs
ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')
ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle=':')
ax.add_feature(cfeature.LAKES.with_scale('50m'), alpha=0.5)
ax.add_feature(cfeature.RIVERS.with_scale('50m'), edgecolor='tab:green')
data_projection = ccrs.PlateCarree()
#List lat and lon of respective cities in GHA
addis_ababa     = [38.77000,8.99592]      #1.  Ethiopia
asmara          = [38.91700,15.28300]     #2.  Eritrea
bujumbura       = [29.31700,-3.31700]     #3.  Burundi
djibouti        = [42.59000,11.50000]     #4.  Djibouti
dodoma          = [35.75875,-6.16833]     #5.  Tanzania
juba            = [31.60000,4.86700]      #6.  S. Sudan
kampala         = [32.61600,0.31700]      #7.  Uganda
khartoum        = [32.55250,15.61000]     #8.  Sudan
kigali          = [30.12292,-1.96667]     #9.  Rwanda
mogadishu       = [45.33787,2.02425]      #10. Somalia
nairobi         = [36.91250,-1.31583]     #11. Kenya


ax.plot(addis_ababa[0],addis_ababa[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(asmara[0],asmara[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(bujumbura[0],bujumbura[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(djibouti[0],djibouti[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(dodoma[0],dodoma[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(juba[0],juba[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(kampala[0],kampala[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(khartoum[0],khartoum[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(kigali[0],kigali[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(mogadishu[0],mogadishu[1], marker='o', color='tab:red', transform=data_projection)
ax.plot(nairobi[0],nairobi[1], marker='o', color='tab:red', transform=data_projection)
#Add text
ax.text(addis_ababa[0]-2,addis_ababa[1]-1.5, "Finfine",transform=data_projection)
ax.text(asmara[0]-2,asmara[1]+0.5, "Asmara", color='black', transform=data_projection)
ax.text(bujumbura[0]-2,bujumbura[1]-1.5, "Bujumbura", color='black', transform=data_projection)
ax.text(djibouti[0]-2,djibouti[1]-1.5, "Djibouti", color='black', transform=data_projection)
ax.text(dodoma[0]-2,dodoma[1]-1.5, "Dodoma", color='black', transform=data_projection)
ax.text(juba[0]-2,juba[1]-1, "Juba", color='black', transform=data_projection)
ax.text(kampala[0]-2,kampala[1]-1, "Kampala", color='black', transform=data_projection)
ax.text(khartoum[0]-2,khartoum[1]-1, "Khartoum", color='black', transform=data_projection)
ax.text(kigali[0]-3.5,kigali[1], "Kigali", color='black', transform=data_projection)
ax.text(mogadishu[0]-3,mogadishu[1]+0.5, "Mogadishu", color='black', transform=data_projection)
ax.text(nairobi[0]-1,nairobi[1]+0.5, "Nairobi", color='black', transform=data_projection)
#ax.axes.text("x-axis","y-axis")
# Sets the extent using a lon/lat box
ax.set_extent([22, 55, -12, 22])
xticks=[22,32,42,55]
ax.set_axis_on()
ax.get_axisbelow()
fig.savefig('Greater_horn.png')
plt.show()
