import sys
INF=sys.maxsize
input=sys.stdin.readline
N,M=map(int,input().split())
K=[[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    K[a][b]=1
    K[b][a]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i!=j:
                K[i][j]=min(K[i][j],K[i][k]+K[k][j])
            else:
                K[i][j]=0
result=INF
index=0
for i in range(1,N+1):
    if sum(K[i][1:])<result:
        index=i
        result=sum(K[i][1:])
print(index)