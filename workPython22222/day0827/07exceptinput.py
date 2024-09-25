# 07exceptinput.py
# 문제1 dan입력 키보드 input(), 형변환
# 문제2 예외처리 try: ~ except: ~ 먼저 작성 권장 
# 문제3 dan입력범위 정수1이상  2~9사이 숫자만 입력 
# 1건이상처리는 무조건 반복문
import time

dan = 0 #초기값

try:
    dan = int(input('원하는 단 입력>>> '))
    if dan < 2 or dan > 9 :
        print('숫자범위는 2~9사이 숫자입니다\n다시 입력하세요')
        
    for k in range(1,10,1) :
        print(f'{dan}*{k}={dan*k}' )
        time.sleep(0.3)
except:
    pass


print()
time.sleep(0.5)
print('포인트 7점획득')
print('포인트 5점이상이면 vip자격만족대상입니다')

print()
print('- ' * 50)