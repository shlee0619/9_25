# 01test.py
# 람다식은 import 기술안함, 키워드 lambda기술

def mycal(su):
    return 3*su+8
    
print('일반식', mycal(5))
my1 = lambda su: 3*su+8
print()
print('람다식', (lambda su : 3*su+8)(5))
print('람다식', (lambda su : 3*su+8)(5))
print()



def myAdd(x,y):
    return x+y

print('일반식', myAdd(11,4))
my2 = lambda x,y : x+y
print('람다식', my2(11,4))
print('람다식', (lambda x,y: x+y)(11,4))


def myCheck(su):
    msg = '안내문'
    if (su % 2 == 0):
        msg = '짝'
    else:
        msg = '홀'
    return msg

    
print(myCheck(12))
check = lambda su : '짝' if su%2 == 0 else '홀'
print(check(2))