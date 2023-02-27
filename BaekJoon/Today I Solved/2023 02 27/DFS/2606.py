import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
graph=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[b][a]=graph[a][b]=1



