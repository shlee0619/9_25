# 09resub.py

import re

phone = '010-7800-1234 박이썬'
# 힌트 re.sub( '1패턴', '2변경적용', phone)
model = re.sub( '-[0-9]{4}-' , '-****-' , phone)

print(phone)
print(model) # 010-****-1234