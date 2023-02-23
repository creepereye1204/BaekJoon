N,L=(map(int,input().split()))
I=(list(map(int,input()))).sort()
T=I[0]+L-1
C=1
for i in range(1,len(I)):
    if T<I[i]:
        C+=1
        T = I[i] + L - 1
print(C,end='')


