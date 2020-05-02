import threading
import time

def print_time(i):
    time.sleep(5)
    print(i)

def looper(loops):
    for i in range(loops):
        t = threading.Thread(target=print_time, args=(i,))
        t.start()
# if __name__ == "__main__":
        
# for i in range(10):
#     t1 = threading.Thread(target=print_time, args=(i,))
#     t1.start()
# print("Done Looping")


'''
my_func, args=(i,)

my_func(i)
'''