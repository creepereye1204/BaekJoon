import sys
import copy
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

Max=max(max(graph))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
target=0
def dfs(x,y,k,deep):
    deep[y][x]=False
    for i in range(4):
        ax=x+dx[i]
        ay=y+dy[i]
        if 0<=ax<N and 0<=ay<N and deep[ay][ax] and graph[ay][ax]>k:
            dfs(ax,ay,k,deep)


for k in range(Max):
    deep=[[True]*N for _ in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if graph[i][j]>k and deep[i][j]:
                dfs(j,i,k,deep)
                cnt+=1

    target=max(target,cnt)
print(target)