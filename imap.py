# imagen_path = "./Imagenes/imagen_pixeleada.jpg"
import cv2
import numpy as np
from scipy.signal import deconvolve
import os


def mejorar_imagen_borrosa(imagen_path, kernel_size=(5, 5), lambda_=0.01):
    # Cargar la imagen
    imagen = cv2.imread(imagen_path)

    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Calcular el kernel de desenfoque gaussiano
    kernel = np.ones(kernel_size, np.float32) / \
        (kernel_size[0] * kernel_size[1])

    # Aplicar el desenfoque gaussiano para simular el desenfoque
    imagen_borrosa = cv2.filter2D(imagen_gris, -1, kernel)

    # Convertir la imagen borrosa a señal unidimensional
    signal = imagen_borrosa.flatten()

    # Realizar la deconvolución ciega para mejorar la imagen borrosa
    imagen_mejorada, _ = deconvolve(
        signal, np.hstack((kernel.flatten(), lambda_)))

    # Escalar los valores de píxeles para que estén en el rango correcto
    imagen_mejorada = np.clip(imagen_mejorada, 0, 255).astype(np.uint8)

    # Reconvertir la señal a matriz bidimensional
    imagen_mejorada = imagen_mejorada.reshape(imagen_borrosa.shape)

    # Obtener la ruta del directorio y el nombre del archivo
    directorio, nombre_archivo = os.path.split(imagen_path)

    # Guardar la imagen mejorada
    nombre, extension = os.path.splitext(nombre_archivo)
    nueva_ruta = os.path.join(directorio, nombre + "_mejorada" + extension)
    cv2.imwrite(nueva_ruta, imagen_mejorada)


# Ruta de la imagen que deseas mejorar
imagen_path = "./Imagenes/imagen_pixeleada.jpg"
# Llamar a la función para mejorar la imagen borrosa
mejorar_imagen_borrosa(imagen_path)
