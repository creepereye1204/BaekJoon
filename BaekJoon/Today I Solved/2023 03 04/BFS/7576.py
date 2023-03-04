import sys
from collections import deque
input=sys.stdin.readline
M,N=map(int,input().split())
graph=[list((input().strip().split())) for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
good_tomato_destination=deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]=='1':
            good_tomato_destination.append((j,i))
def bfs():
    cnt=0
    while good_tomato_destination:
        Len=len(good_tomato_destination)
        for _ in range(Len):
            x,y=good_tomato_destination.popleft()
            for i in range(4):
                ax=dx[i]+x
                ay=dy[i]+y
                if 0<=ax<M and 0<=ay<N and graph[ay][ax]=='0':
                    graph[ay][ax]='1'
                    good_tomato_destination.append((ax,ay))
        cnt+=1
    for i in range(N):
        for j in range(M):
            if graph[i][j]=='0':
                return -1
                break
    else:
        return cnt-1
print(bfs())
