# about multithreading
# 1. multithreading is a way to run multiple threads concurrently
# 2. each thread runs in a separate memory space
# 3. each thread has its own stack, heap, and code segment
# 4. threads share the process's memory space
# 5. threads are lightweight compared to processes
# 6. threads are used for I/O-bound tasks
# 7. threads are used for tasks that are not CPU-bound

# multithreading in python
# for example there is a list of numbers and i have to calculate the sqaure and cube of the numbers present in the list at the same time 

import time


def calc_square(arr):
    for i in arr:
        time.sleep(1)
        print("square is", i*i)

def calc_cube(arr):
    for i in arr:
        time.sleep(1)
        print("cube is", i*i*i)

arr=[1,2,3,4,5,6]

t=time.time()

calc_square(arr)
calc_cube(arr)


print("done in" , time.time()-t)

# when time.sleep() hits ur cpu does nothing
# suppose ur cpu is waiting for some response in the sockets and meanwhile in the time  between it will not wait rather it will do some other work

# by multithreading

import threading

t3=time.time()

t1=threading.Thread(target=calc_square, args=(arr,))
t2=threading.Thread(target=calc_cube, args=(arr,))

t1.start() # this will spawn a new thread with the main function and start the process
t2.start()

# join simply means the working of indivisaul threads is over and now it will jump to the excution of main program 
t1.join() # join is used to wait for the t1 is completed
t2.join()

print("done in" , time.time()-t3)


# the process above will simultaneously process the two threads and do the work parallely
