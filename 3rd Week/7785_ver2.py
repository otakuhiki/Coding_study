import sys
input = sys.stdin.readline

n = int(input())
entryCheck = {}
cnt=0

for i in range(n):
    company = []
    company.append(list(input().split()))
    entryCheck[company[0][0]]=company[0][1]

name=[]
for key in entryCheck:
    name.append(key)

num = len(name)
name = sorted(name, reverse = True)
for i in range(num):
    if entryCheck[name[i]] == 'enter':
        print(name[i])