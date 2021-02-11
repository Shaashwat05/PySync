import numpy as np
import cv2
import time

# The duration in seconds of the video captured
capture_duration = 5

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

start_time = time.time()
i=0
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    print(i)
    if ret==True:
        out.write(frame)
        i+=1
        #cv2.imshow('frame',frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()