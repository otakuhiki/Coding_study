import sys
input = sys.stdin.readline

n = int(input())
que=[]

for i in range(n):
    mode = input().split()
    if mode[0] == 'push':
        que.append(mode[1])
    elif mode[0] == 'pop':
        if len(que) !=0:
            print(que.pop())
        else: print(-1)
    elif mode[0] == 'size':
        print(len(que))
    elif mode[0] == 'empty':
        if len(que) !=0:
            print(0)
        else: print(1)
    elif mode[0] == 'front':
        if len(que) !=0:
            print(que[0])
        else: print(-1) 
    elif mode[0] == 'back':
        if len(que) !=0:
            print(que[-1])
        else: print(-1) 