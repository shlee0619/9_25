# 01testlambda.py
# 람다식은 import 기술안함,  키워드 lambda기술

def mycal(su):
    return 3*su+8


print('일반식', mycal(2))
my1 = lambda su : 3*su+8
print('람다식', my1(2)) 
print('람다식', (lambda su : 3*su+8)(2)) 
print()



def myAdd(x,y):
    return x+y

print('일반식', myAdd(11,9)) 
my2 = lambda x,y : x+y
print('람다식', my2(11,9)) 
print('람다식', (lambda x,y : x+y)(11,9)) 


print('- ' * 50)
print()
# 함수에서  계산처리후 if~else제어문  리턴값
def myCheck(su): 
    msg = '안내문'
    if su%2 == 0:
        msg = '짝수'
    else:
        msg = '홀수'
    return msg 


print(myCheck(17))
print((lambda su: '짝수' if su%2==0 else '홀수')(17))









print()