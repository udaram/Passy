import cv2
import numpy as np

def play():
    file="video.mp4"
    cap = cv2.VideoCapture(file)
    while True :
        ret,frame = cap.read()  
        cv2.putText(frame,"Press 'Q' to quit the video",(80,20),cv2.FONT_HERSHEY_SIMPLEX,1,(20,200,50),2,cv2.LINE_AA)
        cv2.imshow('Movie',frame) 
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
                
    cap.release()
    cv2.destroyAllWindows()

