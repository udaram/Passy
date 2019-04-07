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
		print('left button clicked')

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			new_gesture.append((x,y))
		print('mouse moved')
		
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		print('mouse up')

def store_gesture(shape):
	passwd=np.zeros(shape,dtype=np.uint8)
	for point in new_gesture:
		cv2.circle(passwd,point,5,255,-1)
	cv2.imwrite('pass_ges.jpg',passwd)
	print('New Gesture Saved')

def create_new_gesture():
	print('Preparing to create new gesture')
	new_gesture=[]
	pass_img = cv2.imread('img/pass_img.png',1)
	cv2.namedWindow('Create a new password')
	cv2.setMouseCallback('Create a new password',record_new_pass)
	shape = pass_img.shape[:2]
	while(True):
		cv2.imshow('Create a new password',pass_img)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break

	cv2.destroyAllWindows()
	store_gesture(shape)

if __name__=="__main__":
	create_new_gesture()