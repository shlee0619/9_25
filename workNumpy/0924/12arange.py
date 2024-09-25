import numpy as np

'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]]
'''

kor = np.arange(1,16).reshape(3,5) #15개숫자발생
print(kor)
print()

eng = np.arange(1,16).reshape(3,5) #15숫자발생
print(eng)
print()

#에러 a = np.array(  [1,2], [3,4]  )
a = np.array( [ [1,2], [3,4] ] ) # [ ] 리스트
b = np.array( ( [5,6], [7,8] ) ) # ( ) 튜플 
print(np.vstack([a,b]))  # [ ] 리스트
print(np.vstack((a,b))) # ( ) 튜플
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

print()
print(np.hstack([a,b]))  # [ ] 리스트
print(np.hstack((a,b))) # ( ) 튜플

'''
[[1 2 5 6]
 [3 4 7 8]]
'''

'''
a = np.array( [ [1,2], [3,4] ] ) # [ ] 리스트
b = np.array( ( [5,6], [7,8] ) ) # ( ) 튜플 
'''





print()