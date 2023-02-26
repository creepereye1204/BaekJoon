import sys
input=sys.stdin.readline
R,C=map(int,input().split())
L=[list(input()) for _ in range(R)]
result=0
def cal(x,y):
    if x==C-1:
        return True
    for dy in [-1,0,1]:
        ay=y+dy
        ax=x+1
        if 0<=ay and ay<R and 0<=ax and ax<C:
            if  L[ay][ax]=='.':

                L[ay][ax]='x'
                if cal(ax,ay):
                    return True
    return False

for y in range(R):
    if cal(0,y): result+=1
print(result)

