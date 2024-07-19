import numpy as np
import cv2


def mostrar_imagen_bn(imagen):
    cv2.imshow('Imagen B/N', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mostrar_imagen_negativa(imagen):
    negativo = 255 - imagen
    cv2.imshow('Imagen Negativa', negativo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def aplicar_umbral(imagen):
    umbral = int(input("Ingresa el umbral: "))
    umbralizada = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral:
                umbralizada[x, y] = 0
            else:
                umbralizada[x, y] = 255
    cv2.imshow('Imagen umbral', umbralizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def aplicar_umbral_invertido(imagen):
    umbral = int(input("Ingresa el umbral: "))
    umbral_invertido = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral:
                umbral_invertido[x, y] = 255
            else:
                umbral_invertido[x, y] = 0
    cv2.imshow('Imagen umbral invertido', umbral_invertido)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def aplicar_umbral_doble(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbraldoble = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral:
                umbraldoble[x, y] = 255
            if imagen[x, y] >= umbral2:
                umbraldoble[x, y] = 255
            else:
                umbraldoble[x, y] = 0
    cv2.imshow('Imagen umbral doble', umbraldoble)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def aplicar_umbral_doble_invertido(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbraldoble_invertido = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral:
                umbraldoble_invertido[x, y] = 0
            if imagen[x, y] >= umbral2:
                umbraldoble_invertido[x, y] = 0
            else:
                umbraldoble_invertido[x, y] = 255
    cv2.imshow('Imagen umbral doble invertido', umbraldoble_invertido)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def aplicar_umbral_escala_grises(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbralgris = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1:
                umbralgris[x, y] = 255
            if imagen[x, y] >= umbral2:
                umbralgris[x, y] = 255
            else:
                umbralgris[x, y] = imagen[x, y]
    cv2.imshow('Imagen umbral de la escala de grises', umbralgris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def aplicar_umbral_invertido_escala_grises(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbralgris_invertido = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1:
                umbralgris_invertido[x, y] = 255
            if imagen[x, y] >= umbral2:
                umbralgris_invertido[x, y] = 255
            else:
                umbralgris_invertido[x, y] = 255-imagen[x, y]
    cv2.imshow('Imagen umbral de la escala de grises invertido',
               umbralgris_invertido)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def operador_extension(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    op_extension = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1:
                op_extension[x, y] = 0
            if imagen[x, y] >= umbral2:
                op_extension[x, y] = 0
            else:
                op_extension[x, y] = (imagen[x, y]-umbral1) * \
                    (255/(umbral2-umbral1))
    cv2.imshow('Imagen operador de extension', op_extension)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def operador_reduccion_nivel_gris(imagen):
    umbrales = []
    while True:
        umbral_str = input("Ingresa un umbral (o 't' para terminar): ")
        if umbral_str.lower() == 't':
            break
        else:
            umbrales.append(int(umbral_str))
    umbrales.sort()
    n_reducidos = len(umbrales) + 1
    reducciongris = np.zeros_like(imagen, dtype=np.uint8)
    for i in range(n_reducidos):
        if i == 0:
            reducciongris[imagen <= umbrales[i]] = i * (256 // n_reducidos)
        elif i == n_reducidos - 1:
            reducciongris[imagen > umbrales[i - 1]] = i * (256 // n_reducidos)
        else:
            reducciongris[(imagen > umbrales[i - 1]) &
                          (imagen <= umbrales[i])] = i * (256 // n_reducidos)
    cv2.imshow('Imagen operador reduccion de nivel de gris', reducciongris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def transformacion_punto_a_punto(imagen):
    transformacion = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen

    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacion[x, y] = imagen[x, y]-negativo[x, y]
            if transformacion[x, y] > 256:
                transformacion[x, y] = 255
            if transformacion[x, y] <= 0:
                transformacion[x, y] = 0

    cv2.imshow('Imagen transformacion punto a punto', transformacion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def transformacion_punto_a_punto_adicion(imagen):
    transformacionad = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen

    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacionad[x, y] = round((imagen[x, y] + negativo[x, y]) / 2)
        if transformacionad[x, y] > 255:
            transformacionad[x, y] = 255
        elif transformacionad[x, y] < 0:
            transformacionad[x, y] = 0

    cv2.imshow('Imagen transformacion punto a punto ADICION', transformacionad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def transformacion_punto_a_punto_sustraccion(imagen):
    transformacionsus = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen

    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacionsus[x, y] = round(2*(imagen[x, y] - negativo[x, y]))
        if transformacionsus[x, y] > 255:
            transformacionsus[x, y] = 255
        elif transformacionsus[x, y] < 0:
            transformacionsus[x, y] = 0

    cv2.imshow('Imagen transformacion punto a punto SUSTRACCION',
               transformacionsus)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def operador_vecindad(imagen):
    ancho, alto = imagen.shape[:2]
    vecindad = np.zeros_like(imagen, dtype=np.uint8)

    for x in range(ancho):
        for y in range(alto):

            suma_vecindad = np.sum(
                imagen[max(0, x-1):min(x+2, ancho), max(0, y-1):min(y+2, alto)])
            valor_operador = round(2 * (imagen[x, y] - suma_vecindad / 9))

            if valor_operador > 255:
                valor_operador = 255
            elif valor_operador < 0:
                valor_operador = 0

            vecindad[x, y] = valor_operador

    cv2.imshow('Imagen con Operador de Vecindad', vecindad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    imagen = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)

    while True:
        print("1. Mostrar Imagen B/N")
        print("2. Mostrar Imagen Negativa")
        print("3. Aplicar Umbral")
        print("4. Aplicar Umbral Invertido")
        print("5. Aplicar Umbral Doble")
        print("6. Aplicar Umbral Doble Invertido")
        print("7. Aplicar Umbral a Escala de Grises")
        print("8. Aplicar Umbral Invertido a Escala de Grises")
        print("9. Operador de Extensión")
        print("10. Operador de Reducción de Nivel de Gris")
        print("11. Transformación Punto a Punto")
        print("12. Transformación Punto a Punto con Adición")
        print("13. Transformación Punto a Punto con Sustracción")
        print("14. Operador de Vecindad")
        print("15. Salir")

        opcion = input("Selecciona una opción (1-15): ")

        if opcion == '1':
            mostrar_imagen_bn(imagen)
        elif opcion == '2':
            mostrar_imagen_negativa(imagen)
        elif opcion == '3':
            aplicar_umbral(imagen)
        elif opcion == '4':
            aplicar_umbral_invertido(imagen)
        elif opcion == '5':
            aplicar_umbral_doble(imagen)
        elif opcion == '6':
            aplicar_umbral_doble_invertido(imagen)
        elif opcion == '7':
            aplicar_umbral_escala_grises(imagen)
        elif opcion == '8':
            aplicar_umbral_invertido_escala_grises(imagen)
        elif opcion == '9':
            operador_extension(imagen)
        elif opcion == '10':
            operador_reduccion_nivel_gris(imagen)
        elif opcion == '11':
            transformacion_punto_a_punto(imagen)
        elif opcion == '12':
            transformacion_punto_a_punto_adicion(imagen)
        elif opcion == '13':
            transformacion_punto_a_punto_sustraccion(imagen)
        elif opcion == '14':
            operador_vecindad(imagen)
        elif opcion == '15':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
