import numpy as np

a = np.array([9,5,4,3,1,2,3,4,3,2,1,2,4,4,2,1,4,5,1,2,3])
print(a)
ret = np.unique(a)
print(ret)
print()

print('trim적용')
b = np.array([0,0,3,1,2,4,5,2,4])
print('원본', b)
print(np.trim_zeros(b))
print(np.trim_zeros(b,trim='f'))
print(np.trim_zeros(b,trim='b'))

kor = np.array( ([1,2],[3,4]) )
print(kor*kor)


'''
[1,2],[3,4]
[1,2],[3,4]


[[1  4] [9  16]]

'''

eng = [1,2,3,4]
eng = np.array(eng)
print(eng * eng)
print()