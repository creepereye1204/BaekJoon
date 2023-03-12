cnt=0
_,M=map(int,input().split())
knowList=set(input().strip().split()[1:])
partys=[set(input().split()[1:]) for _ in range(M)]
for _ in range(M):
    for party in partys:
        if knowList & party:
            knowList=knowList | party
for party in partys:
    if party & knowList:
        continue
    cnt+=1
print(cnt)