import sys
input = sys.stdin.readline

n = int(input())
stack =[]
out = []
cnt=1 #스택에 들어가는 숫자를 카운트
    
for _ in range(0,n):
    num = int(input())
    # num으로 입력받은 숫자가 스택에 입력 될 때까지 push
    while cnt <= num :
        stack.append(cnt)
        cnt+=1
        out.append('+')
    # 스택의 맨 위의 숫자와 num이 일치 => 수열 가능 => pop
    if stack[-1] == num:
        stack.pop()
        out.append('-')
    # 불일치 => 수열을 불가능 => 종료
    else: 
        print('NO')
        exit(0)

# 수열을 만드는 push, pop절차 출력
for i in out:
    print(i)
