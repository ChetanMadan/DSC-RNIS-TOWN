from sender import send
import cv2

def main():

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        a = send(frame)

        if cv2.waitKey(5)==ord('q'):
            break
    a.close()
    
"""
    cv2.imshow('frame',frame)
    if cv2.waitKey(0)==ord('q'):
        cap.release()

"""

if __name__=='__main__':
        main()