import sys
input=sys.stdin.readline
G=int(input().strip())
P=int(input().strip())
parent={i:i for i in range(10**5+1)}
plane=[]
cnt=0
def union(x,y):
    a=find(x)
    b=find(y)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
for _ in range(P):
    plan=int(input().strip())
    plane.append(plan)
for plan in plane:
    x=find(plan)
    if x==0:
        break
    union(x,x-1)
    cnt+=1
print(cnt)