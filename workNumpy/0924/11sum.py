import numpy as np
import statistics 

data = [1,2,3,4,6,5,7,9,1,3,7] #합계48
#총점,평균
print('총점', sum(data)) 
print('평균', round(sum(data)/len(data),2)) 
print()

print('넘피총점평균')
print('총점', np.sum(data)) 
print('평균', round(np.sum(data)/np.size(data),2)) 
print()

print('통계총점평균 숫자변경해서 확인')
data = [ 1, 2, 2, 3, 4, 5, 6, 6, 6, 8 ]
# print('총점', statistics.sum(data)) 에러
print('총점', sum(data)) 
print('평균', round(statistics.mean(data),2)) 
print('평균', round(sum(data)/len(data),2)) 
print('중앙', statistics.median(data))  #4.5숫자없지만 중앙값은 
print()
print(data)
np.random.shuffle(data)
print(data)
print()



#양수
a = np.random.rand(15).reshape(3,5) # 3행*5열
print(a)
print('- ' * 50)

#음수
b = np.random.randn(15).reshape(3,5) # 3행*5열
print(b)
print()


print('🎄 ' * 40)
kor = np.arange(16) #0부터 16개숫자발생
print(kor)
eng = np.arange(1,16) #1부터 15숫자발생
print(eng)

data = np.random.randint(1,45)
print(data)

