
import numpy as np
import cv2

# Leer la imagen en blanco y negro
imagen = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Definir la máscara
mascara = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

# Dimensiones de la imagen y la máscara
alto_imagen, ancho_imagen = imagen.shape
alto_mascara, ancho_mascara = mascara.shape

# Crear una matriz para la imagen convolucionada
imagen_conv = np.zeros_like(imagen)

# Aplicar la convolución a la imagen
for y in range(alto_imagen):
    for x in range(ancho_imagen):
        valor_pixel = 0
        for i in range(alto_mascara):
            for j in range(ancho_mascara):
                # Calcular las coordenadas en la imagen original considerando el desplazamiento
                x_imagen = x - ancho_mascara // 2 + j
                y_imagen = y - alto_mascara // 2 + i
                # Verificar si las coordenadas están dentro de la imagen
                if x_imagen >= 0 and x_imagen < ancho_imagen and y_imagen >= 0 and y_imagen < alto_imagen:
                    valor_pixel += imagen[y_imagen, x_imagen] * mascara[i, j]
        imagen_conv[y, x] = np.clip(valor_pixel, 0, 255)

# Mostrar la imagen resultante
cv2.imshow('Imagen con Convolución', imagen_conv)
cv2.waitKey(0)
cv2.destroyAllWindows()
