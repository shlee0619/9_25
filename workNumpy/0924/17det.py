import numpy as np

# 접근 np.random.rand()
# 접근 np.linalg.det()

a = np.array( [ [1,2], [3,4] ] )
print(a)

# 문제  np.dot(a,a) 예상 
# 값 = 1*4 - 2*3 
ret  = np.linalg.det(a) #175page
print('np.linalg.det ', ret) # -2.0000000000000004





print()