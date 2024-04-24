from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def BFS(arr, x, y):
    n = len(arr)
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    count = 1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<N and 0<=ny<N and arr[nx][ny]==1):
                arr[nx][ny]=0
                queue.append((nx,ny))
                count=count+1
    return count
def DFS(x,y):
    global dfsCnt
    if(0<=x<N and 0<=y<N and arr[x][y]==1):
        dfsCnt=dfsCnt+1
        arr[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            DFS(nx,ny)
        return True
    return False
N=int(input())
arr= []
for i in range(N):
    arr.append(list(map(int,input())))
bfscnt=[]
dfsCnt=0

# for i in range(N):
#     for j in range(N):
#         if(arr[i][j]==1):
#             bfscnt.append(BFS(arr,i,j))
dfsCntArr=[]
for i in range(N):
    for j in range(N):
        if(DFS(i,j)==True):
            dfsCntArr.append(dfsCnt)
            dfsCnt=0
# bfscnt.sort()
# print(len(bfscnt))
# for i in bfscnt:
#     print(i)

dfsCntArr.sort()
print(len(dfsCntArr))
for i in dfsCntArr:
    print(i)

