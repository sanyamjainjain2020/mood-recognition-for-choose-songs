import cv2 as cv
import matplotlib.pyplot as plt
from deepface import DeepFace
import sys
faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0)
while True:
# if 10:
    ret,frame=cap.read()
#     result = DeepFace.analyze(frame, actions=['emotion'])
    
    
    gray =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv.rectangle(frame,(x,y), (x+w, y+h), (0,255,0),2)
    
    
#     font = cv.FONT_HERSHEY_SIMPLEX
    
#     cv.putText(frame,
#               result['dominant_emotion'],
#               (50, 50),
#               font, 3,
#               (0,0,255),
#               2,
#               cv.LINE_4)
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q'):
        sys.exit()
    img=cv.imread('frame')
    predictions=DeepFace.analyze(img)
    predictions['dominant_emotion']
cap.release()
cv.destroyAllWindows()
