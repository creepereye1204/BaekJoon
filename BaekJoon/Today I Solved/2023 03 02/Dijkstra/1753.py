# import sys
# from heapq import *
# INF=sys.maxsize
# input=sys.stdin.readline
# def Dijkstra(graph,start):
#     distances={node:INF for node in graph}
#     distances[start]=0
#     queue=[]
#     heappush(queue,[distances[start],start])
#     while queue:
#         current_distance,current_destination=heappop(queue)
#         for new_distance,new_destination in graph[current_destination]:
#             if graph[new_destination]<new_distance:
#                 continue
#             distance = new_distance + current_distance
#             if distance<distances[new_destination]:
#                 distances[current_destination]=distances
#                 heappush([distance,new_destination])
#
# V,E=map(int,input().split())
# K=int(input())
# for _ in range(E):
#     u,v,w=map(int,input().split())
#
#
#
