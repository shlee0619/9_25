# homeworkcoffee.py

money , sel = 0, 9 

money = int(input('금액입력 >>> ')) #600적절 
while True:
  print('\n================ 커피머신 ================')
  data = input('1.커피(250) 2.코코아(300) 3.반환 9:종료>>> ')
  sel = int(data)
  #if~elif~if제어문 커피값계산
  if sel == 9:
    break
  elif sel == 1:
    pass
    #커피주문
  elif sel == 2:
    pass
    #코코아주문
  elif sel == 3 :
    pass
  else:
    print('주문번호를 정확히 선택하세요')


print()
print('현재잔액은 ' , money , '입니다')
