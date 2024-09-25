import numpy  as np

x = [3,5,9]
y = [2,7,4]

#에러 print(x*y) Error: can't multiply sequence by non-int of type 'list'

z = np.array(x)*np.array(y)
print(z) #[ 6 35 36]
print()
my = np.concatenate( (x,y) ) #[3 5 9 2 7 4]
print(my)

#에러 my = np.concatenate(x,y)
#에러 print( np.concatenate(x,y) )

print()
data = np.array([9,2,5,1,3,8,6,4,7])
data.sort()
print(data) #[1 2 3 4 5 6 7 8 9]
print(data.shape)
print(data.size)  #len대신 넘피에서 size기술


my = np.array( [
    [ [1,2,3,4], [56,43,7,8] ],
    [ [9,2,3,7], [39,43,5,9]],
    [ [1,5,3,8], [24,43,6,1]],
    [ [6,2,3,4], [71,43,2,3]],
 ])

print(my)
print('my.size = ' ,my.size )
print('my.shape = ' , my.shape )
print('my.ndim = ', my.ndim) 

'''
my.size =  32 = 4*8
my.shape =  (4면, 2행, 4열)
my.ndim =  3차원
'''


print()