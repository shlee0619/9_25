# 04delpop.py 
import time

data = [ 7,8,9,10,3,5,2,4,1 ]
data.remove(9) #9삭제
data.pop()     #1삭제
print(data)    #[7, 8, 10, 3, 5, 2, 4]

del data[2]
print(data) #[7, 8, 3, 5, 2, 4]
time.sleep(1)

# 문제 8, 3, 5, 2
del data[1:5]  # [ 시작: 끝+1 ]
print(data)

time.sleep(0.5)
data = [ 7,8,9,10,3,5,2,4,1 ] #문제 모든데이터전부삭제
# data.clear #에러대신 삭제가 안됨
# data.clear() 정답빙고
del data[:]  #전체삭제 비권장 
print(data)
print('삭제연습끝 드뎌 dict실습 k:v')

# count(90) , len(리스트/딕트/문자열),  






# remove, del, pop, clear 제거삭제기능
# remove(데이터값)
# pop(위치)  pop()맨끝
# del 대상[위치]
# clear 전부삭제 


# 추가 append(), insert(위치,값) , add ()
# 추가 딕트이름[k300] = dataValue  
# 덮어씌어짐 딕트이름[k300] = dataValue  
print()