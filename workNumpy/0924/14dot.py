# 14dot.py
import numpy as np

# 새책 174~175페이지   dot=닷연산=행렬곱 
print()
kor = np.array( [[3,2], [5,4]])
ret = np.dot(kor,kor)
print(ret) # 19, 14, 35, 26
print('14dot.py dot행렬곱연산 2:21 졸려요')
'''
 [3,2], [3,2]   
 [5,4], [5,4]  맞는지 

3*3 + 2*5 = 19 
3*2 + 2*4 = 14
5*3 + 4*5 = 35
5*2 + 4*4 = 26
'''

print()
eng = np.array( [[5,4], [2,3]])
ret = np.dot(eng,eng)
print(ret)  # [33 32 16 17]
'''
 [5,4], [5,4]   
 [2,3], [2,3]  

 5*5 + 4*2 = 33

'''




print()
