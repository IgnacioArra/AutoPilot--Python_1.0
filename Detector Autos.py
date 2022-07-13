
import cv2
import pyshine as ps,cv2
import time

cascade_src = 'cars.xml'
img = 'C:\\Users\\Ignacio\\Desktop\\Autos\\auto.mp4'
#video_src = 'C:\Users\Ignacio\Desktop\Autos\auto.mp4'

cap = cv2.VideoCapture(img)
car_cascade = cv2.CascadeClassifier(cascade_src)
while True:
    ret, frame = cap.read()
   

    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.2, 3,)
    

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255, 250, 240),1)         

    cv2.imshow('video', img)
    if cv2.waitKey(33) == 27:
        break

print ("SE HA CERRADO EL SISTEMA")

        

cv2.destroyAllWindows()
