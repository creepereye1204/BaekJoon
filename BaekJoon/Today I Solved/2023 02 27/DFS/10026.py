import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

height=int(input())
grid_=[list(input().strip()) for _ in range(height)]
grid=[i.copy() for i in grid_]
width=len(grid[0])
dx=[-1,1,0,0]
dy=[0,0,1,-1]
color={'R':0,'G':0,'B':0}
color_={'R':0,'B':0}
cnt=0
def dfs(x,y,rgb,grid):
    if 0<=x<width and 0<=y <height and grid[y][x]==rgb:
        grid[y][x]='*'
        for i in range(4):
            ax=x+dx[i]
            ay=y+dy[i]
            dfs(ax,ay,rgb,grid)
for c,_ in color.items():
    for i in range(height):
        for j in range(width):
            if grid_[i][j]=='G':
                grid_[i][j]='R'
            if grid[i][j]==c:
                dfs(j,i,c,grid)
                color[c]+=1
for c,_ in color_.items():
    for i in range(height):
        for j in range(width):
            if grid_[i][j]==c:
                dfs(j,i,c,grid_)
                color_[c]+=1
print(sum(list(color.values())),sum(list(color_.values())))


