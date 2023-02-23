import sys
input = sys.stdin.readline
M = [int(input()) for _ in range(int(input()))]
M.sort(reverse=True)
target=0
for i in range(len(M)):
    if M[i]-i>0:
        target+=M[i]-i
    else:
        break
print(target)