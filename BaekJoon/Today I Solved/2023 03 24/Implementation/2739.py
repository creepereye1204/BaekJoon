N,K=map(int,input().split())
NUMBER=input()
choice=[True]*len(NUMBER)
for i in range(len(NUMBER)-1):
    if K==0:
        print('s')
        break
    if int(NUMBER[i])<int(NUMBER[i+1]):
        choice[i]=False
        K-=1
print(choice)

