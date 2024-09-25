# homeworkmilk.py
apart = [[101,102,103,104],
         [201,202,203,204],
         [301,302,303,304],
         [401,402,403,404]
         ]

unpaid = [101,204,302,403]

#힌트 중첩 for 



for a in range(len(apart)):
    for b in range(len(apart[a])):
        if apart[a][b] in unpaid:
            print(f'{apart[a][b]} 우유 배달 중지x')
        else:
            print(f'{apart[a][b]} 우유 배달 계속o')
    print()