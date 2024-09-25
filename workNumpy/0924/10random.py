
import random
import numpy as np


x = np.zeros([3,5]) #zeros([하나]) 3행 4열

print(x)
print()
print()

x = np.ones([3,5]) #기본이 실수값
print(x)
print()

a = np.zeros([3,5], dtype = np.int64) #zeros([하나]) 3행 4열

print(a)
print()
print()

b = np.ones([3,5], dtype = np.int64) #기본이 실수값
print(b)
print()
print(b.ndim)
print(b.size)
print(b.shape)


