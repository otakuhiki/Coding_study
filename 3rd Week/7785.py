import sys
input = sys.stdin.readline

n = int(input())
entryCheck = {}
cnt=0

for i in range(n):
    name, status = map(str, input().split())
    if status == 'enter':
        entryCheck[name] = status
    elif status == 'leave':
        del entryCheck[name]

out = sorted(entryCheck.keys(), reverse = True)
for i in out:
    print(i)


