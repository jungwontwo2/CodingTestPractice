import sys
input=sys.stdin.readline
N,M=map(int,input().split())
hearArr=[]
seeArr=[]
for i in range(N):
    hearArr.append(input())
for i in range(M):
    seeArr.append(input())
answer=list(set(hearArr)&set(seeArr))
answer.sort()
print(len(answer))
for i in answer:
    print(i,end='')