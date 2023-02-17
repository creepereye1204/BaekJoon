import sys
input=sys.stdin.readline
def calculator(n,m,c):
    while m>=n:

        if m==n:
            print(c)
            return None
        if m%10==1:
            m//=10
        elif m%2==0:
            m//=2
        else:
            print(-1)
            return None
        c += 1
    print(-1)
if __name__=="__main__":
    c=1
    n,m=map(int,input().split())
    calculator(n,m,c)
