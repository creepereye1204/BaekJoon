import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
travels=[]
for i in range(N):
    travel=[]
    loc=list(map(int,input().split()))
    for j in range(N):
        if loc[j]==1:
            travel.append(i+1)
            travel.append(j+1)
    travels.append(set(travel))

go=set(list(map(int,input().split())))
v=set([])
f=True
for i in go:
    if v & set([i]) or f:
        f=False
        v=set([])
        for travel in travels:
            if set([i]) & set(travel):
                v=v| set([i]) | set(travel)
    else:
        print('NO')
        exit()
print('YES')