# to make any functional scope as global varible

x=67
def func():
    global x
    x=12

func()
print(x)


def f1():
    x=88
    def f2():
        print(x)  # this is called closure property / back thoery
    return f2

myRes=f1()
myRes()

def chaiCoder(num):
    def actual(x):
        return x** num
    return actual

square=chaiCoder(2)
print(square(2))

cube=chaiCoder(3)
print(cube(2))


