from collections import deque
N,K=map(int,input().split())
def bfs():
    q=deque()
    q.append(N)
    while q:
        loc=q.popleft()
        if loc==K:
            print(visited[loc])
            return
        for i in (loc-1,loc+1,2*loc):
            if 0<=i<Max and not visited[i]:
                q.append(i)
                visited[i]=visited[loc]+1
Max = 10 ** 5 + 1
visited = [0] * Max
bfs()
