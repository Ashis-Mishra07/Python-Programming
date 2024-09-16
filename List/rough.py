list=["Ashis" , "Suraj" , "Amit"]
print(list)

# Iterate through index
print(list[0])
print(list[-1])

print(list[1:2])
print(list[:2])

# Assigning values
list[0]="Shaunak"
list[1:2]=["Shankiya"]
# Assigning multiple values
list[1:3]=["Asmit" , "Roop"]


# to add 
list[1:1]=["Rupesh"]

print(list)

# for looping
for name in list:
    print(name)

for name in list:
    print(name,end="-")


# if statement
if "Asmit" in list:
    print("Ashis is present")

# appending ele at the end
list.append("Ashis")

# deleting last ele
list.pop()

# removing custom ele
list.remove("Shaunak")

# insert an ele
list.insert(1 , "Bibhas")

list2=list # here the pointer or list2 and list will point to the same refernece
list3=list.copy() # here it will point to different reference

squared_num=[x**2 for x in range(5)]  # 0 1 2 3 4
print(squared_num)




