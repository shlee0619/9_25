import numpy as np

x = [2,4,6,8,10]      #시건합계 30/5   평균 6시간
y = [81,93,91,97,98]  #점수합계 460/5  평균 92점

su = np.polyfit(x, y, 1)
print(su)  #결과출력 [ 1.9 80.6]

