from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
q = deque([i for i in range(1,n+1)])
#print(q)
target = 0
cnt=1
output = []
while(cnt!= n+1):
    #target = target + k
    q.rotate(-(k-1))
    print(q)
    out = q.popleft()
    output.append(out)
    cnt+=1
    print('-제거된 사람: ', out, '\n', '-제거 후: ' , q)

print('<', end='')
print(*output, sep=', ', end='')
print('>')

