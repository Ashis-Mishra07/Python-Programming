num=input("Enter a number ")
num=int(num)

for i in range(2,num):
    if(num%i==0):
        print("Not prime")
        exit()

print("Prime")


