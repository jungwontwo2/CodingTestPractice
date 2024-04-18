num=int(input())
for i in range(num):
    time,message = input().split()
    time=int(time)
    for j in range(len(message)):
        for k in range(time):
            print(message[j],end="")
    print()