import sys
input = sys.stdin.readline

n = int(input())
lst=[]
for i in range(0,n):
    lst.append(int(input()))
cnt =1
start = lst[-1]
for i in range(0,n):
    temp = lst.pop()
    if start < temp:
        cnt += 1
        start = temp
print(cnt)
