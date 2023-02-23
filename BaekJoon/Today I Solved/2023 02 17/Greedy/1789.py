import math
I=int(input())
C=int(math.sqrt(2*I))
while True:
    if C*(C+1)<=2*I:
        print(C)
        break
    else:
        C-=1