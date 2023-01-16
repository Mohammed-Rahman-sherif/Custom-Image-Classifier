import numpy as np
import cv2

mask_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.imread('test10.jpg')

gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
faces = mask_cascade.detectMultiScale(gray,1.01, 7)

for (x,y,w,h) in faces:
        cv2.rectangle(cap,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img', cap)
cv2.waitKey(0)
cv2.destroyAllWindows()
