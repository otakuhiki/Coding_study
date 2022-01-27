miro=[]
for i in range(10):
    miro.append(list(map(int, input().split())))

x = 1
y = 1
miro[1][1]=9
while(1):
    if (miro[y][x+1] == 0): #오른쪽이 0 -> 오른쪽으로
        #ant[y][x] = miro[y][x+1]
        miro[y][x] = 9
        miro[y][x+1] = 9
        x+=1
    elif (miro[y][x+1] == 1): #오른쪽이 1 -> 아래확인    
        if (miro[y+1][x] == 1): #아래 확인
            miro[y][x] = 9
            break
        elif(miro[y+1][x] == 0): #아래0 -> 아래로이동
            #ant[y][x] = miro[y+1][x]
            miro[y][x] = 9
            miro[y+1][x] =9
            y+=1
        elif(miro[y+1][x] == 2):
            miro[y][x] = 9
            #ant[y][x] = miro[y][x+1]
            miro[y+1][x] = 9
            break
    elif (miro[y][x+1] == 2):
        miro[y][x] = 9
        #ant[y][x] = miro[y][x+1]
        miro[y][x+1] = 9
        break   
for i in range(10):
    for j in range(10):
        print(miro[i][j], end=' ') 
    print()
