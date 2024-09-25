import numpy as np

x = [2,4,6,8,10]       #시간 총합계 30 /5   평균 6시간
y = [81,93,91,97,98]   #점수 총합계 460 /5  평균 92점
A = np.vstack( [x,np.ones(len(x))] ).T
m,c = np.linalg.lstsq(A,y, rcond=None)[0]

print(m, c )  
#결과출력 1.8999999999999921 80.59999999999997

print()
print(round(m,2), round(c,2) )  
#결과출력 1.9  80.6