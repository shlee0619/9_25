# testfor11.py

# 변수선언안하고 for 대표변수 처리

for k in range(1, 1001, 1) :
    print(k, end='\t') # print()함수 자동 라인개행포함 엔터기능<br>
    if k%5 == 0:
        print()

    if k==40:
        break 

    #문제1  한줄=한행=row 5개씩 출력
    #문제2  40숫자출력  if  조건  반복탈출 break 

print()
print()
'''
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
26  27  28  29  30
'''
