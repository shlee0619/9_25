# 14sortbubble.py
print()

a = [ 4, 7, 5, 1, 2]
for i in range(4):
    for j in range(i,5):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
            
    
    print(a)    #작은바퀴회전후 출력

# [1, 7, 5, 4, 2]
# [1, 2, 7, 5, 4]
# [1, 2, 4, 7, 5]
# [1, 2, 4, 5, 7]

# i=0일때 1>2
    # 1 7 5 4 2
# i=1일때  7 > 5
    # 1 5 
# i=2일때
# i=3일때
# i=4일때