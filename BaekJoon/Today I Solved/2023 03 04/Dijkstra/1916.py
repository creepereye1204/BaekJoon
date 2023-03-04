import sys
from heapq import *
INF=sys.maxsize
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
start,end=map(int,input().split())
def dijkstra(start):
    q=[]
    distances=[INF]*(n+1)
    distances[start]=0
    heappush(q,[0,start])
    while q:
        current_distance,current_destination=heappop(q)

        if distances[current_destination]<current_distance:
            continue

        for new_destination,new_distance in graph[current_destination]:
            distance=new_distance+current_distance
            if distance<distances[new_destination]:
                distances[new_destination]=distance
                heappush(q,[distance,new_destination])
    return distances

print(dijkstra(start)[end])