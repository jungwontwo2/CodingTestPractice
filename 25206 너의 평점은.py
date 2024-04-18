# sum=0.0
# hakjumSum=0
# for i in range(20):
#     name,hakjum,grade=input().split()
#     hakjum=float(hakjum)
#     hakjumSum=hakjumSum+hakjum
#     if(grade=='A+'):
#         sum=sum+hakjum*4.5
#     elif(grade=='A0'):
#         sum=sum+hakjum*4.0
#     elif(grade=='B+'):
#         sum=sum+hakjum*3.5
#     elif(grade=='B0'):
#         sum=sum+hakjum*3.0
#     elif(grade=='C+'):
#         sum=sum+hakjum*2.5
#     elif(grade=='C0'):
#         sum=sum+hakjum*2.0
#     elif(grade=='D+'):
#         sum=sum+hakjum*1.5
#     elif(grade=='D0'):
#         sum=sum+hakjum*1.0
#     elif(grade=='F'):
#         sum=sum
#     else:
#         sum=sum
#         hakjumSum=hakjumSum-hakjum
# print(round((sum/hakjumSum),6))
sum=0.0
hakjumSum=0
grade_dict = {'A+':4.5,
              'A0':4.0,
             'B+':3.5,
             'B0':3.0,
             'C+':2.5,
             'C0':2.0,
             'D+':1.5,
             'D0':1.0,
              'F':0}
for i in range(20):
    name,hakjum,grade=input().split()
    hakjum=float(hakjum)
    if(grade!='P'):
        hakjumSum=hakjumSum+hakjum
        sum=sum+hakjum*grade_dict[grade]
print(round((sum/hakjumSum),6))