"""
import socket
import time


def client_program():
    host = '127.0.0.1'  # as both code is running on same pc
    port = 8888  # socket server port number

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    s.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message[0].lower().strip() != 'bye':
        mess = [message, time.time()]
        s.send(bytes(str(mess), 'UTF-8'))
        #s.sendall(message.encode())  # send message
        #data = client_socket.recv(1024).decode()  # receive response

        #print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
        
        print("sent : ", bytes(message, 'UTF-8'))
    s.close()  # close the connection


if __name__ == '__main__':
    client_program()

"""
import socket
import time
import pickle
ret = False
def conn_ini():
    host = '127.0.0.1'  # as both code is running on same pc
    port = 9000  # socket server port number
    ret = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    s.connect((host, port))  # connect to the server
    return s
def send(message):
    if not ret:
        sender = conn_ini()

    mess = [message, time.time()]
    sender.send(pickle.dumps(mess))
    #s.sendall(message.encode())  # send message
    #data = client_socket.recv(1024).decode()  # receive response

    #print('Received from server: ' + data)  # show in terminal    
    #print("sent : ", bytes(message, 'UTF-8'))
    return sender

if __name__ == '__main__':

    re = send(input())
    re.close()