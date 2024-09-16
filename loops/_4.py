str=input("Enter the string  ")

length=len(str)
str_rev=""

for ch in str:
    str_rev=ch+str_rev

print(str_rev)

# reverse a string using revcersed method 
str=input("Enter the string  ")
newStr="".join(reversed(str))
print(newStr)
