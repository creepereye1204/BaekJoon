import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q=deque()
    q.append(1)
    visited[1]=1
    while q:
        now=q.popleft()
        for c in tree[now]:
            if not visited[c]:
                visited[c]=now
                q.append(c)

T=int(input().strip())
tree=[[] for i in range(T+1)]
visited=[0]*(T+1)
for _ in range (T-1):
    x,y=map(int,input().split())
    tree[x]+=[y]
    tree[y]+=[x]
bfs()
for i in visited[2:]:
    print(i)
