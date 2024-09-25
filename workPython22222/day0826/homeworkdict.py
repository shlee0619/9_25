# homeworkdict.py

# 김자바, 이합격,  박이썬
# aaa bbb ccc kim  lee goo
score_dict = {
    '김자바':[100,60] , 
    '이합격':[90,77], 
    'kang':[82,34], 
    'park' : [90,34] 
}

list_kor = []
list_eng = []
for data in score_dict.values():
    list_kor.append(data[0])
    list_eng.append(data[1])

    hap_kor = sum(list_kor)
    hap_eng = sum(list_eng)
    print(hap_kor, hap_kor//2)
    print(hap_eng, hap_eng//2)


# 아래처럼 출력
# 김자바 160  80
# 이합격 167  83
# 강감찬 116  58
# 박이썬 124  62

print()
print('- ' * 50)
