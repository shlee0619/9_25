
import numpy as np


x = [2, 4, 6, 8, 10]      #시간합계 30/5   평균 6시간
y = [81, 93, 91, 97, 98]  #점수합계 460/5  평균 92점


mean_x = np.mean(x) 
mean_y = np.mean(y)

print('시간 x 평균: ', mean_x) #시간 x 평균:  6.0
print('점수 y 평균: ', mean_y) #점수 y 평균:  92.0
print()

# parent=40  children= 76
parent = sum([(i - mean_x)**2 for i in x])
children = sum([(x[idx]-mean_x) * (y[idx] - mean_y) for idx, value in enumerate(x)])
a = children / parent
b = mean_y - ( mean_x * a)

print('분자 children: ', children) 
print('분모 parent: ', parent)
print('기울기(a): ', a)
print('y 절편(b): ', b)
print()
'''
분자 children:  76.0
분모 parent:  40.0
기울기(a):  1.9
y 절편(b):  80.6
'''

z = []
for i in range(5):
    cal= int((a*x[i]+b))
    z.append(cal)

print('예측점수 =' , z )#예측값출력
#예측점수 = [84, 88, 92, 95, 99]

#원본 x = [2, 4, 6, 8, 10]      #시간합계 30/5   평균 6시간
#원본 y = [81, 93, 91, 97, 98]  #점수합계 460/5  평균 92점
