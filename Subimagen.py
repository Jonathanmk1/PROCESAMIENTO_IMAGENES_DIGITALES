import numpy as np
import cv2
import matplotlib.pyplot as plt
# blanco y negro
n = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)
# color
# n = cv2.imread('./Imagenes/lena.jpg')
print(n)
print(type(n))
r, c = n.shape
# r = tam[0]
# c = tam[1]
print(r)
print(c)
sun = n[100:, 100:]
plt.imshow(n, cmap='gray')
plt.waitforbuttonpress()

#cv2.imshow('Imagen', n)
#cv2.waitKey(0)
#cv2.imshow('Imagen', sun)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
