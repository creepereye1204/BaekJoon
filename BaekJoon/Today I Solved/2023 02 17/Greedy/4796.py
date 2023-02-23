import sys
c=1
while True:
    L, P, V = map(int, sys.stdin.readline().strip().split())
    if L==0:
        break
    a=V//P
    b=V%P
    value=str(L*a+(b if b<=L else L))
    print(f"Case {str(c)}: {value}")
    c += 1
