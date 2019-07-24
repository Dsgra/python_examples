'''

'''

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

'''

'''

 import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('00175431.jpg',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros

mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] 

# apply mask and inverse DFT

fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()     

'''

'''
