while(True):
    a=int(input())
    if(a==-1):
        break
    arr = []
    for i in range(1,a):
        if(a%i==0):
            arr.append(i)
    if(sum(arr)==a):
        print(a,end=" = ")
        for i in range(len(arr)-1):
            print(arr[i],end=" + ")
        print(arr[-1])
    else:
        print(f"{a} is NOT perfect.")