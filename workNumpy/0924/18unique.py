import numpy as np

a = np.array( [9,5,4,3,1,2,3,4,3,2,4,1,2,3,7,3,1,2,1,2,5,1,7,1,2,2,1,3] )
print(a)
ret = np.unique(a)
print(ret)
print()

print('trim적용')
b = np.array( [0,0,0,3,0,2,3,4,0,2,4,1,2,3,7,3,1,2,0,0,5,1,7,1,0,0,0,0] )
print('원본', b)
print(np.trim_zeros(b))
print(np.trim_zeros(b,trim='f'))
print(np.trim_zeros(b,trim='b'))
print()

kor = np.array( ([1,2], [3,4]) )
print(kor*kor)
'''
[1,2], [3,4]
[1,2], [3,4]

[ [ 1  4] [ 9 16] ]
'''

eng = [ 1,2,3,4 ]
#print(eng * eng) 
#에러이유 print(eng * eng) 
#

print()