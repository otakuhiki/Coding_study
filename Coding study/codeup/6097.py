h, w= map(int, input().split())
sato = [[0 for i in range(0,w)] for j in range(0,h)]

n = int(input())
for i in range(0,n):
    l,d,x, y=map(int, input().split())
    if (d == 0):
        for i in range(0,l):
            sato[x-1][y-1]=1
            y+=1
    elif (d == 1):
        for i in range(0,l):
            sato[x-1][y-1]=1
            x+=1
for i in range(0,h):
    for j in range(0,w):
        print(sato[i][j], end=' ')
    print()