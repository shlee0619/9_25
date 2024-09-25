# 11reemailcheck.py

import re

def email_check(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{email}은(는) 올바른 이메일입니다.")
    else:
        print(f"{email}은(는) 올바르지 않은 이메일입니다.")
    #re.findall( '^시작 .[a-z]{2,}$끝', )
    #re.findall( ' .[^부정a-z]{2,}', )
email_check("kim@gmail") # .org .kr .com .net
email_check("kim_gmail.net") # @포함여부
email_check("$^kim") #첫글자특수문자포함
email_check("kim@gmail.net") #올바른 이메일입니다.