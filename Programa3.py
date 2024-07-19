# generar una lista de 5 ceros
import numpy as np
import cv2
# lista de ceros
a1 = np.zeros(5, dtype=np.int8)
# lista de unos
a1 = np.ones(5, dtype=np.int8)
# a1 = np.array([0, 0, 0, 0, 0])

# solo crear un numero escalar
a1 = np.array(5)
# si ponemos solo el corchete lo hace lista y esto es de una dimension a1 = np.array([5],[2],[3])
a1 = np.array([5])
# para dos diensiones, corchetes ahi mismo
a1 = [[5], [10, 34]]

a1 = [[5], [10, 34]]
a1 = np.array([[[5, 2], [10, 34]]])

# print(a1)
# print(type(a1[0][0]))

# ahora una matriz de 5 x 4 de unos
a1 = np.ones((2, 5, 4), dtype=np.int8)
# print(a1)
# print(type(a1))
# print(a1[1, 1, 1])

# ahora con numeros aleatorios, una matriz de tupla
a1 = np.random.randint(0, 255, (2, 5, 4), dtype=np.uint8)
# print(a1)
# imprimir un valor especifico de la matriz
# print(type(a1[1,0,2]))
# print(type(a1))


# ejercicio, hacer un arreglo en una matriz
m = np.arange(24).reshape(6, 4)
# print(m)

matriz1 = np.random.randint(0, 255, (320, 640), dtype=np.uint8)
print(matriz1)
cv2.imshow('Image', matriz1)
cv2.waitKey(0)
cv2.destroyAllWindows()
submatriz = matriz1[2:5, 2:6]
print("")
print(submatriz)
"""
para las array de la linea 13  para arriba

print(a1)
print(type(a1))
print(type(a1[0]))
"""
