import sys

input = sys.stdin.readline
n = int(input())

for i in range(0,n):
    sentence = list(input().split())
    sentence.reverse()
    print('Case #{0}: {1}'.format(i + 1, ' '.join(sentence)))
