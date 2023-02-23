import sys
input=sys.stdin.readline
N,C=map(int,input().split())
H=int(input())
M=[list(map(int,input().split())) for _ in range(H)]
M.sort(key=lambda x:x[1])
Box=[C]*(N+1)
answer=0
for s,e,b in M:
    _min=C
    print(Box)
    for i in range(s,e):
        _min=min(_min,Box[i])
    _min=min(_min,b)
    for i in range(s,e):
        Box[i]-=_min
    answer+=_min

print(Box)
