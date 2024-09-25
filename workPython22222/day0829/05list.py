# 05list.py

import time

lotto = [12,13,2,4,45,23]

for k in range(1,11,1):
    su = k**2
    print(su, end = '\n')


print()
for k in range(1,11,1):
    su =k**2
    print(su, end = '\n')


print()
mylist = [a**2 for a in range(1,11,1)]
mytuple = (pow(b,2) for b in range(1,11,1))
mylist = {c**2 for c in range(1,11,1)}

