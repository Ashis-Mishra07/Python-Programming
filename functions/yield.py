def evenGenerator(num):
    for i in range(2,num+1,2):
        yield i


for i in evenGenerator(10):
    print(i)

# yield is more of a like retunr but the difference is that it returns a generator object
# which can be used to iterate over the values , it will return is the condition match and 
# the function will not be terminated , it will wait for the next call to the function
# and then it will continue from where it left off