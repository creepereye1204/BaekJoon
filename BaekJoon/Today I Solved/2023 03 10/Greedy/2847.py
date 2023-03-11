N=int(input())
a=[int(input()) for _ in range(N)]
cnt=0
for i in range(len(a)-1,0,-1):
    if a[i-1]<a[i]:
        continue
    while a[i-1]>=a[i]:
        a[i-1]-=1
        cnt+=1
print(cnt)