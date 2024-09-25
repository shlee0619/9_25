apart=[
    [101,102,103,104],
    [201,202,203,204],
    [301,302,303,304],
    [401,402,403,404]
]

unpaid=[101,204,302,403]


print('황두경님')
for a in range(len(apart)):
    for b in range(len(apart[a])):
        if apart[a][b] in unpaid:
            print (apart[a][b],'우유배달❌',end=' ')
        else :
            print (apart[a][b],'우유배달⚪',end=' ')
    print()