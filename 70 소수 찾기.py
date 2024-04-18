result=0
N = int(input())
a=list(map(int,input().split()))
for i in a:
    cnt = 0
    for j in range(2,i+1):
        if(i%j==0):
            cnt=cnt+1
    if(cnt==1):
        result=result+1
print(result)