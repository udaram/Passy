import numpy as np
import cv2
from pynput.keyboard import Key, Controller
drawing = False 
ix,iy = -1,-1
new_gesture = []

# mouse callback function
def record_gesture(event,x,y,flags,param):
	global ix,iy,drawing
	keyboard = Controller()

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		#print('left button clicked')

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			new_gesture.append((x,y))
		#print('mouse moved')

		
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		keyboard.press(Key.esc)      #simulating an esc keypress to close the window
		keyboard.release(Key.esc)
		#print('mouse up')

def store_gesture(shape):
	passwd=np.zeros(shape,dtype=np.uint8)
	for point in new_gesture:
		cv2.circle(passwd,point,4,255,-1)
	cv2.imwrite('pass_ges.jpg',passwd)
	print('New Gesture Saved')

def create_new_gesture():
	global new_gesture
	print('Preparing to create new gesture')
	new_gesture=[]
	pass_img = cv2.imread('img/pass_img.png',1)
	cv2.namedWindow('Create a new password')
	cv2.setMouseCallback('Create a new password',record_gesture)
	shape = pass_img.shape[:2]
	while(True):
		cv2.imshow('Create a new password',pass_img)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break

	cv2.destroyAllWindows()
	store_gesture(shape)

def get_mse(imageA,imageB):
	mse = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	mse /= float(imageA.shape[0] * imageA.shape[1])
	return mse

def login_gesture():
	global new_gesture
	new_gesture=[]
	secret_img=cv2.imread('pass_ges.jpg',0)
	login_img=cv2.imread('img/pass_img.png',1)
	cv2.namedWindow('Draw the gesture to login')
	cv2.setMouseCallback('Draw the gesture to login',record_gesture)
	shape=secret_img.shape[:2]
	while(True):
		cv2.imshow('Draw the gesture to login',login_img)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break	
	cv2.destroyAllWindows()
	passwd=np.zeros(shape,dtype=np.uint8)
	for point in new_gesture:
		cv2.circle(passwd,point,4,255,-1)

	sim = compare_img(passwd,secret_img)

	if sim>0.5:
		print("Authorized ; Match : "+str(sim))
	else:
		print("Not Auth")


	
def compare_img(img1,img2): #img2 should be the secret image
	height,width =img1.shape[:2]

	white_count=0
	original_white_count=0
	#sim_mat=np.zeros((height,width),dtype=np.uint8)
	for h in range(0,height):
		for w in range(0,width):
			if img2[h][w]==255:
				original_white_count+=1
			if img1[h][w]==255 and img2[h][w]==255:
				#sim_mat[h][w]=255
				white_count+=1


	sim = white_count/original_white_count

	return sim
	



if __name__=="__main__":
	print('1. Create new gesture\n2.Login gesture')
	while True:
		command=int(input())
		if command==1:
			create_new_gesture()
		elif command==2:
			login_gesture()
		