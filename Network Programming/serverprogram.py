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
            message = self.c.recv(1024).decode()
            print("by Client: ", message)




s = socket.socket()
print("Socket successfully created")
port = 779
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)  # 5 incoming connections will be queued up
print("socket is listening")
while True:
    c, addr = s.accept()
    thread1 = ReadMessageThread(c,"One", 100)

    thread1.start()
    while True:
        print('Got connection from', addr, "\n Give your message\n")
        message = input()

        c.send(message.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break