#시간초과 : 완전탐색 이외의 방법 생각해보기

import sys
input = sys.stdin.readline

#완전 탐색 -> 두 점의 x좌표나 y좌표가 같으면 x, y축에 평행 한 직선임

n = int(input())
point=[]
for i in range(0,n):
    point.append(list(map(int, input().split())))

print(point)

#반복 횟수는 nC2 
cnt = (n * n-1)/2
line = 0

for i in range(0, n):
    for j in range(i+1, n):
        if(point[i][0] == point[j][0] or point[i][1] == point[j][1]):
            line +=1
        
print(line)
