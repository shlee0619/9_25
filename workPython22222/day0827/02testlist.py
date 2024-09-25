# 02test.py

mylist = [ ] #리스트선언
mydict = {} #dict선언


mylist.append('lee')
mylist.append(90)
mylist.append(85)
mylist.append(True)
mylist.append(90)
mylist.insert(1, '빅데이터')

# 문제 85데이터삭제  remove(), pop(), del []
mylist.remove(85)
for k in mylist:
    print(k, end='\t')

print()
# 리스트데이터갯수 count(데이터), len()
cnt = mylist.count(90)
print('리스트갯수 ', mylist.count(90))









print()
