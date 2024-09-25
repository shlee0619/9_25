# 14def.py

# 파이썬함수 
# def 함수이름(매개): ~~~ return 값

# 함수의 매개인자X, 리턴값 
# 함수는 호출하자 
def book():
    title='몽블랑'  #지역변수=local variable = 북씨 소유
    return title 

def price():
    pay=7800
    return pay

def main():
    print('시작함수 4:32')
    print('main함수 4:33')

    #리턴값이 있다 의미 함수가 값을 가지고 있음
    value1 = book()
    value2 = price()
    print('book함수 title' , book())
    print('price함수 pay ' , price())

    print('book함수 title' , value1)
    print('price함수 pay ' , value2)


#함수없이 그냥 처리  신규등록, 삭제, 출력
#메뉴만들어서 필요한기능을 함수로 구현해서 호출 

main()





print()





