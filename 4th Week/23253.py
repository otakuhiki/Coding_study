import sys
input = sys.stdin.readline

#교과서를 꺼낼 수 있는 지판단하는 변수
out = True 

n, m = map(int, input().split())

for i in range(0, m):
    num = int(input())
    stacks = list(map(int,input().split()))
    #스택에 입력되는 교과서 번호가 내림차순인 경우만 
    # 교과서를 오름차순으로 정렬 가능
    for j in range(1, num):
        if stacks[j-1] < stacks[j]:
            out=False
            break

if out == True:
    print('Yes')
else: 
    print('No')