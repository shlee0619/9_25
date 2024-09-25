# 12file.py

# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요


pathName = 'C:/Mtest/sample.txt'
wfile = open(pathName, 'a', encoding = 'UTF-8')
name = input('이름입력>>> ')
age = input('나이입력>>> ')
index = input('주소입력>>> ')




wfile.write(name + '\n')
wfile.write(age + '\n')
wfile.write(index + '\n')
wfile.close()



print('sample.txt파일저장성공했습니다.')
print()

pathName2 = 'C:/Mtest/sample2.txt'
# wfile2 = open(pathName2, 'a', encoding='UTF-8')
# wfile2.close() 권장
with open(pathName2, 'a', encoding='UTF-8') as myfile:
    pass
    name = input('이름입력>>> ')
    age = input('나이입력>>> ')
    index = input('주소입력>>> ')

    myfile.write(name + '\n')
    myfile.write(age + '\n')
    myfile.write(index + '\n')

print(pathName2, '파일저장성공했습니다. ')
print()

