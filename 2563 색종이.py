arr=[[0]*100 for i in range(100)]
N=int(input())
for i in range(N):
    x,y=map(int,input().split())
    for j in range(10):
        for k in range(10):
            arr[x+j][y+k]=1
count=0
for i in arr:
    count = count+i.count(1)
print(count)