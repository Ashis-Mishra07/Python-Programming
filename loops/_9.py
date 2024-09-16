import time

max_attempts=5
wait_time=1
attempts=0

while attempts < max_attempts :
    print("Attempt" , attempts+1 , "- wait time" , wait_time)
    time.sleep(wait_time)
    wait_time = wait_time*2
    attempts = attempts + 1