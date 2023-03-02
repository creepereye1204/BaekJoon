import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    if graph[a][b]>c:#같은 경로를 다니는 버스일지라도 가성비가다름
        graph[a][b]=c
def Floyd_Warshall():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:#불가능한 경우의수 배제
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(0 if graph[i][j]==INF else graph[i][j],end=' ')
        print()
Floyd_Warshall()
print(graph)