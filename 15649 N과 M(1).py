def dfs():
    if len(arr) == b:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, a+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        dfs()
        arr.pop()
        visited[i] = False


a,b=map(int,input().split())
arr=[]
visited=[False]*(a+1)

dfs()