baduk=[]
for i in range(19):
    baduk.append(list(map(int, input().split())))

n=int(input())
for i in range(0,n):
    x, y = map(int, input().split())
    for j in range(19):
        if baduk[x-1][j]==1:
            baduk[x-1][j]=0
        elif baduk[x-1][j]==0:
            baduk[x-1][j]=1
        
        if baduk[j][y-1]==1:
            baduk[j][y-1]=0
        elif baduk[j][y-1]==0:
            baduk[j][y-1]=1 

for i in range(19):
    for j in range(19):
        print(baduk[i][j], end=' ') 
    print()