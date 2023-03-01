import sys
input=sys.stdin.readline
n=[[0]*15 for _ in range(15)]

for i in range(15):
    n[0][i]+=i
else:
    for i in range(1,15):
        for j in range(1,15):
            n[i][j]=n[i][j-1]+n[i-1][j]
T=int(input())
for _ in range(T):
    y=int(input())
    x=int(input())
    print(n[y][x])



