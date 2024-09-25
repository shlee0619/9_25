import numpy as np

a = np.array( [ [1,2], [3,4] ] )
b = np.array( [ [5,6], [7,8] ] )

print(np.vstack((a,b)))
# [1 2] [3 4]  [5 6] [7 8]

print()
print(np.hstack((a,b)))
# [1 2 5 6] [3 4 7 8] 



print()
print('- ' * 50)
c = np.array( ([1,2,3], [7,8,9])  )  #2행*3열=매트릭스=metrix
print('원본',c)
print()
print('변형', np.transpose(c)) #전치행렬 매트릭트
print()
print('변형', c.T)

'''
원본 [[1 2 3]
 [7 8 9]]

변형 [[1 7]
 [2 8]
 [3 9]]

변형 [[1 7]
 [2 8]
 [3 9]]

'''










print()
print()
print()