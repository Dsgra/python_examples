
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('00175431.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap ='gray')
plt.title('Imagen de Entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mag_spectrum, cmap = 'gray')
plt.title('Espectograma Magnitude'), plt.xticks([]), plt.yticks([])
plt.show()

rep = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
ref = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT)
ref101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wr = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
cons= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=None)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(rep,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(ref,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(ref101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wr,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(cons,'gray'),plt.title('CONSTANT')

plt.show()
