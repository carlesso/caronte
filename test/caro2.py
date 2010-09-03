#!/usr/bin/env python3

from http.server import *
import socket
import urllib.parse
__version__ = "0.0.1"


class CaronteHandler(BaseHTTPRequestHandler):
    
    server_version = "Caronte/"+__version__

    def handle(self):
        (ip, port) = self.client_address
        print("Ip =>", ip, " :: Port", port)
        print(self.handle_one_request())

    def do_CONNECT(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.path)
        try:
            if self._connect_to(self.path, soc):
                print("YESSS")
                self.wfile.write(self.protocol_version + "200 Connection established\r\n")
                self.wfile.write("Proxy-agent: " + self.version_string() + "\r\n")
                self.wfile.write("\r\n")
                self._read_write(soc, 300)
        finally:
            print("\tbye")
            soc.close()
            self.connection.close()

    def _connect_to(self, netloc, soc):
        print("NET", netloc)
        i = netloc.find(':')
        if i >= 0:
            host_port = netloc[:i], int(netloc[i+1:])
        else:
            host_port = netloc, 80
            
        print("\t connect to", host_port)
        try:
            soc.connect(host_port)
        except arg:
            try:
                msg = arg[1]
            except:
                msg = arg
            self.send_error(404, msg)
            return 0
        return 1


    def do_GET(self):
        print ("GETTTT!")
        print(self.path)
        (scm, netloc, path, params, query, fragment) = urllib.parse.urlparse(self.path, 'http')
        print("NNONON =>", netloc)
        self.path = netloc
        self.do_CONNECT()
        #self.send_error(301)

class Caronte(HTTPServer):
    def test(self):
        print("TEST")

def run(server_class=Caronte, handler_class=CaronteHandler):
    server_address = ('', 4321)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    #running = Caronte()
    run()

