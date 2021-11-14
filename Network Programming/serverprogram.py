import socket
import threading
from time import sleep


class ReadMessageThread(threading.Thread):
    name=""
    def __init__(self,c1,c2, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.c1=c1
        self.c2 = c2
        name=thread_name

        # helper function to execute the threads

    def run(self):
        while True:

            message = self.c1.recv(1024).decode()
            print("by Client: ", message)
            c1.send(message.encode())
            c2.send(message.encode())



s = socket.socket()
print("Socket successfully created")
port = 777
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)  # 5 incoming connections will be queued up
print("socket is listening")
while True:
    c1, addr = s.accept()
    c2,addr=s.accept()
    thread1 = ReadMessageThread(c1,c2,"One", 100)
    thread2 = ReadMessageThread(c2, c1, "two", 101)



    #thread2=SendMessageThread(c1,"two",101)
    thread1.start()
    thread2.start()

    # Close the connection with the client
    #c.close()

    # Breaking once connection closed
    #break