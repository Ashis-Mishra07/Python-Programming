import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end-start}")
        return result
    return wrapper  # this will return  to the sleep_n_seconds function

@timer   # this decorator will call the timer function and pass the function sleep_n_sec it timer function
def sleep_n_seconds(n):
    time.sleep(n)
    return n

sleep_n_seconds(5)