# from threading import *
# class Mychildthread(Thread):
#     pass
# myt1 = Mychildthread()
# print(myt1.name)


from threading import *
class MyChildClass(Thread): 
    def run(self): 
        for i in range(1,9):
            print(f'{current_thread().getName()} is executing at count of {i}')
myt1=MyChildClass()
myt1.start()
myt1.join()
for i in range(1,9):
    print(f'{current_thread().getName()} is executing at count of {i}')
