import sys
input = sys.stdin.readline

n = int(input())
stack=[]

for i in range(n):
    mode = input().split()
    if mode[0] == 'push':
        stack.append(mode[1])
    elif mode[0] == 'pop':
        if len(stack) !=0:
            print(stack.pop())
        else: print(-1)
    elif mode[0] == 'size':
        print(len(stack))
    elif mode[0] == 'enpty':
        if len(stack) !=0:
            print(0)
        else: print(1)
    elif mode[0] == 'top':
        if len(stack) !=0:
            print(stack[-1])
        else: print(-1)  