# 틀렸는데,,,모르겠네
import sys
input = sys.stdin.readline

dayWork = list(input().split())
work = { 'Re': 0, 'Pt': 0, 'Cc':0, 'Ea':0, 'Tb':0, 'Cm':0, 'Ex':0}
#print(dayWork)
cnt=0
for i in range(0, len(dayWork)):
    for key, value in work.items():
        if dayWork[i] in key:
            work[key]=value+1
total = len(dayWork)

#print(work, total)

for key, value in work.items():
    print(key, value , format(value/total, '.2f'))
print('Total', total, '1.00')

#input: Cc Pt Pt Re Tb Re Cm Cm Re Pt Pt Re Ea Ea Pt Pt Pt Re Re Cb Cb Pt Pt Cb
