import numpy as np
import cv2

drawing = False 
ix,iy = -1,-1
new_gesture = []

# mouse callback function
def record_new_pass(event,x,y,flags,param):
	global ix,iy,drawing

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			new_gesture.append((x,y))
		
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False

def store_gesture(height,width):
	pass=np.zeros((height,width),dtype=np.uint8)
	for point in new_gesture:
		cv2.circle(pass,point,5,255,-1)
	cv2.imshow('ges',pass)
	print('New Gesture Saved')
def create_new_gesture():
	new_gesture=[]
	pass_img = cv2.imread('../img/pass_img.png',1)
	cv2.namedWindow('Create a new password')
	cv2.setMouseCallback('Create a new password',record_new_pass)
	height, width = pass_img.shape[:2]
	while(True):
		cv2.imshow('Create a new password',pass_img)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			store_gesture(height,width)
			break

	cv2.destroyAllWindows()
