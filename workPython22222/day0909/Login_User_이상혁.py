#Login_User_이상혁.py


# import cx_Oracle
# import time

from datetime import datetime
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
    'database' : 'work_python_id_login',
    'port' : 3306

}


CN = pymysql.connect(**config)
cursor = CN.cursor()


def sign_up():
    print("=== 회원 가입 ===")
    userid = input("아이디: ")
    userpwd = input("비밀번호: ")

    sql = "INSERT INTO login (userid, userpwd) VALUES (%s, %s)"
    val = (userid, userpwd)
    try:
        cursor.execute(sql, val)
        CN.commit()
        print("회원 가입이 완료되었습니다.")
    except pymysql.IntegrityError:
        print("이미 존재하는 아이디입니다.")

def login():
    print("=== 로그인 ===")
    userid = input("아이디: ")
    userpwd = input("비밀번호: ")

    sql = "SELECT * FROM login WHERE userid = %s AND userpwd = %s"
    val = (userid, userpwd)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        print("로그인 성공!")
        return userid
    else:
        print("로그인 실패!")
        return None

def register_product():
    print("=== 상품 등록 ===")
    product_code = input("상품 코드: ")
    product_name = input("상품명: ")

    sql = "INSERT INTO product (product_code, product_name) VALUES (%s, %s)"
    val = (product_code, product_name)
    try:
        cursor.execute(sql, val)
        CN.commit()
        print("상품이 등록되었습니다.")
    except pymysql.IntegrityError:
        print("이미 존재하는 상품 코드입니다.")

def place_order(userid):
    print("=== 주문하기 ===")
    product_code = input("주문할 상품 코드: ")
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql = "INSERT INTO user_order (userid, product_code, order_date) VALUES (%s, %s, %s)"
    val = (userid, product_code, order_date)
    try:
        cursor.execute(sql, val)
        CN.commit()
        print("주문이 완료되었습니다.")
    except pymysql.IntegrityError:
        print("유효하지 않은 사용자 ID 또는 상품 코드입니다.")

def main():
    logged_in_user = None
    while True:
        print("\n=== 메뉴 ===")
        print("1. 가입")
        print("2. 로그인")
        print("3. 상품 등록")
        print("4. 주문")
        print("9. 종료")

        choice = input("선택: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            logged_in_user = login()
            if logged_in_user:
                print(f"{logged_in_user}님 환영합니다.")
        elif choice == '3':
            if logged_in_user:
                register_product()
            else:
                print("먼저 로그인해주세요.")
        elif choice == '4':
            if logged_in_user:
                place_order(logged_in_user)
            else:
                print("먼저 로그인해주세요.")
        elif choice == '9':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()

cursor.close()
CN.close()


