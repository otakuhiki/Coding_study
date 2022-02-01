import sys
from collections import deque
n = int(input())

q =deque([i for i in range(1,n+1)])
#print(q)

num = n
for i in range (1,n):
    
    out = (i **3) % num
    if (out==1):
        print(q)
        print('turn: ',i)
        print('out:', out)
        q.popleft()     
        num-=1
    else: 
        print(q)
        print('out:', out)
        print('turn: ',i)
        q.rotate(-(out-1))
        q.popleft() 
        num-=1
        
print(q[0])

