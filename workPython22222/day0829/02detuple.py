# deflist.py

def data_hap(x,y,z,a,b,c):
    #숫자합계구해서 리턴처리
    hap = x+y+z+a+b+c
    return hap

def my_hap(*args):
    print('*args타입', type(args))  #*args타입: tuple
    hap = 0
    for num in args:
        hap = hap+num
    return hap





mylist = [4,2,3,5]
mytuple = (4,2,3,5)

mylist[1]=54
print(mylist)

mytuple[1] = 94
print(mytuple)
# data=my_hap(6,11,24,7,5,21,39)
# print('데이터 결과 ', data)
# print('데이터 결과 ', my_hap(6,11,24,7,5,21,39))
# total = data_hap(6,9,21,7,3,21)
