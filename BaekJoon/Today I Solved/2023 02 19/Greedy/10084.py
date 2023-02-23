import sys
S=sys.stdin.readline().strip()
T=sys.stdin.readline().strip()
len_s={'A':0,'B':0}
len_t={'A':0,'B':0}
for i in S:
    len_s[i]+=1
for i in T:
    len_t[i]+=1
C=len_t['A']-len_s['A']+len_t['B']-len_s['B']
for _ in range(C):
    if T[-1]=='A':
        T=T[:-1]
    else:

       if T[-1]=='B':
           T=T[:-1]
           T=T[::-1]
       else:
           print(0)
           break
else:
    if T==S:
        print(1)
    else:
        print(0)