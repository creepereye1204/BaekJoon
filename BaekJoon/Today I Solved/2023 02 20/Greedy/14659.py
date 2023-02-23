import sys
input=sys.stdin.readline
N=int(input())
M=list(map(int,input().split()))
cnt=0
target=0
result=0
for m in M:
    if cnt>m:
        target+=1
        result=max(result,target)
    else:
        cnt=m
        target=0
print(result)