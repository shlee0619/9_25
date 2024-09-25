import numpy as np
import random

for k in range(6):
    data = random.randint(1,45) #난수발생 리스트목록
    print(data, end =' ')

print()
for j in range(6):
    data = np.random.randint(1,45) #난수발생 리스트목록
    print(data, end =' ')

print()
print()

# x = np.random.randint(1,45).reshape(3,5)  에러
# x = np.random.randint(45).reshape(3,5) 에러
#x = np.random.rand(45).reshape(3,5)  # 0.000 ~ 0.9999
x = np.random.rand(45)  # 45갯수  0.000 ~ 0.9999
print(x)
print()

y = np.random.rand(15).reshape(3,5) # 3행*5열
print(y)
print()

z = np.random.rand(15).reshape(5,3) # 5행*3열
print(z)
print()
