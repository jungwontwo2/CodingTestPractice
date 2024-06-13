a=int(input())
arr1=list(map(int,input().split()))
b=int(input())
arr2=list(map(int,input().split()))
dict={}
for i in range(len(arr1)):
    dict[arr1[i]]=0
for i in arr2:
    if(i in dict):
        print(1, end=" ")
    else:
        print(0, end=" ")