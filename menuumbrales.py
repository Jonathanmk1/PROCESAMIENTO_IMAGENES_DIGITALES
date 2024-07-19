import cv2
import numpy as np


def umbral_binario(imagen, umbral):
    p = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    r, c = p.shape
    q = np.zeros(p.shape, dtype=p.dtype)

    for x in range(r):
        for y in range(c):
            if p[x, y] > umbral:
                q[x, y] = 255
            else:
                q[x, y] = 0

    cv2.imshow("Imagen de salida", q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# _,q = cv2.threshold(p, umbral, 255, cv2.THRESH_BINARY)


def umbral_binario_invertido(imagen, umbral):
    p = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    r, c = p.shape
    q = np.zeros(p.shape, dtype=p.dtype)

    for x in range(r):
        for y in range(c):
            if p[x, y] > umbral:
                q[x, y] = 0
            else:
                q[x, y] = 255

    cv2.imshow("Imagen de salida", q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# _,q = cv2.threshold(p, umbral, 255, cv2.THRESH_BINARY_INV)


def truncar(imagen, umbral):
    p = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    r, c = p.shape
    q = np.zeros(p.shape, dtype=p.dtype)

    for x in range(r):
        for y in range(c):
            if p[x, y] > umbral:
                q[x, y] = umbral
            else:
                q[x, y] = p[x, y]

    cv2.imshow("Imagen de salida", q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# _,q = cv2.threshold(p, umbral, 255, cv2.THRESH_TRUNC)


def ajustar_a_0(imagen, umbral):
    p = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    r, c = p.shape
    q = np.zeros(p.shape, dtype=p.dtype)

    for x in range(r):
        for y in range(c):
            if p[x, y] < umbral:
                q[x, y] = 0
            else:
                q[x, y] = p[x, y]

    cv2.imshow("Imagen de salida", q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# _,q = cv2.threshold(p, umbral, 255, cv2.THRESH_TOZERO)


def ajustar_a_0_invertido(imagen, umbral):
    p = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
    r, c = p.shape
    q = np.zeros(p.shape, dtype=p.dtype)

    for x in range(r):
        for y in range(c):
            if p[x, y] > umbral:
                q[x, y] = 0
            else:
                q[x, y] = p[x, y]

    cv2.imshow("Imagen de salida", q)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# _,q = cv2.threshold(p, umbral, 255, cv2.THRESH_TOZERO_INV)


def menu(imagen, umbral):
    print("1. Umbral binario")
    print("2. Umbral binario invertido")
    print("3. Truncar")
    print("4. Ajustar a 0")
    print("5. Ajustar a 0 invertido")
    print("0. Salir")

    while True:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 0:
            print("¡Hasta luego!")
            break

        if opcion == 1:
            umbral_binario(imagen, umbral)
        elif opcion == 2:
            umbral_binario_invertido(imagen, umbral)
        elif opcion == 3:
            truncar(imagen, umbral)
        elif opcion == 4:
            ajustar_a_0(imagen, umbral)
        elif opcion == 5:
            ajustar_a_0_invertido(imagen, umbral)
        else:
            print("Opción inválida")


imagen = './Imagenes/coins.png'
umbral = 90

menu(imagen, umbral)
