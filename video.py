import numpy as np
import cv2
import time

data = []

# The duration in seconds of the video captured
capture_duration = 5

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

start_time = time.time()
i=0
while( int(time.time() - start_time) < capture_duration ):
    #start2 = time.time()
    ret, frame = cap.read()
    #ans = time.time()  - start2
    print(i)
    if ret==True:
        data.append(frame)
        i+=1
        #cv2.imshow('frame',frame)

for i in data:
    out.write(i)


cap.release()
out.release()
cv2.destroyAllWindows()
