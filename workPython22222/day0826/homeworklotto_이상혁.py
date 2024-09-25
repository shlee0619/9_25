# 04lotto.py

import random

# 로또 1~45사이 숫자
# 로또 정수 
# 반복문 for,while
# 난수발생 6개 숫자 중복 체크 조별...
# 난수발생후 출력은 sort정렬 

list1 = []
while True:
    com = random.randint(1,45)
    if com in list1:
        continue
    list1.append(com)
    
    if len(list1) == 6:
        break
'''
while len(list1) != 6:
    list.append(random.randint(1,45))
    for k in range(len(list1)):
        if (list1.count(list1[k])>1):
            list1.pop()
            list1.append(random.randint(1,5))
'''
list1.sort()
for k in list1:
    print(k, end = ' ')


print()
print()


