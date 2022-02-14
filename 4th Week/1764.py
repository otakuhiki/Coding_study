import sys
input = sys.stdin.readline

name={} #key: name, value: name갯수
out = [] #출력할 이름을 담는 list

n, m = map(int, input().split())

#듣도 못한 사람의 name은 무조건 dict에 입력
for i in range(0, n):
    nameN = input().strip() #strip(): 개행 문자 제거
    name[nameN]=1

#도보 못한 name을 입력 받으며 겹치는 name을 out에 입력
for i in range(0, m):
    nameM = input().strip()
    if nameM in name:
        out.append(nameM)
 
#사전순으로 이름을 정렬
out = sorted(out)
#겹치는 이름 수와 이름을 출력
print(len(out))
for i in range(0, len(out)):
    print(out[i])
