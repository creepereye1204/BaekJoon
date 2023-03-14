import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
parent=[i for i in range(N+1)]
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

for i in range(N):
    city=list(map(int,input().split()))
    for j in range(N):
        if city[j]==1:
            union(i+1,j+1)
path=list(map(int,input().split()))
root=set([find(i) for i in path])
print('YES' if len(root)==1 else 'NO')
