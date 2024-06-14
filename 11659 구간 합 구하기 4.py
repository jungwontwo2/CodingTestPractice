import sys
input = sys.stdin.readline
a,b=map(int,input().split())
arr=list(map(int,input().split()))

prefix_sum = [0] * (a + 1)
for i in range(1, a + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
for _ in range(b):
    x, y = map(int, input().split())
    result = prefix_sum[y] - prefix_sum[x - 1]
    print(result)