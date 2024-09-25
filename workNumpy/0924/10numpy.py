import numpy as np

x = np.zeros([3,5]) # 기본이 실수값
print(x)
print()

x = np.ones([3,5]) # 기본이 실수값
print(x)
print()


a = np.zeros([3,5], dtype=np.int64) # 실수
print(a)
print()

b = np.ones([3,5] , dtype=np.int64) # 실수
print(b)
print()
print('b.ndim =', b.ndim)
print('b.size =', b.size)
print('b.shape =', b.shape)
#에러 print('b.len =', b.len)
