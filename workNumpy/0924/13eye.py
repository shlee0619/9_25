# 13eye.py
import numpy as np

x = np.zeros(9)  #실수
print(x)
print()

y = np.ones(9)   #실수
print(y)
print()

z = np.full( (4,6), 0) #정수 35숫자를 4행x6열
print(z)
print()

print('eye함수= zeros + 대각ones')
a = np.eye(4,6)
print(a)
print()
print('13eye.py문서입니다 ')