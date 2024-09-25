# HWsetlotto_이상혁.py

#추천 lotto = set()   #셋항목함수  lotto.add()
#금지 lotto = list()  리스트추가   append()
#난수 로또숫자발생, 중복체크 , set추가
#set데이터타입을 list변환
#출력은 오름차순적용 sort()
import random



def mysetlotto(l):
    print()
    while len(l) != 6:
        l.add(random.randint(1,45))
        
    l = list(l)
    l.sort()
    return l
lotto = set()
print(mysetlotto(lotto))


    
    # while~while~if~else
    # while~for~if~else
    # while~if~else
    


