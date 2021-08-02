# from threading import *
# def my_msgprint():
#     print("The above line is executed by: ", current_thread().getName())

# print("Main Thread creating child object")
# mthread = Thread(target = my_msgprint) # L1
# print("Main Thread starting child thread") 
# mthread.start()# L2

# We can change the name of the child thread 
# from threading import *
# def my_msgprint():
#     print("The above line is executed by: ", current_thread().getName())

# print("Main Thread creating child object")
# mthread = Thread(target = my_msgprint, name = 'MyChildThread')
# print("Main Thread starting child thread")
# mthread.start()

# We have multiple threads in our program. 
# Then the execution order cannot be expected and hence we cannot predict the exact output 
# for multithreaded programs. It is varied from machine to machine and execution run 
# as shown in the below example.

from threading import *
def my_msgprint(i):
    for loop in range(1,i):
        print(f"{current_thread().getName()} thread running count is {loop}")

mthread = Thread(target = my_msgprint, name = 'MyChildThread', args = (5,))
mthread.start()

for i in range(1,5):
    print(f"Main thread running count is {i}")

