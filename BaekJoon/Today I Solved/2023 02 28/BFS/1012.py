import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
T=int(input())
def dfs(x,y):
    graph[y][x]=False
    for i in range(4):
        ax=dx[i]+x
        ay=dy[i]+y
        if 0<=ax<M and 0<=ay<N and graph[ay][ax]:
            dfs(ax,ay)
for _ in range(T):
    cnt=0
    M,N,K=map(int,input().split())
    graph=[[False]*M for _ in range(N)]
    f=[list(map(int,input().split())) for _ in range(K)]
    for X,Y in f:
        graph[Y][X]=True
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                dfs(j, i)
                cnt += 1
    print(cnt)

