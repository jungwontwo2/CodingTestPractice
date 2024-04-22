ComputerCnt=int(input())
NetworkCnt=int(input())
dfsArr=[0 for i in range(ComputerCnt+1)]
bfsArr=[0 for i in range(ComputerCnt+1)]
arr=[[0]*(ComputerCnt+1) for i in range(ComputerCnt+1)]
for i in range(1,NetworkCnt+1):
    x,y=map(int,input().split())
    arr[x][y]=1
    arr[y][x]=1
dfsCnt=0
bfsCnt=0
def dfs(x:int):
    global dfsCnt
    dfsArr[x]=1
    for i in range(len(arr[x])):
        if(arr[x][i]==1 and dfsArr[i]!=1):
            dfsCnt=dfsCnt+1
            dfs(i)
dfs(1)
print(dfsCnt)