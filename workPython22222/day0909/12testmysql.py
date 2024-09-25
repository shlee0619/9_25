#12testmysql.py


# import cx_Oracle
# import time

import pymysql

configOracle = {
    
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
    
}

config = {

    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '1234',
    'database' : 'naver',
    'port' : 3306

}


CN = pymysql.connect(**config)
cursor = CN.cursor()


def testInsert():
    dcode = int(input('코드입력>> '))
    dname = input('이름입력>> ')
    msg = f"insert into test values ({dcode}, '{dname}', 0, now())"
    cursor.execute(msg)
    CN.commit()

def testSelectAll():
    msg = "select * from test "
    cursor.execute(msg)
    rows = cursor.fetchall()
    for r in rows:
        print(r[0], r[1], r[2], r[3] )
        
    print('레코드갯수 ', len(rows))

def testUpdate():
    
    fixcode = int(input('수정할 코드 입력>> '))
    fcode = int(input('코드명 수정>>'))
    fname = input('이름 수정>>')
    msg = f"update test set code = {fcode}, name = '{fname}', 0, now() where code = {fixcode}"
    cursor.execute(msg)
    CN.commit()

def testDelete():
    pass

testInsert()
print()

while True:
    print()
    sel = int(input('1등록 2전체출력 3수정 4삭제 5이름조회 9종료>>>>  '))
    if sel == 9:
        break
    elif sel == 1:
        print('test테이블 신규등록 처리입니다')
        testInsert()
        testSelectAll()
    elif sel == 2:
        testSelectAll()
    elif sel == 3: #수정 update ~ where
        testUpdate()
    elif sel == 4: #삭제 delete ~ where
        pass
    elif sel == 5: #이름조회
        pass
    else:
        print('작업번호를 잘못 선택하셨습니다.')


# web웹태그 + css = 방명록, 게시판, 인스타 가능
# web웹태그 code, name, title, 조회수, 날짜, 이미지
  # 댓글기능까지 있으면 완벽한 프로그램
  # 로그인처리 userid, password


print('- '* 50)
print()


