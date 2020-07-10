#Invisible cloak

#importing libraries
import numpy as np 
import cv2 
import time 


#video capture
cap = cv2.VideoCapture(0)

time.sleep(2)

#capturing background 
background = 0

for i  in range(30):
	ret, background = cap.read()


while(cap.isOpened()) :

	ret, img = cap.read() #cap image

	if not ret:
		break

#Coverting from BGR to HSV

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSB

	#HSV values
	lower_red = np.array([0, 120, 70])
	upper_red = np.array([10, 255, 255])

	mask1 = cv2.inRange(hsv, lower_red, upper_red) #separating cloak part


	lower_red = np.array([170, 120, 70])
	upper_red = np.array([180, 255, 255])

	mask2 = cv2.inRange(hsv, lower_red, upper_red)


	mask1 = mask1 + mask2 #OR 

	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,
		           np.ones([3,3], np.uint8 ), iterations = 2) # Noise removal

	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,
		            np.ones((3,3), np.uint8), iterations = 1)

	mask2 = cv2.bitwise_not(mask1) #Except the cloak

	res1 = cv2.bitwise_and(background, background, mask = mask1) # used for segmentation of the color (cloak)
	res2 = cv2.bitwise_and(img, img, mask = mask2) #used to substitute cloak part
	final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

	cv2.imshow("Extraordinary Window !!", final_output)
	k = cv2.waitKey(10)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()




	












