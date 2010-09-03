#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 4321))

try:
    s.listen(5)
    while True:
        (a, b) = s.accept()
        print(a.recv(1000))
except KeyboardInterrupt:
    print("Closing")
    s.shutdown(socket.SHUT_RDWR)
    s.close()
