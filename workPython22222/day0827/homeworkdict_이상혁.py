# homeworkdict.py
# 이상혁 조원소스 
score_dict = {
    'Witkiew' : [100,60],
    'Dostoev' : [90,77],
    'Tolstoy' : [82,20],
    'Navokov' : [90,34]
}

list_kor = []
list_eng = []

print('이상혁님')
for key in score_dict:
    list_kor.append(score_dict[key][0])
    list_eng.append(score_dict[key][1])

for k in range(4):
    print(f'{list(score_dict.keys())[k]} {list_kor[k]+list_eng[k]} {(list_kor[k]+list_eng[k])//2}')

# 아래처럼 출력
# Witkiew 160 80
# Dostoev 167 83
# Tolstoy 102 51
# Navokov 124 62