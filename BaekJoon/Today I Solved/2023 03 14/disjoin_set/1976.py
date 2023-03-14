import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
travels={i:set([]) for i in range(1,N+1)}
for i in range(N):
    loc=list(map(int,input().split()))
    travels[i+1]|=set([i+1])
    for j in range(N):
        if loc[j]==1:
            travels[i+1]|=set([j+1])

for key,value in travels.items():
        for i,j in travels.items():
            if j & value:
                travels[key]|=j
go=list(map(int,input().split()))
start= travels[go[0]]

for i in go:
    if set([i]) & start:
        continue
    print('NO')
    break
else:
    print("YES")

