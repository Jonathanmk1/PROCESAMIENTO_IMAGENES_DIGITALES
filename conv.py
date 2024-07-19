import numpy as np
import cv2

imagen = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)
# máscara
mascara = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
# mascara = np.array([[1/9, 1/9, 1/9],[1/9, 1/9, 1/9],[1/9, 1/9, 1/9]])

# tamaño de los renglones y columnas
r, c = imagen.shape
# creamos una matriz vacia para guardar la nueva imagen de puros zeros
nueva = np.zeros((r, c), dtype=np.uint8)
# Aplicar la convolución
for i in range(1, r - 1):
    for j in range(1, c - 1):
        valor = np.sum(imagen[i - 1:i + 2, j - 1:j + 2] * mascara)
        # Aplicar saturación en los extremos
        nueva[i, j] = min(max(valor, 0), 255)

# Mostrar la imagen
cv2.imshow('Imagen convolucionada', nueva)
cv2.waitKey(0)
cv2.destroyAllWindows()
