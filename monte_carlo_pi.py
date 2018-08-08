import sys
import threading
import math
import random

#global lock for the threads
thread_lock = threading.Lock()
within_radius = 0
total_hits = 0
class threads(threading.Thread):
    def __init__(self, threadID, name, Counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.Counter = Counter

    def run(self):
        global thread_lock
        global within_radius
        global total_hits
        thread_lock.acquire()
        in_radius = point_in_square()
        if(in_radius == True):
            within_radius += 1
            total_hits += 1
        else:
            total_hits += 1
        thread_lock.release()

def point_in_square():
    x = random.uniform(0, .5)
    y = random.uniform(0, .5)
    if(math.sqrt(x*x+y*y) <= .5):
        return True
    return False
    
    

def main():
    # increase these two vars to decrease error
    first_range = 200
    second_range = 200
    
    for j in range(0, first_range):
        threads_arr = []
        for i in range(1, second_range):
            threads_arr.append(threads(i, "thread"+str(i), i))
        for t in threads_arr:
            t.start()
        for t in threads_arr:
            t.join()
    pi = 4.0 * float(within_radius)/total_hits
    print pi
    return pi
if __name__ == "__main__":
    main()

 
