import sys
input=sys.stdin.readline
C=[int(input()) for _ in range(int(input()))]
calc=[25,10,5,1]
for c in C:
    rest=c
    target=[0,0,0,0]
    for i in range(len(calc)):
        target[i],rest=rest//calc[i],rest%calc[i]
        print(target[i],end=' ')
    print('')

