# 06random.py
# 파이썬 일반수학함수 접근

import math  
# math대표함수 pow,sqrt  9의제곱 81,  81제곱근
# random함수 randint  1~45숫자 6개 발생 

a = int(math.pow(9,2))
b = math.sqrt(81)
print(a)
print(int(math.pow(9,2)))
print(9*9)
print()

print(b)
print(math.sqrt(81))
print(81/9)
print('- '  * 50)


import random
# math대표함수 pow,sqrt  9의제곱 81,  81제곱근
# random함수 randint  1~45숫자 6개 발생 
for k in range(6):
    data = random.randint(1,45)
    print(data, end =' ')