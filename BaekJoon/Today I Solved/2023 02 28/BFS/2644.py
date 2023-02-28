import sys
from collections import deque
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
def bfs(v):
    q=deque()
    q.append(v)
    while q:
        node=q.popleft()
        for gr in graph[node]:
            if visited[gr]==0:
                visited[gr]=visited[node]+1
                q.append(gr)
bfs(x)
print(visited[y] if visited[y]>0 else -1)

