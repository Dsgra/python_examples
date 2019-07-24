# Convert Video Gray Video_Files
import numpy as np
import cv2

cap = cv2.VideoCapture('big_buck_bunny_480p_h264SyncLogo.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

