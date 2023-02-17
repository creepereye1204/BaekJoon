import sys
input=sys.stdin.readline
target=[]
c=1
while True:
    L, P, V = map(int, input().strip().split())
    if L==0:
        break
    a=V//P
    b=V%P
    case='Case '+str(c)+': '+str(L*a+(b if b<=L else L))
    c+=1
    print(case)
