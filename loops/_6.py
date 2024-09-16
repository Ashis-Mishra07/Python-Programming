num=input("enter number  ")
num=int(num)

# res=1
# for i in range(1 , num+1):
#     res=res*i

# print(res)


res=1
count=1

while count<=num:
    res=res*count
    count+=1

print(res)