import sys
input=sys.stdin.readline
N=int(input().strip())
rate=[int(input().strip()) for _ in range(N)]
rate.sort()
result=0
for i in range(1,N+1):
    result+=abs(rate[i-1]-i)
print(result)