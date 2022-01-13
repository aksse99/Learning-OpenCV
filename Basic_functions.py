import cv2
import numpy as np

img = cv2.imread("Resources/abc.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,100)
imgDailation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDailation,kernel,iterations=1)

cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDailation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
