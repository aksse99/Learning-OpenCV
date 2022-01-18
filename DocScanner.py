import cv2
import numpy as np

widthImg = 640
heightImg = 480

cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)

    return imgThres


def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>5000:
            cv2.drawContours(imgContours,cnt,-1,(0,255,0),2)
            perim = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*perim, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
        return biggest

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgContours = img.copy()
    imgThres = preProcessing(img)
    getContours(imgThres)
    cv2.imshow("Result",imgContours)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break