import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
dy=[-1,-1,-1,1,1,1,0,0]
dx=[-1,0,1,-1,0,1,-1,1]
def dfs(x,y,width,height,map):
    if 0<=x<width and 0<=y<height and map[y][x]==1:
        map[y][x]=0
        for i in range(8):
            dfs(x+dx[i],y+dy[i],width,height,map)
while True:
    cnt = 0
    N,M=map(int,input().split())
    if N == 0 and M == 0:
        break
    L=[list(map(int,input().split())) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if L[i][j]==1:
                dfs(j,i,N,M,L)
                cnt+=1
    print(cnt)

