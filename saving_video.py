import numpy as np
import cv2
import math

cap = cv2.VideoCapture('How Air Traffic Control Works.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    centerH = height//2
    centerW = width//2
    center = (centerW, centerH)
    if ret is True:
        frame = 255 - frame
        frame = cv2.flip(frame, 0)
        frame = cv2.line(frame, (0,0), (100,100), (255,0,0), 10)
        frame = cv2.rectangle(frame, (centerW-128, centerH-128), (width//2+128, height//2+128), (0,255,0), 10)
        frame = cv2.circle(frame, center, 128, (0,0,255), 5, cv2.LINE_AA)
        frame = cv2.ellipse(frame, center, (256,128), counter, 0, 360, (255,255,0), 5, cv2.LINE_AA)

        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        pts = np.array([[100, 50], [200, 300], [700, 200], [500, 100]], np.int32)
        frame = cv2.polylines(frame, [pts], True, (0,255,255), thickness=10, lineType=cv2.LINE_AA)

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, 'SOME TEXT HERE', center, font, 5, (0,0,0), 5, cv2.LINE_AA)

        out.write(frame)

        cv2.imshow('frame', frame)
        if(cv2.waitKey(1)) & 0xFF == ord('q'):
            break
        counter+=1
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()