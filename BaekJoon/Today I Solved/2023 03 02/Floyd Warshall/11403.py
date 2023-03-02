import sys
INF=sys.maxsize
N=int(input())
M=[[INF]*N for _ in range(N)]
def Floyd_Warshall():
    for i in range(N):
        v=list(map(int,input().split()))
        for j in range(N):
            if v[j]==1:
                M[i][j]=v[j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                M[i][j]=min(M[i][j],M[i][k]+M[k][j])
    for i in range(N):
        for j in range(N):
            print(1 if M[i][j]!=INF else 0,end=' ')
        print()
Floyd_Warshall()
