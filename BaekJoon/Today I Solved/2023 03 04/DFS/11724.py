import sys

input=sys.stdin.readline
N,M=map(int,input().split())
graph=[False for _ in range(N+1) for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    graph[u][v],graph[v][u]=True
def dfs(x,y):
    if 0<=x<N and 0<=Y<N :


