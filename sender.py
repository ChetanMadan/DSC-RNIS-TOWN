
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