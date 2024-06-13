a=int(input())
b=list(map(int,input().split()))
result=0
b.sort()
for i in range(a):
    for j in range(i+1):
        result+=b[j]
print(result)