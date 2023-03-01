import time
n=[0]*51
def fibo(x):
    if n[x]==0:
        if x==1 or x==2:
            return 1
        n[x]=fibo(x-1)+fibo(x-2)
    return n[x]
start=time.time()
print(time.time()-start,':초 값',fibo(35))

