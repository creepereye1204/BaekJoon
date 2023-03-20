import sys
from collections import deque

input=sys.stdin.readline
dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,-1,1]
def bfs(x,y,x_,y_):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        if x==x_ and y==y_:
            return graph[y][x]
        for i in range(8):
            ax=x+dx[i]
            ay=y+dy[i]
            if 0<=ax<board and 0<=ay<board and graph[ay][ax]==0:
                graph[ay][ax]+=graph[y][x]+1
                q.append((ax,ay))

T=int(input().strip())
for _ in range(T):
    board=int(input().strip())
    graph=[[0]*board for _ in range(board)]
    x,y=map(int,input().split())
    x_,y_=map(int,input().split())
    print(bfs(x,y,x_,y_))
