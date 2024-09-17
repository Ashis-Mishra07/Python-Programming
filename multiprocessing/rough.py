import time
import multiprocessing

def calc_square(arr):
    for i in arr:
        time.sleep(0.3)
        print("sqaure of " , i , " is " , i*i)

def calc_cube(arr):
    for i in arr:
        time.sleep(0.3)
        print("cube of " , i , " is " , i*i*i)

arr=[1,2,3,4,5]

if __name__ == "__main__":
    p1=multiprocessing.Process(target=calc_square , args=(arr ,))
    p2=multiprocessing.Process(target=calc_cube , args=(arr ,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print("Done")

    # now abou the difference between multiprocessing and threading that if u open task manager the main task
    # and the two child tasks will be running as different processes  but in mutlithreading they will be running as
    # different threads but single process .

    # 3 diff python exe files u will see while doing it , while in threading only one python exe file will be there
