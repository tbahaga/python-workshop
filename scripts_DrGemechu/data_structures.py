co2 = [325.68, 338.68, 354.35, 371.13, 387.37]
co2.append(400.0)
print(co2)
co2.insert(0, 316.91)
print(co2)
co2[6] = 401.0  # Remember, 7th item at index 6
print(co2)
location = (40.0, -105.3, 1655.1)
print(len(co2))
print(min(co2), max(co2))
co2_1960 = co2[0]  # index 0 at 1960
co2_2010 = co2[5]  # index 5 at 2010
print('Mauna Loa carbon dioxide concentration '
      'in 1960 was {0} ppm and '
      'in 2010 was {1} ppm.'.format(co2_1960, co2_2010))
lat, lon, elev = location  # unpacking the tuple
print('lat {0}, lon {1}, elevation {2}'.format(lat, lon, elev))
metars = {
    'KPRG': (48.96, 2.44, 66),
    'FAGM': (-26.24, 28.15, 1671),
    'KNYC': (40.71, -74.01, 10)}
print(metars['KNYC'])
metars['SBSP'] = (-23.63, -46.66, 801)
#If you have corrections,e.g.,
metars['SBSP'] = (-23.627, -46.655, 803.1)
print(metars['SBSP'])
temperature = 35
if temperature > 32:
    print('Temperature is above freezing.')
temperature = 30
if temperature > 32:
    print('Temperature is above freezing.')
else:
    print('Temperature is at or below freezing.')
wind_speed = 65
if wind_speed >= 64 and wind_speed <= 82:
    print('Category one hurricane')
elif wind_speed >= 83 and wind_speed <= 95:
    print('Category two hurricane')
elif wind_speed >= 96 and wind_speed <= 112:
    print('Category three hurricane')
elif wind_speed >= 113 and wind_speed <= 136:
    print('Category four hurricane')
elif wind_speed > 136:
    print('Category five hurricane')
else:
    print('Below hurricane level wind speed')
#EXample for loop
data = [('2016-12-27T19:02:00Z', 19.03), ('2016-12-27T19:22:00Z', -1),
   ('2016-12-27T19:42:00Z', -1), ('2016-12-27T20:02:00Z', -1),
   ('2016-12-27T20:22:00Z', -1), ('2016-12-27T21:02:00Z', 19.03),
   ('2016-12-27T21:22:00Z', -1), ('2016-12-27T22:02:00Z', 28.29),
   ('2016-12-27T22:22:00Z', -1), ('2016-12-27T23:02:00Z', 34.98),
   ('2016-12-27T23:22:00Z', 35.5), ('2016-12-28T00:01:00Z', -1),
   ('2016-12-28T00:21:00Z', 33.44), ('2016-12-28T01:02:00Z', -1),
   ('2016-12-28T01:22:00Z', 36.01), ('2016-12-28T02:01:00Z', 37.55),
   ('2016-12-28T02:22:00Z', 44.76), ('2016-12-28T03:02:00Z', 38.58),
   ('2016-12-28T03:22:00Z', 36.53), ('2016-12-28T04:02:00Z', 26.75),
   ('2016-12-28T04:22:00Z', 23.15), ('2016-12-28T05:02:00Z', 24.18),
   ('2016-12-28T05:22:00Z', 22.12), ('2016-12-28T06:02:00Z', 27.78),
   ('2016-12-28T06:22:00Z', 27.27), ('2016-12-28T07:02:00Z', 28.29)]
gusts = []
for time, obs in data:
    if obs > 35:
        gusts.append((time, obs))
gusts
#More precise for loop
[(time, obs) for time, obs in data if obs > 35]
#Write and read files
#Write to file data.txt
data=[1,2,3]
with open("data.txt", 'w') as f:
    f.write(str(data))
#Read from file data.txt
with open("data.txt", 'r') as f:
    data = f.read()
#Reading snow data
with open("snow.csv", 'r') as file:
    snowdata = [entries for line in file for entries in [line.split(",")]
                if (len(entries) > 0 and entries[0].isdigit())]
# Import matplotlib as use the inline magic so plots show up in the notebook
import matplotlib.pyplot as plt
#%matplotlib inline

# Make some "data"
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
# Make a simple line plot
plt.plot(x, y)

#Change the line style
plt.plot(x, y, color='tab:red', linestyle='--')
# Make a scatter plot
plt.plot(x, y, color='tab:orange', linestyle='None', marker='o')
# Make contour plots
x=np.linspace(-2*pi, 2*pi, 100)
y=np.sin(x)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2)
#Now make the contour line plot
plt.contour(X, Y, Z)
plt.show()
#Now make the shaded contour plot
plt.contourf(X, Y, Z)
#Or use imshow for the shaded plot
plt.imshow(Z)

