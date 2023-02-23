import sys
from heapq import *
input = sys.stdin.readline
target=[tuple(map(int, input().split())) for _ in range(int(input()))]
target.sort()
room=[]
heappush(room,target[0][1])
for i in range(1,len(target)):
    if room[0]<=target[i][0]:
        heappop(room)
        heappush(room,target[i][1])
    else:
        heappush(room,target[i][1])
print(len(room))