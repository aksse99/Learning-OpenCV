import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
minArea = 500
color = (255,0,255)
numberPlateCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_russian_plate_number.xml")

vid = cv2.VideoCapture(0)
vid.set(3,frameWidth)
vid.set(4,frameHeight)
vid.set(10,200)
while True:
    success, img = vid.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = numberPlateCascade.detectMultiScale(imgGray,1.1,4)


    for(x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI",imgRoi)



    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
