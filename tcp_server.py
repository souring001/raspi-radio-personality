import asyncore
import socket
from threading import Thread
import time

class ServerUDP(asyncore.dispatcher):

    data = ""

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind((host, port))
        self.listen(1)
        print("Server listening on port "+str(port))

    def handle_accept(self):
        socket, address = self.accept()
        print('Connected by', address)
        EchoHandler(socket)

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        raw_data = self.recv(1024)
        data = str(raw_data.decode())

        if data == 'quit()':
            print("Closing TCP Server...")
            self.out_buffer = "Closing UDP Server".encode()+raw_data
            self.close()
            print("Server closed")
            exit(0)
        elif len(data)>0:
            print("Client << "+data)
            self.out_buffer = "Server >> ".encode()+raw_data #input("intorduzca algo para enviar: ").encode()

class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        print("Starting TCP Server service...")

    def run(self):
        s = ServerUDP('', 51452)
        print("Running TCP Server")
        asyncore.loop()

# s = Server()
# s.start()
