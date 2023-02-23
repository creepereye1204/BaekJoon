import sys
from heapq import *
input=sys.stdin.readline
_,m=map(int,input().split())
a=list(map(int,input().split()))
heapify(a)
for _ in range(m):
    x,y = heappop(a),heappop(a)
    z=x+y
    heappush(a,z)
    heappush(a,z)
print(sum(a))




