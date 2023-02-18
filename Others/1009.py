import sys
N=int(input())
for i in range(N):
    a,b=sys.stdin.readline().split()
    print(int(a[-1])**int(b[-1])%10)

