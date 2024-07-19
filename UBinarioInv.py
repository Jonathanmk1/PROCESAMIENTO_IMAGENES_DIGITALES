import numpy as np
import cv2

p = cv2.imread('./Imagenes/coins.png', cv2.IMREAD_GRAYSCALE)
r, c = p.shape
q = np.zeros(p.shape, dtype=p.dtype)

umbral = 90
for x in range(r):
    for y in range(c):
        if p[x, y] > umbral:
            q[x, y] = 0
        else:
            q[x, y] = 255

cv2.imshow("Imagen de salida", q)
cv2.waitKey(0)
cv2.destroyAllWindows()
