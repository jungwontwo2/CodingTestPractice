from collections import deque
N,M,V=map(int,input().split())
arr=[[0]*(N+1) for i in range(N+1)]
dfsCheck=[0 for i in range(N+1)]
bfsCheck=[0 for i in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    arr[x][y]=1
    arr[y][x]=1
def dfs(start:int):
    print(start, end=" ")
    dfsCheck[start]=1
    for i in range(len(arr[start])):
        if(arr[start][i]==1 and dfsCheck[i]!=1):
            dfs(i)
def bfs(start:int):
    queue=deque([start])
    bfsCheck[start]=1
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in range(1,N+1):
            if(bfsCheck[i]!=1 and arr[start][i]==1):
                queue.append(i)
                bfsCheck[i]=1

dfs(V)
print()
bfs(V)