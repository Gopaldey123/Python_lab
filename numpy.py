import numpy as np

arr = np.array([20,25,35,30])
target = 36

closest = arr[np.abs(arr-target).argmin()]
print (closest)

