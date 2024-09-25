# mymenu.py

import time
import sys  #프로그램종료 sys.exit()
from datetime import datetime #datetime.now()
#import datetime #datetime.datetime.now()

menu = dict()
flag = True
num,su,sel = 0,0,0
msg,info,message = '안내메', '안내메', '안내메'

dt = datetime.now()
print('처리날짜 ', datetime.now())
print('처리날짜 ', dt)
print()

def menuInsertNew(a,b):
    name = input('이름입력key>>>')
    price = input('가격입력value >>>')
    menu[name] = price
    print(name, '등록 성공했습니다')

def menuAllprint():
    for k,v in menu.items():
        print( k ,' ', v)
    print()

def menuEditupdate(a):
    if menu.get(a) == None:
            print('편집대상 딕트가 key 없습니다')
    else:
        price = input('변경가격 재입력value >>>')
        menu[a] = price #mysite[200키] = '새로운값'
        print(a, '가격수정편집 성공했습니다')


def menuDelete(a):
    if menu.get(a) == None:
        print('삭제대상 딕트가 key 없습니다')
    else:
        menu.pop(a)
        print(a, '데이터삭제 성공했습니다')
        time.sleep(0.3)
        for k,v in menu.items():
            print( k ,' ', v)

def menuFindsearch(a):
    if menu.get(a) == None:
        print(a, '데이터가 없습니다')
    else:
        print(a, menu[a],'데이터 조회성공했습니다')

def menuExit():
    print('딕트처리를 종료합니다\n')
    sys.exit()


while flag:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료>>'))
    if num == 9: menuExit()
    elif num == 1: 
        name = input('이름입력key>>>')
        price = input('가격입력value >>>')
        menuInsertNew(name,price)

    elif num == 2: 
        menuAllprint()

    elif num == 3:  
        name = input('편집대상 키값 입력>>> ')
        menuEditupdate(name)

    elif num == 4: #삭제
        name = input('삭제대상 키값 입력>>> ')
        menuDelete(name)

    elif num == 5: #한건만=본인꺼
        key = input('조회검색 key 입력>>> ')
        menuFindsearch(key)
    else:
        pass
        print('처리번호를 잘못 입력하셨네요\n')










