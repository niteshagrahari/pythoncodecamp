import threading
from time import sleep


class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # helper function to execute the threads

    def run(self):
        for i in range(1, 10):
            print(str(self.thread_name), i)
            sleep(1)


thread1 = thread("One", 100)
thread2 = thread("Two", 100);

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Exit")
