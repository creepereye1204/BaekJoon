import sys
input=sys.stdin.readline
_,M=map(int,input().split())
L=sorted(list(map(int,input().split())))
Plus=[]
Minus=[]
target=[]
for i in L:
    if i<0:
       Minus.append(abs(i))
    else:
       Plus.append(i)
Plus=sorted(Plus,reverse=True)
for i in range(0, len(Minus) // M):
    target.append(Minus[i * M])
if len(Minus) % M > 0:
    target.append(Minus[(len(Minus) // M) * M])
for i in range(0, len(Plus) // M):
    target.append(Plus[i * M])
if len(Plus) % M > 0:
    target.append(Plus[(len(Plus) // M) * M])
target =sorted(target)
print(sum(2*target[:-1])+target[-1])
#








