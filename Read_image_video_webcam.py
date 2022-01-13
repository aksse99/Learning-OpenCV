import cv2
#Importing a Image

#img = cv2.imread("Resources/work.jpg")
#cv2.imshow("Output",img)
#cv2.waitKey(0)

#Imorting a Video

#vid = cv2.VideoCapture("Resources/song.mp4")
#while True:
#   success, img = vid.read()
#  cv2.imshow("Video", img)
# if cv2.waitKey(1) & 0xff ==ord('q'):
#    break

#Importing webcam

vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,200)
while True:
    success, img = vid.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
