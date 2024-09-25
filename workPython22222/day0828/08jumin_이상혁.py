# 08jumin.py

import datetime #from import
import time

jumin = '930124-1234444'
jum1  = '930124' #len() 6자릿수 체크
jum2  = '1234444' #len() 7자릿수 체크

# 문제 1 성별체크 1/3 남자 2/4여자
if int(jumin[7])==1 or int(jumin[7])==3:
    print("남자")
elif int(jumin[7])==2 or int(jumin[7])==4:
    print("여자")
else:
    print("잘못된 접근이 발생했습니다.")
print()



# 문제 2 생일 12월 30일

print(f"생일: {jumin[2:4]}월 {jumin[4:6]}일")
print()
# 문제3 나이계산 2024-1997
mytime = time.localtime()
if int(jumin[0]) == 9:
    nai = mytime.tm_year - (1900+int(jumin[0:2]))
elif int(jumin[0]) >= 0:
    nai = mytime.tm_year - (2000+int(jumin[0:2]))
else:
    print("잘못된 접근이 발생했습니다.")
print(f'현재 {nai} 살입니다.')
print()
print()

len1 = len(jum1)
len2 = len(jum2)

