# some something in this file anything random
age = 54
name = "John"
print(name, age)
# add a loop
for i in range(10):
    print(i)
# add a function
def add(a, b):
    return a + b
print(add(2, 3))


# opeartions start to fectch the file 

f=open('file.py')
f.readline()  # this will read every single next line and return '' (empty)  if not found anything 
f.__next__()  # this will exactly the same thing as nextLine but show error if not found

for line in open('file.py'):
    print(line)
# the above will print all the lines and since for is a iterator so it will stop if not found anything 

while True:
    line =f.readline()
    if not line:
        break
    print(line)


mylist=[1,2,3,4,5]
I = iter(mylist) 
I.__next__() # this will check if the next iterator present or not and return its value

# anything that is iterable 
R=range(0,5)
I=iter(R)
# the below two methods can be used 
I.__next__()
next(I)

