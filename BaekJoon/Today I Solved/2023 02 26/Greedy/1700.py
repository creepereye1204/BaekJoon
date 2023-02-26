N,_=map(int,input().split())
L=list(input().split())
slot=[]
cnt=0
while len(L)>0:
    V=L[0]
    del L[0]
    if len(slot)<N and V not in slot:
        slot.append(V)
    else:
        if V not in slot:
            cnt+=1
            stack=[]
            for i in L:
                if i in slot and i not in stack:
                    stack.append(i)
            if len(slot)!=len(stack):
                for s in range(len(slot)):
                    if slot[s] not in stack:
                        slot[s]=V
                        break
            else:
                for i in range(len(slot)):
                    if slot[i]==stack[-1]:
                        slot[i]=V
                        break
print(cnt)