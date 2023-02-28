import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
x,y=map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
def dfs(v):
    print(graph[v])
    for i in graph[v]:
        if visited[i]==0:
            visited[i]+=visited[v]+1
            dfs(i)
dfs(x)
print(visited[y] if visited[y]>0 else -1)

