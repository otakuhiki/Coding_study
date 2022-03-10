import heapq
import sys
input = sys.stdin.readline

#최소힙과, 최대힙을 사용하여 구현
for _ in range(int(input())):
    minq, maxq = [], []
    visited = [False for _ in range(1000001)]
    for i in range(int(input())):
        alpha, num = input().split()
        if alpha == 'I':
						#힙에 푸쉬할 때 식별자 id값으로 i를 넣음
            heapq.heappush(minq, (int(num), i))
            heapq.heappush(maxq, (-int(num), i))
            visited[i] = True  #힙에 넣을 때 visited를 True로 둠
        elif num == '-1':
						
            while minq and not visited[minq[0][1]]:
                heapq.heappop(minq)
            if minq:
								#힙에서 꺼낼 때 visited를 False로 둠으로써 만약 최소힙에서 꺼낸 값이라면 
                #최대 힙에서는 꺼내지 않도록 동기화
                visited[minq[0][1]] = False
                heapq.heappop(minq)
        else:
            while maxq and not visited[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)

    #visited가 False로 되어있는 값들은 다 꺼내논 뒤에 제대로 된 값을 heap을 통해 꺼냄
    while minq and not visited[minq[0][1]]: heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]: heapq.heappop(maxq)

    #마지막에도 쓰레기 값은 힙으로 다 꺼낸 뒤에 최대값과 최소값을 출력
    print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else'EMPTY')
