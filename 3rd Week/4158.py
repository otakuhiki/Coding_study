import sys
input = sys.stdin.readline

#key: cd의 번호, value; cd갯수
while(1):
    label = 0
    cnt=0
    cd={}
    #여러개의 테스트 케이스가 반복해서 입력됨
    #최종적으로 0 0 이 입력되면 종료
    n, m = map(int, input().split())
    if (n == 0 and m ==0): break
    for i in range(0, n+m):
        label = int(input())
        #첫번째 cd는 무조건 dict에 입력
        if (i==0):
            cd[label]=1
        else:
            #겹치는 cd갯수만을 카운트
            if label in cd:
                cd[label]=2
                cnt+=1
            else:
                cd[label]=1           
    print(cnt)
