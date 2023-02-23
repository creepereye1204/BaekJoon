import sys
from heapq import *
input=sys.stdin.readline
M=[int(input()) for _ in range(int(input()))]
heapify(M)
result=0
while len(M)>1:
    plus=heappop(M)+heappop(M)
    result+=plus
    heappush(M,plus)
else:
    print(result)
