import sys
from heapq import *
input=sys.stdin.readline
N,K=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(N)]
C=[int(input()) for _ in range(K)]
heapify(L)
C.sort()
result=0
jew_value=[]
for c in C:
    while len(L)!=0 and L[0][0]<=c:
        heappush(jew_value,-heappop(L)[1])
    if jew_value:
        result-=heappop(jew_value)
print(result)
