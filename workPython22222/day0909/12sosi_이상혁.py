# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  
import sys

# pip install oracledb 
import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}


# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
conn = cx_Oracle.connect(**config) 
print('config매개인자 ', type(config))
cursor = conn.cursor()

print("database version: ", conn.version)
print("oracle connect ok success")
print()


def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    message = "select"

    #코드데이터 입력 후 code필드값 중복체크/함수탈출/재입력

    #1신규등록 2전체출력 3수정 4삭제 5제목조회 9종료
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))

    
    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'B')"    
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)



def sosiSelectAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)
    rows = cursor.fetchall()
    print('rows타입 ', type(rows))
    print()

    print('%4s\t %10s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        #print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4s\t %12s\t %12s\t  %5s\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    print()
    time.sleep(1)

   


def sosiSelectTitle():
    print('제목 데이터 like 조회하세요')
    title = input('조회할 제목 입력>> ')
    msg = f"select * from sosi where title LIKE '%{title}%'"
    cursor.execute(msg)
    rows = cursor.fetchall()

    if rows:
        print('%4s\t %10s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급'))
        for r in rows:
            print('%4s\t %10s\t %10s\t  %4s\t %6s\t %s' %r)
        print('조회된 데이터 갯수:', len(rows))
    else:
        print('해당 제목을 포함하는 데이터가 없습니다.')
    print('- ' * 50)
    time.sleep(1)

def sosiUpdate():
    print('코드로 조회 후 수정')
    dcode = int(input('수정할 코드 입력>> '))
    msg = f"SELECT * FROM sosi WHERE code = {dcode}"    
    cursor.execute(msg)
    row = cursor.fetchone()
    if row:
        a = input('어떤 항목을 수정하시겠습니까? >> ')
        if a == '코드':
            code = int(input('어떻게 수정하시겠습니까? >> '))
            msg = f"UPDATE sosi SET code = {code} where code = {dcode}"
            cursor.execute(msg)
            conn.commit()
        elif a == '이름':
            name = input('어떻게 수정하시겠습니까? >> ')
            msg = f"UPDATE sosi SET name = '{name}' where code = {dcode}"
            cursor.execute(msg)
            conn.commit()
        elif a == '제목':
            title = input('어떻게 수정하시겠습니까? >> ')
            msg = f"UPDATE sosi SET title = '{title}' where code = {dcode}"
            cursor.execute(msg)
            conn.commit()
        elif a == '급여':
            sal = int(input('어떻게 수정하시겠습니까? >> '))
            msg = f"UPDATE sosi SET sal = {sal} where code = {dcode}"
            cursor.execute(msg)
            conn.commit()
        elif a == '등급':
            grade = input('어떻게 수정하시겠습니까? >> ').upper()
            msg = f"UPDATE sosi SET grade = '{grade}' where code = {dcode}"
            cursor.execute(msg)
            conn.commit()
        else:
            print("해당 항목이 존재하지 않습니다.")

    print('- ' * 50)
    time.sleep(1)        

def sosiDelete():
    print('코드로 조회 후 삭제 처리하세요')
    dcode = int(input('삭제할 코드 입력>> '))
    msg = f"select * from sosi where code = {dcode}"
    cursor.execute(msg)
    row = cursor.fetchone()

    if row:
        print('삭제할 데이터:', row)
        confirm = input('정말 삭제하시겠습니까? (Y/N) >> ').upper()
        if confirm == 'Y':
            msg = f"delete from sosi where code = {dcode}"
            cursor.execute(msg)
            conn.commit()
            print(f"{dcode}번 코드 데이터가 삭제되었습니다.")
        else:
            print('삭제가 취소되었습니다.')
    else:
        print('해당 코드의 데이터가 없습니다.')
    print('- ' * 50)
    time.sleep(1)

while True:
    print()
    num=int(input('1등록 2출력 3조회 4수정 5삭제 9종료>>'))
    if num==9:    sys.exit()
    elif num==1:  sosiInsert()
    elif num==2:  sosiSelectAll()
    elif num==3:  sosiSelectTitle()
    elif num==4:  sosiUpdate()
    elif num==5: sosiDelete()
    else: print('처리번호를 잘못 입력하셨네요\n')