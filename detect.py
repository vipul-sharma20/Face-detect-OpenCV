import numpy as np
import cv2
cam = cv2.VideoCapture(0)
name = 'detect'
name1 = 'win'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow(name1, cv2.WINDOW_AUTOSIZE)
while True:
    s, img = cam.read()
   # cv2.imshow(name1, img)
   # key = cv2.waitKey(10)
   # if key == 27:
   #     cv.destroyWindow("win")
   #     break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow(name1, gray)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print s
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow(name, img)    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyWindow(name)
        break
    
