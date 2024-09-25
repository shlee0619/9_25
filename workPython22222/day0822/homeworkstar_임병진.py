# homeworkstar.py
# 2024. 08. 22 (writer: B. Lim)

print('-'*10)
for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()
print('-'*10)

for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()
print('-'*10)

for i in range(4,-1,-1):
    print(' '*i,end='')
    print('*' * (9 - (2 * i)), end = '')
    print(' '*i)
print('-'*10)

for i in range(5):
    print(' '*i, end = '')
    print('*' * (9-(i*2)),end = '')
    print(' '*i)
print('-'*10)
