import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())
k = int(input())

card = []
for i in range(n):
    card.append(int(input().readline()))

result = set()
for i in list(permutations(card, k)):
    result.add(''.join(list(map(str, i))))

print(len(result))