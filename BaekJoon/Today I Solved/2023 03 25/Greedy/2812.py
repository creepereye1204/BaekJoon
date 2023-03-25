import sys
input=sys.stdin.readline
n,m=map(int,input().split())
count=m
q=input().strip()
result=[]
for i in q:
    while result and result[-1]<i and m:
        result.pop()
        m-=1
    result.append(i)
print(''.join(result[:n-m]))