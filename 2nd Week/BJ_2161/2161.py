import sys
input = sys.stdin.readline

n = int(input())
card = [i for i in range(1,n+1)]
out = []

while(len(card) > 1):
    print(card.pop(0), end=' ')
    temp = card.pop(0)
    card.append(temp)
print(card[0])
