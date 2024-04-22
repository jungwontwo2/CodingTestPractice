# https://www.acmicpc.net/problem/1018
arr=[]
cntArr=[]
N,M=map(int,input().split())
for i in range(N):
    arr.append(list(input()))
# print(arr)
for i in range(N-7):
    for j in range(M-7):
        wCnt=0
        bCnt=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if((a+b)%2==0):
                    if(arr[a][b]=='W'):
                        bCnt=bCnt+1
                    else:
                        wCnt=wCnt+1
                else:
                    if(arr[a][b]=='W'):
                        wCnt=wCnt+1
                    else:
                        bCnt=bCnt+1
        cntArr.append(min(wCnt,bCnt))
print(min(cntArr))