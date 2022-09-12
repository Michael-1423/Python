import numpy as np
import sklearn.preprocessing

a = np.ndarray(shape = (2,3) , dtype = int)
a[0][0] = 2
a[0][1] = 1
a[0][2] = 4
a[1][0] = 1
a[1][1] = 0
a[1][2] = 3
print(a)

data_binarized = sklearn.preprocessing.Binarizer(threshold = 2).transform(a)
print("\nBinarized data:\n", data_binarized)

print("Mean = ", a.mean(axis = 0))
print("Std deviation = ", a.std(axis = 0))

data_scaled = sklearn.preprocessing.scale(a)
print(data_scaled)
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis = 0))
