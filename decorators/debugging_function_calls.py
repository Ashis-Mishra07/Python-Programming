


def debug(func):
    def wrapper(*args ,** kwargs):
        args_value=' ,'.join(str(a) for a in args) # join returns a iterable list
        key_value=' ,'.join( f"{k}={v}" for k , v in kwargs.items())
        print(f"Calling {func.__name__} with args {args_value} with args value {key_value}")
        return func(*args , **kwargs)
    return wrapper

@debug
def hello():
    print("Hello World")

@debug
def greet(name , greet="Hello"):
    print(f"{greet} , {name}")

greet("Ashis" , greet="Hi")


