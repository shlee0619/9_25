# 10recompile.py

import re

data = '''
kim 840916-1094852
lee 921207-2059326
goo 981024-1674938
'''

# p = re.compile('(\d{6})-\d{7}')
# result = p.sub('\1-*******', data)
# print(result)


pattern = re.compile('(\d{6})[-](\d{7})')
first = pattern.sub('\g<1>-*******', data)
print(first)
print(data)

two = re.sub('[0-9]{7}', '*******', data) #권장 sub()
print(two)

com = re.compile('-\d+')
first = com.sub('-*******',data)
print(first)

two = re.sub('[0-9]{7}', '*******', data)
print(two)
    


# compile('\d{6}-\d{7}')적용후 sub()확인
# 문자열함수 for~~if~ data[시작위치:]
# 정규식 re.sub( '-[0-9]{4}-' , '-****-', phone)

#정규식 compile(), sub(1,2,3), 다른방법
#kim 840916-*******
#lee 921207-*******
#goo 981024-*******