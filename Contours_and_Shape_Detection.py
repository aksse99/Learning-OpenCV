import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContours, cnt, -1, (0, 255, 0), 2)
        perim = cv2.arcLength(cnt, True)
        # print(perim)
        approx = cv2.approxPolyDP(cnt, 0.02*perim, True)
        print(len(approx))
        obj = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        if obj == 3:
            objectType = "Tri"
        elif obj == 4:
            x = w/float(h)
            if x > 0.95 and x < 1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        elif obj > 4:
            objectType = "Circle"
        else:
            objectType = "None"

        cv2.rectangle(imgContours, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(imgContours, objectType, (x+(w//2)-10, y+(h//2)+10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)


path = "Resources/shape.jpg"
img = cv2.imread(path)
imgContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 130, 200)
getContours(imgCanny)


cv2.imshow("Original", img)
cv2.imshow("Gray ", imgGray)
cv2.imshow("Blur ", imgBlur)
cv2.imshow("Canny ", imgCanny)
cv2.imshow("Contours ", imgContours)
cv2.waitKey(0)
