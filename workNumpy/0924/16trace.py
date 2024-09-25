# 16trace.py

import numpy as np

# 헷갈려요 array([]), arange(최종) 
# 문제1] 0~15까지 16개 정수 발생 arange(16) 4행*4열
x = np.arange(16).reshape(4,4)
print(x)
print()
print('trace결과', np.trace(x)) #30=0+5+1+15
print()

# 새책 175페이지 trace 행렬의 대각선 합 
y = np.arange(27).reshape(3,3,3)
print(y)
print()
print('trace결과', np.trace(y)) #
print()
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]

trace결과 [36=0+12+24 39=1+13+25 42=2+14+26]
'''


z = np.arange(27).reshape(3,9)
print(z)
print()
print('trace결과', np.trace(z)) # 30
'''
[[ 0  1  2  3  4  5  6  7  8]
 [ 9 10 11 12 13 14 15 16 17]
 [18 19 20 21 22 23 24 25 26]]

trace결과 30
'''