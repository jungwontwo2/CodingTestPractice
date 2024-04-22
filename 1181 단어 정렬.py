N=int(input())
arr=[]
for i in range(N):
    word=input()
    if(word not in arr):
        arr.append(word)
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)