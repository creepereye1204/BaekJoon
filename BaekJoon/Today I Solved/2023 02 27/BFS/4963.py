import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
dy=[-1,-1,-1,1,1,1,0,0]
dx=[-1,0,1,-1,0,1,-1,1]
def bfs(x,y,width,height,map):
    q = deque()
    map[y][x]=0
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i in range(8):
            ax=dx[i]+x
            ay=dy[i]+y
            if 0 <= ax < width and 0 <= ay < height and map[ay][ax] == 1:
                map[ay][ax]=0
                q.append([ax,ay])

while True:
    cnt = 0
    N,M=map(int,input().split())
    if N == 0 and M == 0:
        break
    L=[list(map(int,input().split())) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if L[i][j]==1:
                bfs(j,i,N,M,L)
                cnt+=1
    print(cnt)

