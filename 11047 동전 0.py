N,K=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
cnt=0
for i in range(len(arr)-1,-1,-1):
    cnt = cnt + K//arr[i]
    K=K%arr[i]
print(cnt)