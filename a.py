import numpy as np
import matplotlib.pyplot as pl

l = [1,2,3,4]
a = np.ndarray(shape = (2,3) , dtype = int)
a[0][0] = 2
a[0][1] = 1
a[0][2] = 4
a[1][0] = 2
a[1][1] = 1
a[1][2] = 4
print(a)
print(a.shape)

b = np.log(l)

print(pl.plot(l,b))
pl.show()
