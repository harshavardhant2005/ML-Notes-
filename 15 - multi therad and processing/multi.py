import multiprocessing
import multiprocessing.process
import time 
def print_num():
    for i in range(5):
        time.sleep(1.5)
        print(i**2)
def print_cube():
    for i in range(5):
        time.sleep(1)
        print(i**3)

if __name__ =="__main__":
    p1 = multiprocessing.Process(target =print_num)
    p2 = multiprocessing.Process(target =print_cube)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
