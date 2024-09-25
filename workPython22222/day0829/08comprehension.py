# 08comprehension.py [ 연산 if/else for~~]



message = ['spam','ham', 'spam','ham', 'spam','ham']





#문제1 for반복 ~ if
#spam출력, 개수출력
msg_cnt=0
for k in message:
    if k == 'spam':
        print(k, end = ' ')
        msg_cnt = msg_cnt +1


print()
print('개수', message.count('spam'))
print('개수', msg_cnt)
temp_list = [ k for k in message if k == 'spam'] #방법1
# temp_list = [ k for k in message if 'spam' in k] #방법2
# print(temp_list)




#문제3 spam = 0 ham =1  dummy = [1,1,0,1,0,1,0] 
#message = ['ham','ham','spam','ham','spam','ham','spam']
mydummy = [0 if k == 'spam' else 1 for k in message]

print('comprehension', mydummy)