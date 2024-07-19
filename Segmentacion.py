import cv2
import numpy as np

# Función para filtrar el color seleccionado
def filter_color(img, lower_range, upper_range):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    res = cv2.bitwise_and(img, img, mask=mask)
    return res

# Leer la imagen
imgColor = cv2.imread("./Imagenes/billar.png")

# Convertir la imagen a HSV
hsv_img = cv2.cvtColor(imgColor, cv2.COLOR_BGR2HSV)

# Definir los rangos de color para cada opción
color_ranges = {
    'rojo': ((0, 100, 100), (10, 255, 255)),
    'verde': ((40, 100, 100), (80, 255, 255)),
    'azul': ((100, 100, 100), (140, 255, 255)),
    'morado': ((125, 100, 100), (160, 255, 255)),
    'amarillo': ((20, 100, 100), (40, 255, 255)),
    'rosa': ((150, 100, 100), (170, 255, 255)),
    'naranja': ((5, 100, 100), (15, 255, 255)),
    'celeste': ((85, 100, 100), (110, 255, 255)),
    'violeta': ((110, 100, 100), (135, 255, 255)),
    'marrón': ((0, 100, 40), (20, 255, 150)),
}

# Mostrar las opciones de color al usuario
print("Ingrese un color disponibles=> rojo, verde, azul, morado, amarillo, rosa, naranja, celeste, violeta, marrón")

# Pedir al usuario que seleccione un color
color = input("Ingrese el color que desea seleccionar: ").lower()

# Verificar si el color seleccionado está en las opciones
if color in color_ranges:
    # Filtrar la imagen por el color seleccionado
    lower_range, upper_range = color_ranges[color]
    filtered_img = filter_color(imgColor, np.array(lower_range), np.array(upper_range))

    # Mostrar la imagen filtrada
    cv2.imshow('Elementos de color ' + color, filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("El color ingresado no es válido.")
