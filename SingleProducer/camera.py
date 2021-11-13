import cv2
import numpy as np
from numpy.core.fromnumeric import shape


vid = cv2.VideoCapture(0)

i =1 
while i<2:
    ret, frame = vid.read()
    _,buff = cv2.imencode('.jpg', frame)
    i+=1
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if(k == 27):
        break
vid.release()
cv2.destroyAllWindows()

print(frame)
by = frame.tobytes()
s = np.frombuffer(by, dtype= np.uint8)
print(s.shape)
d = s.reshape(480,640,3)
print(d)
print(d.shape)
