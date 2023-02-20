import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

import serial                              # add Serial library for Serial communication

Arduino_Serial = serial.Serial('com6',9600)  #Create Serial port object called arduinoSerialData
print(Arduino_Serial.readline())               #read the serial data and print it as line

while True:
    ret,frame = video.read()
    hands,img = detector.findHands(frame)

    if hands:
        lmlist=hands[0]
        fingerUp=detector.fingersUp(lmlist)
        print(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
           # Arduino_Serial.write(b'0')
        if fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
        if fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
        if fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
        if fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
        if fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2,cv2.LINE_AA)
            #Arduino_Serial.write(b'1')


    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

#----------------------------------------