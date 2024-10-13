

#변수 하나씩선언, 다중선언 가능

#a = 7
#b = 4
#ret=0

a,b,ret = 7,4,0

ret = a*b

#출력의 네 가지 방법

#print(변수, '문자', ~~) , 나열식
print(a,'*',b,'=',ret)

#print( '%d정수 %s문자열 %f실수 %c문자' %(데이터) )
print('%d * %d = %d' %(a,b,ret))

# print( '{} * {} = {}'.format(a,b,ret) )
print('{} * {} = {}'.format(a,b,ret))

#print( f'{변수 및 값}' )
print(f'{a} * {b} = {ret}')

print()
