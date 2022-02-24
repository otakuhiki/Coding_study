out=[]  #결과를 담는 배열
n = int(input())

for _ in range(n):
    ps=input()
    #key: ( 또는 ), value: 횟수
    check=dict()

    #입력받은 괄호를 쪼개서 카운트
    for i in range(0, len(ps)):
        if ps[i] == '(':
            check['(']=check.get('(',0)+1
        elif ps[i] == ')':
            check[')']=check.get(')',0)+1
    
    #왼쪽 괄호 수 != 오른쪽 괄호 수 
    if check.get('(') != check.get(')'):
        out.append('NO')
    #왼쪽 괄호 수 == 오른쪽 괄호 수 
    else: out.append('YES')

for answer in out:
    print(answer)