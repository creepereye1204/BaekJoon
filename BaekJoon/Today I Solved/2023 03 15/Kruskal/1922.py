import sys
input=sys.stdin.readline
def union(x,y):
    a=find(x)
    b=find(y)
    if a<b:
        Parent[b]=a
    else:
        Parent[a]=b
def find(x):
    if Parent[x]!=x:
        Parent[x]=find(Parent[x])
    return Parent[x]
N=int(input())
M=int(input())
Parent=[i for i in range(N+1)]
NetWork=[list(map(int,input().split())) for _ in range(M)]
NetWork.sort(key=lambda x:x[2])
result=0
for i in range(M):
    if find(NetWork[i][0])!=find(NetWork[i][1]):
        union(NetWork[i][0],NetWork[i][1])
        result+=NetWork[i][2]
print(result)