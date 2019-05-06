import cv2
import numpy as np

def photosh():
    file="iitjammu.jpg"
    frame=cv2.imread(file)
    frame=cv2.resize(frame,(1000,500))
    cv2.putText(frame,"Press 'Q' to quit from PHOTO",(250,25),cv2.FONT_HERSHEY_SIMPLEX,1,(20,200,50),2,cv2.LINE_AA)
    cv2.imshow('IIT Jammu',frame)
    cv2.waitKey(0)            
    cv2.destroyAllWindows() 
