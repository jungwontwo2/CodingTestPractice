import sys
N=int(input())
arr=[]
for i in range(N):
    a=sys.stdin.readline().split()
    if a[0]=='1':
      arr.append(a[1])
    elif a[0]=='2':
        if(len(arr)==0):
            print(-1)
        else:
            print(arr.pop())
    elif a[0]=='3':
        print(len(arr))
    elif a[0]=='4':
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='5':
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
