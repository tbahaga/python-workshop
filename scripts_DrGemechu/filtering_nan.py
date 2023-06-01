import math
import numpy as np
a=[1,2,3,4,float('NAN'), 6,7,8]
print(np.mean(a))
b=[]
for i in a:
     if not math.isnan(i):
         b.append(i)
print(b)
print(np.mean(b))
