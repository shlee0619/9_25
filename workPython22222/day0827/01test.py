#01test.py

mylist = [ ] #리스트선언



mylist.append('lee')
mylist.append(90)
mylist.append(85)
mylist.append(90)
mylist.append(True)
mylist.insert(1, '빅데이터')
# 문제 85데이터삭제 remove, pop, del[]
mylist.remove(85)
print('- '*50)
for k in mylist:
    print(k, end= '\t')
print()

# 리스트개수 count(데이터), len()
cnt = mylist.count(90)
print('리스트개수', cnt)


