import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    print(frame)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if(k == 27):
        break
vid.release()
cv2.destroyAllWindows()
