from collections import deque
N,M,V=map(int,input().split())
print(N,M,V)
arr=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    arr[x][y]=1
    arr[y][x]=1
for i in arr:
    print(i)
visitedDFS=[0]*(N+1)
visitedBFS=[0]*(N+1)
def dfs(start:int):
    visitedDFS[start]=1
    print(start,end=" ")
    for i in range(1,N+1):
        if(visitedDFS[i]==0 and arr[start][i]==1):
            dfs(i)
def bfs(start:int):
    q=deque([start])
    visitedBFS[start]=1
    while q:
        start=q.popleft()
        print(start)
        for i in range(1,N+1):
            if(visitedBFS[i]==0 and arr[start][i]==1):
                q.append(i)
                visitedBFS[i]=1

dfs(V)
bfs(V)