# 이전코드 시간초과
# n=int(input())
# a=list(map(int,input().split()))
#
# aa=sorted(set(a))
# for i in a:
#     print(aa.index(i), end=' ')

n = int(input())
a=list(map(int,input().split()))
aa=sorted(set(a))
dic={}
for i in range(len(aa)):
    dic[aa[i]] = i
for i in a:
    print(dic[i], end=' ')