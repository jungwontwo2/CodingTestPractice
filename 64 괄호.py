T=int(input())
for i in range(T):
    a=list(input())
    arr=[]
    switch = True
    while len(a)>0:
        if(a[0]=='('):
            arr.append(a.pop(0))
        elif(a[0]==')' and len(arr)>0):
            a.pop(0)
            arr.pop(0)
        else:
            switch=False
            break
    if(len(arr)==0 and switch==True):
        print("YES")
    else:
        print("NO")