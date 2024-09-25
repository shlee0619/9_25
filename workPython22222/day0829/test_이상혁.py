# test.py

# day0829폴더\test.py
# 문제1 name, age, gender 변수사용, 키보드입력, 나이는 숫자
# 문제2 나이입력 범위 20~70사이
        #조건 20미안 청소년 1~19    20~30청년   31~65중년   66이상노년
# 문제3 남자/남/man 입력 남자출력 여자/여/woman입력 여자출력
# 문제4 아래내용을 함수화
# 문제5 아래내용을 함수이름 임의의 명명 def 함수이름() :
def person():
    print('홍길동')
    print(34)
    print(True)

#고민 list관리/tuple관리/dict관리

name = input('이름:')

age = int(input('나이:'))

gender = input('성별:')

print("이름: ", name)

if age < 20:
    print(f'{age} 청소년입니다.')
elif age >= 20 and age <=30:
    print(f'{age} 청년입니다.')
elif age >= 31 and age <=65:
    print(f'{age} 중년입니다.')   
elif age >=66:
    print(f'{age} 노년입니다.')
else:
    print('잘못된 접근 발생')


if gender == '남자' or gender == '남' or gender == 'man':
    print('남성입니다.')
elif gender == '여자' or gender == '여' or gender == 'woman':
    print('여성입니다.')
else:
    print('잘못된 접근 발생')
    
# 함수로 접근하는 경우
def nameprint():
    name = input('이름:')
    print("이름: ", name)

def ageprint():
    age = int(input('나이:'))
    if age < 20:
        print(f'{age} 청소년입니다.')
    elif age >= 20 and age <=30:
        print(f'{age} 청년입니다.')
    elif age >= 31 and age <=65:
        print(f'{age} 중년입니다.')   
    elif age >=66:
        print(f'{age} 노년입니다.')
    else:
        print('잘못된 접근 발생')

def genderprint():
    gender = input('성별:')
    if gender == '남자' or gender == '남' or gender == 'man':
        print('남성입니다.')
    elif gender == '여자' or gender == '여' or gender == 'woman':
        print('여성입니다.')
    else:
        print('잘못된 접근 발생')

nameprint()
ageprint()
genderprint()