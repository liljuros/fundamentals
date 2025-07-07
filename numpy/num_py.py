import numpy as np

# a1 = np.array([1,2,3,4])
# a2 = np.array((0.1, 0.2, 0.3, 0.4))
#
# print(a2.dtype)
# m1 = np.array([1,2,3,4])
# m2 = np.array([
#     [1,2,3,10],
#     [4,5,6,10],
#     [7,8,9,10]
# ])
#
# print(m1.shape, m2.shape)

# a = np.zeros(5, dtype=np.int32)
# print(a)

arr = np.arange(12)
#print(arr.shape)
# m1 = arr.reshape(4, 3)
# print(m1)
m2 = arr.reshape(2,6)
# print(m2)
m3 = m2.reshape(6,2)
print(m3)
m3[0][0] = 5
print(arr)