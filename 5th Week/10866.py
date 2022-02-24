import sys
input = sys.stdin.readline

n = int(input())
dque=[]

for i in range(n):
    mode = input().split()
    if mode[0] == 'push_front':
        dque.append(mode[1])
    elif mode[0] == 'push_back':
        dque.append(mode[1])
    elif mode[0] == 'pop_front':
        if len(dque) !=0:
            print(dque.pop(0))
        else: print(-1)
    elif mode[0] == 'pop_back':
        if len(dque) !=0:
            print(dque.pop(0))
        else: print(-1)
    elif mode[0] == 'size':
        print(len(dque))
    elif mode[0] == 'empty':
        if len(dque) !=0:
            print(0)
        else: print(1)
    elif mode[0] == 'front':
        if len(dque) !=0:
            print(dque[0])
        else: print(-1) 
    elif mode[0] == 'back':
        if len(dque) !=0:
            print(dque[-1])
        else: print(-1) 