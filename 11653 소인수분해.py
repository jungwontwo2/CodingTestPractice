a=int(input())
if(a==1):
    print('')
else:
    for i in range(2,a+1):
        while(a%i==0):
            print(i)
            a=a/i