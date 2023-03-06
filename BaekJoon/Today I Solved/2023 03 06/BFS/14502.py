import sys
import copy
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
global target
target=0
def make_wall(cnt=0):
    if cnt==3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                make_wall(cnt+1)
                graph[i][j]=0
def bfs():
    global target
    Max=0
    map=copy.deepcopy(graph)
    q=deque()
    for i in range(N):
        for j in range(M):
            if map[i][j]==2:
                q.append((j,i))


    while q:
        x,y=q.popleft()
        for i in range(4):
            ax=dx[i]+x
            ay=dy[i]+y
            if 0<=ax<M and 0<=ay<N and map[ay][ax]==0:
                map[ay][ax]=2
                q.append((ax,ay))
    for i in range(N):
        for j in range(M):
            if map[i][j]==0:
                Max+=1
    target=max(Max,target)
make_wall()
print(target)
    
