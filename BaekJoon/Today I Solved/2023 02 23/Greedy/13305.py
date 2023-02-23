import sys
input=sys.stdin.readline
N=int(input())
root=list(map(int,input().split()))
city=list(map(int,input().split()))
Min=city[0]
result=0
for i in range(len(root)):
    if Min>city[i]:
        Min=city[i]
    result+=Min*root[i]
print(result)