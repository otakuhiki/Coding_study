n = int(input())
out= []

for _ in range(n):
    num = int(input())
    # 금액은 오름차순으로 입력됨
    price = list(map(int, input().split()))
    outCase=[]
    
    while(len(price)):
        # 125%에 해결하는 금액이 있으면 pop()을 하여 출력 배열에 삽입
        if price[0]*4/3 in price:
            price.pop(price.index(price[0]*4/3))
            outCase.append(price.pop(0))
        # 할인 금액만 찾으면 되므로 나머지는 그냥 pop()
        else: price.pop(0)
    # Case별로 출력해야 함
    out.append(outCase)

for i in range(n):
    print("Case #{}:".format(i+1,),end=" ") 
    for j in range(len(out[i])):
        print(out[i][j],end=" ")
    print()
