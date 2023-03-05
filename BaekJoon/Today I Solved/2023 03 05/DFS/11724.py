import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[True]*(1+N)
cnt=0
def dfs(start):
    visited[start]=False
    for i in graph[start]:
        if visited[i]:
            dfs(i)
for i in range(1,N+1):
    if visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

