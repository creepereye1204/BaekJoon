import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    graph[b]+=[a]
    graph[a]+=[b]
def dfs(root):
    visited[root]=1
    for i in graph[root]:
        if visited[i]==0:
            dfs(i)

dfs(1)
print(sum(visited)-1)







