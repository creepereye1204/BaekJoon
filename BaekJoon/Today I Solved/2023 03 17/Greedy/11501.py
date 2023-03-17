import sys
input=sys.stdin.readline
def predict(stocks):
    mx=stocks[-1]
    result=0
    for i in range(len(stocks)-1,-1,-1):
        if mx<=stocks[i]:
            mx=stocks[i]
        else:
            result+=mx-stocks[i]
    return result
for _ in range(int(input())):
    input()
    stocks=list(map(int,input().split()))
    print(predict(stocks))