import sys
input = sys.stdin.readline

book={} #key: title, value: name갯수
out = [] #출력할 이름을 담는 list

n= int(input())

#듣도 못한 사람의 name은 무조건 dict에 입력
for i in range(0, n):
    title = input().strip()
    if (i==0):
        book[title]=1
    else:
        #겹치는 book갯수를 카운트
        if title in book:
            book[title]+=1
        #1권씩만 있는 경우도 처리
        else:
            book[title]=1

#max()로 제일 큰 숫자를 찾아서 out에 담음
for k, v in book.items():
    if max(book.values()) == v:
        out.append(k)

#사전순으로 이름을 정렬 하여 첫번째 이름 출력
out = sorted(out)
print(out[0])