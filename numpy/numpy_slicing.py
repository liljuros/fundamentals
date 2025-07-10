import numpy as np

l = [1,2,3,4,5,6]

#print(l[::-1])
# arr = np.array(l)
# #print(arr[0:3])
# slice_ = arr[0:2]
# print(slice_, arr)
# slice_[0] = 100
# print(slice_, arr)
arr = np.arange(1,26).reshape(5,5)
#print(arr)
#print(arr[0:2, 0:2])
print(arr[::2, ::2])