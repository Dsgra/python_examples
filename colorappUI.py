import cv2
import numpy as np

def nothing(x):
    pass

# Ahora crearemos una imagen en negro y la utilizaremos como una ventana

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Dsgrande_Color_App_Get_Values')

# Crearemos en este momento barras para controlar los cambios de color

cv2.createTrackbar('R','Dsgrande_Color_App_Get_Values', 0, 255, nothing)
cv2.createTrackbar('G','Dsgrande_Color_App_Get_Values', 0, 255, nothing)
cv2.createTrackbar('B','Dsgrande_Color_App_Get_Values', 0, 255, nothing)

# En la parte del interfaz grafico creamos un switch ON/OFF

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'Dsgrande_Color_App_Get_Values', 0, 1, nothing)

while(1):
    cv2.imshow('Dsgrande_Color_App_Get_Values', img)
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
    # Determinar la posicion del trackback
    r = cv2.getTrackbarPos('R', 'Dsgrande_Color_App_Get_Values')
    g = cv2.getTrackbarPos('G', 'Dsgrande_Color_App_Get_Values')
    b = cv2.getTrackbarPos('B', 'Dsgrande_Color_App_Get_Values')
    s = cv2.getTrackbarPos(switch, 'Dsgrande_Color_App_Get_Values')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

