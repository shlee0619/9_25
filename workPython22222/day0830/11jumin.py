# 11jumin.py

import re

jumin = '981024-1278900'
my = jumin[7]
if my == 1 or my == 3:
    pass
elif my == 2 or my == 4:
    pass
else:
    pass


gender = re.search('(-)(\d{1})', jumin)
print(gender)
genderNum=int(gender.group(2))
if genderNum == 1 or genderNum == 3:
    print('남자')
elif genderNum == 2 or genderNum == 4:
    print('여자')
else:
    print('잘못된 접근')