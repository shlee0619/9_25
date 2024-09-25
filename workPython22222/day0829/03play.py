# 03play.py
import time
import game #물리적인 파일명만 명시
print('03play 사용문서')


print(game.user_id)
print(game.user_pwd)


game.terran()


game.LG('그램')


meter = game.running()
print('코스길이', meter)
print('코스길이 ', game.running())

# game.py문서
# 전역변수 user_id, user_pwd
# terran() LG(lg) running() 리턴값 있음