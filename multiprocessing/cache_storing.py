import time
import multiprocessing

store=[]
def calc_square(arr):
    global store
    for i in arr:
        time.sleep(0.3)
        print("sqaure of " , i , " is " , i*i)
        store.append(i*i)

    print("within process " + str(store))

arr=[1,2,3,4,5]

if __name__ == "__main__":
    p1=multiprocessing.Process(target=calc_square , args=(arr ,))
    p1.start()
    p1.join()

    print("result" + str(store))
    print("Done")

    # shockingly the result will print the squares but the store array is empty
    # this is because everytime the process will make a new array 
    
    # every time the process is called it will create its new copy of the array , every process has its own address space(virtual memory)
    # thus program variable are not shared between the proceses .
    # within process will keep the values but after the process done it will not keep it .
    # you need to use interprocess communication(IPC) techniques to share the data among it 


