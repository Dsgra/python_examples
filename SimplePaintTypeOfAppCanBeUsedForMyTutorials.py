'''
This example will use some of the cv2 openCV library capabilities and it is
a really simple example allowing us to draw circles.
'''

import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# Now it is needed to create a callback function to draw a circle
import cv2
import numpy as np

#Mouse callback function
def draw_circle(event,x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),25,(255,0,0),-1)
# Creating a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
