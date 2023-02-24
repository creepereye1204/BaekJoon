import sys
import heapq

input = sys.stdin.readline
N = int(input())
L = [int(input()) for _ in range(N)]

L.sort()
Minus = []
zero = 1
one = 0
Plus = []
postive = []
result = 0

for i in range(N):
    if L[i] < 0:
        Minus.append(L[i])
    elif L[i] == 0:
        zero = 0
    elif L[i] == 1:
        one += 1
    else:
        Plus.append(L[i])

for _ in range(len(Minus)):
    if len(Minus) >= 2:
        x = heapq.heappop(Minus)
        y = heapq.heappop(Minus)
        result += x * y
    elif len(Minus)==1:
        result += heapq.heappop(Minus) * zero
        break
for p in Plus:
    heapq.heappush(postive, (-p, p))
for _ in range(len(postive)):
    if len(postive) >= 2:
        x = heapq.heappop(postive)[1]
        y = heapq.heappop(postive)[1]
        result += x * y
    elif len(postive)==1:
        result += heapq.heappop(postive)[1]
        break
print(result+one)


















