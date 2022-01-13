import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)
#print(img.shape)
#img[100:200, 200:400] = 255,255,0

cv2.line(img,(0,0),(img.shape[0],500),(0,255,0),2)
cv2.rectangle(img,(0,0),(200,400),(255,255,0),2)
cv2.circle(img,(300,250),50,(0,0,255),3)
cv2.putText(img,"OPENCV",(100,300),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

cv2.imshow("Image",img)
cv2.waitKey(0)