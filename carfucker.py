# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
video_src = 'dataset/video1.avi'
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier(cascade_src)
numcars = 0

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
        cv2.line(img, (640, 0), (640, 718), (0,255,0), 5)
        if (((x+x+w)/2) > 640): 
        	numcars=numcars+1   
    
    cv2.imshow('video', img)
    #font = cv2.FONT_HERSHEY_SIMPLEX
   #cv2.putText(img, str(numcars),(10,500), font, 4,(0,0,0),3,cv2.LINE_AA)
    print numcars
    
    if cv2.waitKey(33) == 27:
        break
	