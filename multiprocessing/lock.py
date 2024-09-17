# when the two process try to use a single resource at a time 
# in order to stop the ambiguity we use lock

# example is transaction in bank account


import time
import multiprocessing



# def deposit(balance):
#     for i in range(100):
#         time.sleep(0.1)
#         balance.value=balance.value+1

# def withdraw(balance):
#     for i in range(100):
#         time.sleep(0.1)
#         balance.value=balance.value-1


# if __name__ == "__main__":
#     balance=multiprocessing.Value('i',200)
#     d=multiprocessing.Process(target=deposit , args=(balance,))
#     w=multiprocessing.Process(target=withdraw , args=(balance,))

#     d.start()
#     w.start()

#     d.join()
#     w.join()

#     print("Final balance is " , balance.value)






# output will not be equal to 200 since in deposit we are adding 1 but until the value get fixed to the balance. value , the 
# withdraw process will start and it will decrease the value of balance. value
# so this results is not having any lock and proper value of the balance. value

# instead of using value we can use lock to get the proper value of the balance. value



def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.1)
        # the below section is the critical section
        lock.acquire()
        balance.value=balance.value+1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value=balance.value-1
        lock.release()

if __name__ == "__main__":
    balance=multiprocessing.Value('i',200)
    lock=multiprocessing.Lock()
    d=multiprocessing.Process(target=deposit , args=(balance,lock))
    w=multiprocessing.Process(target=withdraw , args=(balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print("Final balance is " , balance.value)
