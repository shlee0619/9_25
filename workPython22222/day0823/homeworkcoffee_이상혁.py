# homeworkcoffee.py

money, sel= 0, 9

money = int(input('금액입력 >>> ')) #600적절
while True:
    print('\n================= 커피머신 =================')

    data = input('1.커피(250) 2.코코아(300) 3.반환 9:종료>>> ')
    sel = int(data)
    #if~elif~if제어문 커피값계산

    if sel == 9:
        break
    elif sel == 1:
        if ( money<250 ):
            print("잔액이 부족합니다.")
            continue
        money -= 250
        #커피주문
    elif sel == 2:
        if ( money<300 ):
            print("잔액이 부족합니다.")
            continue
        money -=300
        #코코아주문
    elif sel == 3:
        print('반환되셨습니다.', money, '원')
        
    else:
        print('주문번호를 정확히 선택하세요')

    

    print()


print()
print('현재잔액은 ', money)