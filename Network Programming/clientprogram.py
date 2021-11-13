import socket
import threading
from time import sleep


class ReadMessageThread(threading.Thread):
    def __init__(self,c, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.c=c

        # helper function to execute the threads

    def run(self):
        while True:
            print("by Server: ",s.recv(1024).decode())

s = socket.socket()

port = 779

c=s.connect(('127.0.0.1', port))
while True:
    thread1 = ReadMessageThread(c, "One", 100)

    thread1.start()
    message=input()
    s.send(message.encode())
s.close()