def factorial(a: int):
    num = 1
    for i in range(1, a+1):
        num *= i
    return num
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    print(factorial(M)//(factorial(N)*factorial(M-N)))
