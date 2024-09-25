# HWjumin.py.py

import datetime  #from  import 
import time

jumin = '971230-1835064' 

# 구현을 함수화 
# split()사용 [시:끝+1]
# 문제1 if제어 성별체크   1/3 남자  2/4여자 
# 문제2 생일 12월30일 생일 축하합니다
# 문제3 나이계산 2024-1997 = 27

def gendercheck(num):
    if num.split('-')[1][0] == '1' or num.split('-')[1][0] == '3':
        return '남성'
    elif num.split('-')[1][0] == '2' or num.split('-')[1][0] == '4':
        return '여성'
    else:
        return '잘못된 접근'

def birthday(num):
    print(f'생일 {num.split('-')[0][2:4]}월 {num.split('-')[0][4:]}일 축하합니다!')

def agecal(num):
    if int(num.split('-')[0][0:2])<24 and (num.split('-')[1][0] == 3 or num.split('-')[1][0] == 4):
        print(f'나이: {2024- (2000+int(num.split('-')[0][0:2]))}')
    else:
        print(f'나이: {2024- (1900+int(num.split('-')[0][0:2]))}')

print('성별: ', gendercheck(jumin))
birthday(jumin)
agecal(jumin)
