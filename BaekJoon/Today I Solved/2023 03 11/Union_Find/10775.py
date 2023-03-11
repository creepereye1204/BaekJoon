import sys
input=sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

read = sys.stdin.readline
G = int(read().strip("\n"))
P = int(read().strip("\n"))
parent = {i: i for i in range(0, G+1)}
planes = []
count = 0

for _ in range(P):
    planes.append(int(read().strip("\n")))
for plane in planes:
    x = find(plane)

    if x == 0:
        break
    union(x, x-1)
    count += 1

print(count)