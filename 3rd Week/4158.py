import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cd_n = []
cd_m = []

for _ in range(n):
    cd_n.append(int(input()))
for _ in range(m):
    cd_m.append(int(input()))
    if len(cd_m) == m:
       end1, end2 = map(int, input().split())

print(cd_n, cd_m)

n_idx = 0
m_idx = 0
cnt = 0

while(n_idx != n):
    check = cd_n[n_idx]
    if check in cd_m:
        cnt+=1
        n_idx +=1
    else:
        n_idx+=1

# while(n_idx != n):
#     check = cd_n[n_idx]
#     if cd_m[m_idx] == check:
#         #print(3)
#         cnt+=1
#         m_idx+=1
#         if (m_idx == m): 
#             n_idx+=1
#             m_idx = 0 
#             #print(4)
#     else:
#         #print(5)
#         m_idx+=1
#         if (m_idx == m): 
#             n_idx+=1
#             m_idx = 0
#             #print(6)

print(cnt)

