# 07comprehension.py [ 연산 if/else for~~]



message = ['spam','ham', 'spam','ham', 'spam','ham']





#문제1 for반복 ~ if
#spam출력, 개수출력

for k in message:
    if k=='spam':
        print(k, end = ' ')


print()
#문제2 [만앞 if조건 else 불뒤 for] comprehension처리
#문제2 [만앞 for~~~ if 조건만족] comprehension처리
temp_list = [ k for k in message if k == 'spam'] #방법1
temp_list = [ k for k in message if 'spam' in k] #방법2
print(temp_list)




#문제3 spam = 0 ham =1  dummy = [0,1,0,1,0,0] 
#message = ['spam','ham', 'spam','ham', 'spam','ham']
dummy = [0 if k == 'spam' else 1 for k in message]

print(dummy)