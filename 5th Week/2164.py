from collections import deque
n = int(input())

card = deque([x for x in range(1,n+1)])
#print(card)
while (len(card) != 1):
    card.popleft()
    card.append(card.popleft())
print(card[0])

# list VS deque 
# 1. 마지막 원소 삭제 
# list: O(1), deque:O(1)
# 2. 첫번째 원소 삭제
# list: O(n), deque:O(1)
# listㄴ는 첫번째 원소를 삭제하면 삭제 후 모든 원소를 앞으로 이동시키기 때문에 시간 복잡도가 O(n)입니다. 
# 따라서 list로 코드를 구현 하면 시간 초과가 발생