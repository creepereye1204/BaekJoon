import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(M)]
parent=[i for i in range(N+1)]
graph.sort(key=lambda x:x[2])
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    a=find(x)
    b=find(y)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
cnt=0
ans=0
for i in graph:
    if find(i[0])!=find(i[1]):
        union(i[0],i[1])
        ans+=i[2]
        cnt=i[2]
print(ans-cnt)
