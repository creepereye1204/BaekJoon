import sys
input=sys.stdin.readline
N=int(input())
L=sorted(list(map(int,input().split())))
T=1
for arr in L:
    if T<arr:
        break
    T+=arr
print(T)






