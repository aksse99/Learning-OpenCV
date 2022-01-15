import cv2
import numpy as np

img = cv2.imread("Resources/work2.jpeg",1)
imgResize = cv2.resize(img,(400,400))

#imgHor = np.hstack((imgResize, imgResize))
#imgVer = np.vstack((imgResize, imgResize))

imgResize.shape = (200,800,3)
#cv2.imshow("Horizontal", imgHor)
#cv2.imshow("Vertical", imgVer)
cv2.imshow("Image", imgResize)
cv2.waitKey(0)
