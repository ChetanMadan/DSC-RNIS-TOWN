import socket
import sys
import time
from _thread import start_new_thread
import pickle
import cv2
recd=b""

def find_fps(t):
    return(time.time()-t)

def client_thread(conn):
    print('client thread started')
    #conn.send(bytes(input("enter input : "), 'UTF-8'))
    while True:
        data=b""
        while True:
            packet = conn.recv(4096)
            if not packet: break
            data+=packet
        if not data: break
        recd=pickle.loads(data)
        print("DATA PRINTED !!!")
        print(" ")
        print(recd[0])
        print("DATE")
        print(recd[1])

        cv2.imshow("frame transmitted!", recd[0])
        if cv2.waitKey(1)==ord('q'):
            cv2.destroyAllWindows()

        #conn.sendall(bytes(reply, 'UTF-8'))
    print("connection closed")
    conn.close()

    return recd


def main():

    HOST = '10.10.1.202'
    PORT =9000

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



    while True:
        conn, addr = s.accept()
        print('connected to ', addr[0], " ", addr[1])
        try:
            msg = start_new_thread(client_thread(conn,))
            cv2.imshow("transmitted!", recd[0])
            if cv2.waitKey(0)==ord('q'):
                cv2.destroyAllWindows()
                break
            print(msg)

        except TypeError:
            pass
    s.close()

if __name__=='__main__':
    main()
