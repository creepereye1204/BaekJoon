import sys
input=sys.stdin.readline
_=input()
graph=list(input().split())
_=input()
print(''.join('1 ' if i in graph else '0 ' for i in input().split()))
