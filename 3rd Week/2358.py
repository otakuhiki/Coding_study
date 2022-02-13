import sys
input = sys.stdin.readline

#두 점의 x좌표나 y좌표가 같으면 x, y축에 평행 한 직선
#(2,1)(2,2)와 (2,1)(2,3)은 같은 직선

n = int(input())
pointX={}
pointY={}
cnt = 0

# key:각 좌표, value:갯수
#x,y좌표를 따로 dict의 key로 넣어서 해당 key가 있을 경우 value를 더해줌 

for i in range(0,n):
    x, y = map(int, input().split())
    if x in pointX:     
        pointX[x]+=1
    else:
        pointX[x]=1
    if y in pointY:
        pointY[y]+=1
    else:
        pointY[y]=1

#좌표 갯수가 2개이상인 key를 세줌
for k, v in pointX.items():
    if pointX[k] != 1:
        cnt+=1
for k, v in pointY.items():
    if pointY[k] != 1:
        cnt+=1
        
print(cnt)
