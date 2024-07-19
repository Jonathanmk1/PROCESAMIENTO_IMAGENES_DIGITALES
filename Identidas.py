import numpy as np
import cv2
""" tarea hacer las demas funciones 
el profe quiere dos cosas: a patin y con funciones
"""
# creamos una imagen que queremos leer en blanco y negro
p = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)
# tamaño de los renglones y columnas
r, c = p.shape
# creamos una matriz vacia para guardar la nueva imagen de puros zeros
q = np.zeros((r, c), dtype=np.uint8)
# q = 255 - p
# Umbral
ua = 75
ub = 139

for x in range(r):
    for y in range(c):
        if p[x, y] <= ub:
            q[x, y] = 0
        if p[x, y] > ub:
            q[x, y] = 255

# cv2.namedWindow('Imagen', cv2.WINDOW_FULLSCREEN)
cv2.imshow('Imagen Entrada', p)
cv2.waitKey(0)
cv2.imshow('Imagen Salida', q)
cv2.waitKey(0)
cv2.destroyAllWindows()
