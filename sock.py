

import socket
import sys

from _thread import *
HOST = '127.0.0.1'
PORT =8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((HOST, PORT))

except socket.error as msg:
    print(msg)
    sys.exit()

print("bind complete")

s.listen(5)

print("socket listening")

def client_thread(conn):
    print('client thread started')
    #conn.send(bytes(input("enter input : "), 'UTF-8'))
    while True:
        data = conn.recv(4096)
        data=data.decode()
        reply = "data recd : "+ data
        if not data or data=='disconnect':
            break
        print(reply)
        #conn.sendall(bytes(reply, 'UTF-8'))

    conn.close()
    print("connection closed")


while True:
    conn, addr = s.accept()
    print('connected to ', addr[0], " ", addr[1]) 
    try:
        start_new_thread(client_thread(conn,))
    except TypeError:
        pass
s.close()      