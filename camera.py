import cv2
import numpy as np

vid = cv2.VideoCapture(0)

i =1 
while i<2:
    ret, frame = vid.read()
    _,buff = cv2.imencode('.jpg', frame)
    arr = buff.tobytes()
    print(type(arr))
    i+=1
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if(k == 27):
        break
vid.release()
cv2.destroyAllWindows()
