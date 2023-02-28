import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
m,n,v=map(int,input().split())
graph=[[] for _ in range(m+1)]
visited1=[0]*(m+1)
visited2=[0]*(m+1)

for i in range(n):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
visited1[v]=1
visited2[v]=1
def bfs(h):
    q=deque()
    q.append(h)
    while q:
        node=q.popleft()
        print(node,end=' ')
        for i in sorted(graph[node]):
            if visited1[i]==0:
                visited1[i] = 1
                q.append(i)
def dfs(h):
    print(h,end=' ')
    for i in sorted(graph[h]):
        if visited2[i]==0:
            visited2[i] = 1
            dfs(i)
dfs(v)
print('')
bfs(v)