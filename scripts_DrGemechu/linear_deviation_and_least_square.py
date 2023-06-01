
#The second NMA training
#prepared by Gemechu Fanta (PhD)

import numpy as np
import matplotlib.pyplot as plt

X = np.array([50, 54, 56, 59, 60, 61, 62, 65, 67, 71, 71, 74])
Y = np.array([22, 25, 34, 28, 26, 32, 30, 30, 28, 34, 36, 40])
x_centroid = np. mean(X)
y_centroid = np. mean(Y)
x = X - x_centroid
y = Y - y_centroid
yi_over_xi = y/x
table = np.column_stack((X,Y,x,y,yi_over_xi))
print('\nData transformation using Centroid and yi/xi calculation \n')
print('Xi\t\t\t\tYi\t\t\t xi\t\t\t\tyi\t\t\tyi/xi')
print('-------------------------------------------------------------------')
print(table)
ranked_table = table[table[:,-1].argsort()]
print('\nRanking the data by yi/xi\n')
print('Xi\t\t\t\tYi\t\t\t xi\t\t\t\tyi\t\t\tyi/xi')
print('-------------------------------------------------------------------')
print(ranked_table)
xi = ranked_table[:,2]
yi = ranked_table[:,3]
sum_abs_xi  = 0
for i in range(0, len(xi)):    
   sum_abs_xi = sum_abs_xi + abs(xi[i]);  
negative_sum_abs_xi = -sum_abs_xi
print('-------------------------------------------------------------------')
print('Searching for change in sign')
print('-------------------------------------------------------------------')
print('-?|xi| = '+str(negative_sum_abs_xi))
print('-------------------------------------------------------------------')
i = 0
while i < len(xi):
    negative_sum_abs_xi = negative_sum_abs_xi + 2*abs(xi[i])
    print('+'+str(2*abs(xi[i]))+' = '+str(negative_sum_abs_xi))
    if (negative_sum_abs_xi >= 0):
      break
    i += 1
print('-------------------------------------------------------------------')
print('Sign changes at index '+str(i+1))
print('The slope calculated as:')
print('b = y7/x7 = '+str(yi[i])+'/'+str(xi[i])+' = '+ str(yi[i]/xi[i]))
print('===============================================================')
print('Therefore, the eqn of best fit line using least deviations is given by:\n')
print("Y' - "+str(y_centroid)+' = '+ str(yi[i]/xi[i])+"(X - "+str(x_centroid)+")\n"   )
print("or\n")
print("Y' = "+ str(yi[i]/xi[i])+"(X)"+str(-x_centroid*yi[i]/xi[i]+y_centroid))
print('===============================================================')

#For the least square fit

m, b = np.polyfit(X, Y, 1)
print('m',m)
print('b',b)

max_x = np.max(X)
min_x = np.min(X)
xx = np.linspace(min_x, max_x, 1000)
yy = b + m * xx
# Plotting Values and Regression Line
plotsave = plt.figure(figsize=(4,3),dpi=200)
max_x = np.max(X)
min_x = np.min(X)
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = -x_centroid*yi[i]/xi[i]+y_centroid + yi[i]/xi[i] * x
# Ploting Line
plt.plot(x, y, color='r', label='least Deviation Fit',linewidth=2)
plt.plot(xx, yy, color='g', label='least square Fit')
# Ploting Scatter Points
plt.scatter(X, Y, c='b', label='Scatter Plot',linewidth=2)
#plt.text(14,12,"Best Fit Line equation: Y' = "+ str(format(yi[i]/xi[i],'.3f'))+"(X)"+str(format(-x_centroid*yi[i]/xi[i]+y_centroid,'.3f')))
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
