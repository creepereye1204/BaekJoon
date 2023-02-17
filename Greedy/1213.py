N = sorted(input())
M={}
for alpha in N:
    M.setdefault(alpha,0)
    M[alpha]+=1
ans,center='',''
for alphabet,amount in M.items():
    if amount%2:
        if center!='':
            print("I'm Sorry Hansoo")
            break
        center = alphabet
    ans+=alphabet*(amount//2)
else:
    print(ans+center+ans[::-1])