import numpy as np

x = np.random.rand(45)  # 45갯수  0.000 ~ 0.9999
print(x)
print()

y = np.random.rand(15).reshape(3,5) # 3행*5열
print(y)
print()

z = np.random.rand(15) #1행*15열
print(z)
print()


# 0.000 ~ 0.9999 범위를 벗어남 
a = np.random.randn(15) #1행*15열
print(a)
print('0.000 ~ 0.9999 범위를 벗어남 ')
