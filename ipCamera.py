import cv2
import numpy as np

#Connecting to my phone camera in real-time
url = 'https://192.168.1.68:8080/video'
cap = cv2.VideoCapture(url)

#Defining the video type of the output
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.mp4v',fourcc, 20.0, (720 ,480))

#Applying filters in real-time
while(cap.isOpened()):
    _, frame = cap.read()
    #greyscale conversion
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #drawing a line
    lined = cv2.line(gray,(0,0),(511,511),(255,0,0),5)

    #display and save the video, quit by pressing 'q'
    cv2.imshow("Faces found", lined)
    out.write(lined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
