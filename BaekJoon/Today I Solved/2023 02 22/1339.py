alphabet=[input() for i in range(int(input()))]
alphabet_value={}
priority=[]
a=11

for i in alphabet:
    for j in range(len(i)):
        if alphabet_value.get(i[j])==None:
            alphabet_value[i[j]]=0
        alphabet_value[i[j]]+=10**(len(i)-j+1)
alphabet_value=sorted(alphabet_value.items(),key=lambda x:-x[1])

n=9
encode={}
for i in alphabet_value:
    encode[i[0]]=str(n)
    n-=1
result=0
for i in range(len(alphabet)):
    char=''
    for j in range(len(alphabet[i])):
         char+=encode[alphabet[i][j]]
    result+=int(char)
print(result,end='')











