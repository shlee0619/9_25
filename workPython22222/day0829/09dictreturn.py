# 09dictreturn.py

# 함수의 리턴값 1개이상처리
# 함수의 매개인자 1개이상처리 (*args)

def score_procedure(score_dict):
    list_kor = []
    list_eng =[]
    for key in score_dict:
        list_kor.append(score_dict[key][0])
        list_eng.append(score_dict[key][1])

    return sum(list_kor), sum(list_eng), sum(list_kor)//len(list_kor), sum(list_eng)//len(list_eng)


score = {
    'david':[100,60], 
    'foster':[90,77], 
    'wallace':[82,34]}

a,b,c,d = score_procedure
print('국어총점', a)
print('영어총점', b)
print('국어평균', c)
print('영어평균', d)




