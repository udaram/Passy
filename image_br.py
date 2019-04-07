
import cv2
import numpy as np


image ="cat.jpeg"
#creating blank window
blank_image = np.zeros((400,500,3), np.uint8)

#for making boxes and naming the boxes
cv2.putText(blank_image,'1',(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.rectangle(blank_image,(0,0),(200,200),(255,255,255),2)
cv2.putText(blank_image,'2',(300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.rectangle(blank_image,(200,0),(400,200),(255,255,255),2)
cv2.putText(blank_image,'3',(100,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.rectangle(blank_image,(0,200),(200,400),(255,255,255),2)
cv2.putText(blank_image,'4',(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.rectangle(blank_image,(200,200),(400,400),(255,255,255),2)


#reading image and creating window
cv2.namedWindow('window')
im=cv2.imread(image)
im=cv2.resize(im,(400,400))

#creating four segment images
im1=im[0:200,0:200]
_im1=cv2.resize(im1,(100,100))

im2=im[0:200,200:400]
_im2=cv2.resize(im2,(100,100))

im3=im[200:400,0:200]
_im3=cv2.resize(im3,(100,100))

im4=im[200:400,200:400]
_im4=cv2.resize(im4,(100,100))

#Global variables
count=0  #global count 
f=False

#function for counter
def fun_count(x):
    global count
    
    if x>=400:
        count+=1
    return count

#function to coompare the images
def image_match():
    global f
    f=np.array_equal(np.array(blank_image[0:400,0:400]),np.array(im))
    return f
    
#function for mouse click 
def keep_coordinates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        coun=fun_count(x)
        if(x>=400 and coun<=4):
            
            #print(x," ", y)
            if(y>=0 and y<=100):
                image=im4
            elif(y<200):
                image=im1
            elif(y<300):
                image=im2
            else:
                image=im3
            #print(coun)
            if coun is 1:
                blank_image[0:200,0:200]=image
            elif coun is 2:
                blank_image[0:200,200:400]=image
            elif coun is 3:
                blank_image[200:400,0:200]=image
            elif coun is 4:
                blank_image[200:400,200:400]=image
            
            cv2.imshow('window',blank_image)
        f=image_match()
        if(coun is 4):
            if f:
                print("correct")
            else:
                print("wrong")
                
#setMouseCallback
cv2.setMouseCallback('window',keep_coordinates)

#side selection subimage partof window
blank_image[0:100,400:500]=_im4
blank_image[100:200,400:500]=_im1
blank_image[200:300,400:500]=_im2
blank_image[300:400,400:500]=_im3
#horizontal line
cv2.line(blank_image,(400,100),(500,100),(0,0,0),2)
cv2.line(blank_image,(400,200),(500,200),(0,0,0),2)
cv2.line(blank_image,(400,300),(500,300),(0,0,0),2)
cv2.line(blank_image,(400,400),(500,400),(0,0,0),2)
#vertical line
cv2.line(blank_image,(400,0),(400,400),(0,0,0),2)

#display images
cv2.imshow('window',blank_image)
#cv2.imshow('cat',im)

#to close window with pressing any key
cv2.waitKey(0)
cv2.destroyAllWindows() 
