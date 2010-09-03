#!/usr/bin/env python3
import threading
import socket
from lib.utils import get_url_request
import urllib.parse as parse

class Caronte:

    def __init__(self):
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.listen_socket.allow_reuse_address = True
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind((socket.gethostname(), 4321))

        try:
            self.listen_socket.listen(5)
        except:
            print("Broken")

    def start(self):
        while 1:
            (self.connection, b) = self.listen_socket.accept()
            self.con = self.connection.recv(10)
            content = str(self.con, 'ISO-8859-1')
            while not self.check_content(content):
                print("+1")
                # XXX 10 for testing purpose.
                self.con += self.connection.recv(10)
                content = str(self.con, 'ISO-8859-1')
            print("Header!")
            print(content)
            #print(parse.urlparse(content))
            url = get_url_request(content)
            print("Looking for:", url)

            self.retrive(url)
            

    def __del__(self):
        print("\nExiting Caronte...")
        self.listen_socket.shutdown(socket.SHUT_RDWR)
        self.listen_socket.close()
        del(self.listen_socket)
        
    def retrive(self, url):
        ret_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #ret_sock.setblocking(0)
        ret_sock.connect((url.netloc, 80))
        ret_sock.send(self.con)
        data = self.connection.recv(100)
        while data:
            print("+psi")
            ret_sock.send(data)
            data = self.connection.recv(2**10)
            print("DATA ==>>", data, "<<--")
            # if '\r\n\r\n' in str(data, 'ISO-8859-1'):
            #     ret_sock.send(data)
            #     break
        print("FINE 1")
        ret = ret_sock.recv(100)
        while ret:
            print("+xi")
            self.connection.send(ret)
            ret = ret_sock.recv(100)
            print(ret_sock)
        self.connection.close()

        
    def check_content(self, content):
        if '\r\n' in content:
            return True
        else:
            return False


car = Caronte()
try:
    car.start()
except KeyboardInterrupt:
    del(car)
