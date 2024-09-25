#15list.py
import time

#리스트목록 list() 반복O,순서O
mylist= ['kim',78,3.1415,True,'F','kim',78]  
print(mylist)
print()
time.sleep(1)

#set set() 반복x,순서x
myset = {23, 'red', 78, 23,'red', 78, 'red' }    
print(myset)
print()
time.sleep(1)

#tuple튜플, tuple(), 수정불가
mytuple = ('blue', 21, 'A' )  
print(mytuple)
print()
time.sleep(1)

#dict딕트 dict() key,value  700:'구글' 
mydict  = { 100:'naver', 200:'kakao' } 
print(mydict)
print()