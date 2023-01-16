import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

#img = cv2.imread('test2.jpg')
while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1, 6)

        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img', img)

        k = cv2.waitKey(100) & 0xff
        if k == 27:
                break
cap.release()
cv2.destroyAllWindows()
