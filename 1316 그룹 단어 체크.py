N=int(input())
cnt=0
for i in range(N):
    word=input()
    arr=[]
    switch=True
    for j in range(len(word)):
        if(word[j] not in arr or arr[-1]==word[j]):
            arr.append(word[j])
        else:
            switch=False
    if(switch):
        cnt=cnt+1
print(cnt)