import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print('print(np.vstack((a,b)))')
print(np.vstack((a,b)))
# [1 2] [3 4] [5 6] [7 8]


print('-'*40)
print('print(np.hstack((a,b)))')
print(np.hstack((a,b)))
print('-'*40)
c = np.array(([1,2,3],[7,8,9])) #2행 * 3열 = 매트릭스 = metrix
print('c = np.array(([1,2,3],[7,8,9]))')
print(c)


print('변형 np.transpose(c)') #전치행렬 매트릭스
print(np.transpose(c))

print('\n\n')
print('변형2 c.T')
print(c.T)

