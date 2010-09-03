#!/usr/bin/env python3
#
# # -*- coding: UTF-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection
from urllib.parse import urlparse
import socket

class CaronteHandler(BaseHTTPRequestHandler):
    # def handle(self):
    #     print("Handle!")
    #     for i in dir(self):
    #         print("=>", i)
    #     print(dir(self.request))
    #     print(self.request.recv(10000))

    def do_CONNECT(self):
        print("Connect!")

    def do_GET(self):
        print("GET!")
        (scheme, netloc, path, params, query, fragment) \
            = urlparse(self.path)
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        soc.connect((netloc, 80))
        soc.send(self.raw_requestline)
        
        
            
        # client = HTTPConnection(netloc)
        # print("HTTPConnection to", netloc)
        # client.set_debuglevel(9999)
        # client.request('GET', path)
        print(self.headers.__str__())
        for i in self.headers.__str__().split('\n'):
            if ':' in i:
                (k, v) = i.split(':', 1)
                print(k, "maps to", v)
                soc.send("%s: %s\r\n" % (k, v));
        print(soc.recv(10000))
#         client.putheader(k, v)
        # # print(current_head)
        
        # print("Going to GET", path)
        
        # #client.endheaders()
        # print(client.getresponse())
        



class Caronte(HTTPServer):
    def test(self):
        print("Car")

if __name__ == '__main__':
    httpd = Caronte(('', 4321), CaronteHandler)
    httpd.serve_forever()
