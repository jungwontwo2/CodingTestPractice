arr=['ABC','DEC','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a=input()
result=0
for i in range(len(a)):
    for j in arr:
        if(a[i] in j):
            result+=arr.index(j)+3
print(result)