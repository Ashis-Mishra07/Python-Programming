def sum_all(*args):  # variable name can be anything but use *
    return sum(args)

print(sum_all(1 ,2))
print(sum_all(1 ,2 ,3))
print(sum_all(1 ,2 ,3 ,4))

def sum_all(*args):  # variable name can be anything but use *
    print(args)  # this will actually return in the orm of tuples
                 # since tuples are iterable , so we can perform operations on it
    for i in args:
        print(i)

sum_all(1,2)

