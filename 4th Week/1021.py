import sys
from collections import deque
n, m = map(int, input().split())
#pop연산을 수행할 인덱스 번호 배열
popNum = list(map(int, input().split()))
q =deque([i for i in range(1,n+1)])
cnt = 0

for num in popNum:
    while 1:
        #맨 앞에 제거할 인덱스가 있는 경우
        if q[0] == num:
            q.popleft()
            break
        else:
            #위치가 앞쪽 -> 앞의 인덱스를 pop하여 뒤로 삽입
            if q.index(num) < len(popNum)/2:
                while q[0] != num:
                    q.append(q.popleft())
                    cnt+=1
            #위치가 뒷쪽 -> 뒤의 인덱스를 pop하여 앞으로 삽입
            else: 
                while q[0] != num:
                    q.append(q.pop())
                    cnt+=1
print(cnt)
