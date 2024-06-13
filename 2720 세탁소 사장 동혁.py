a=int(input())
for i in range(a):
    b=int(input())
    for j in [25,10,5,1]:
        print(b//j,end=' ')
        b=b%j
    print()