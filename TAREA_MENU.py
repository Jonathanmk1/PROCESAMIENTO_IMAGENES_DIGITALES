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
    umbral_doble = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                umbral_doble[x, y] = 255
            else:
                umbral_doble[x, y] = 0
    cv2.imshow('Imagen umbral doble', umbral_doble)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aplicar_umbral_doble_invertido(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbral_doble_invertido = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                umbral_doble_invertido[x, y] = 0
            else:
                umbral_doble_invertido[x, y] = 255
    cv2.imshow('Imagen umbral doble invertido', umbral_doble_invertido)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aplicar_umbral_escala_grises(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbral_gris = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                umbral_gris[x, y] = 255
            else:
                umbral_gris[x, y] = imagen[x, y]
    cv2.imshow('Imagen umbral de la escala de grises', umbral_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aplicar_umbral_invertido_escala_grises(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    umbral_gris_invertido = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                umbral_gris_invertido[x, y] = 255
            else:
                umbral_gris_invertido[x, y] = 255 - imagen[x, y]
    cv2.imshow('Imagen umbral de la escala de grises invertido', umbral_gris_invertido)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def operador_extension(imagen):
    umbral1 = int(input("Ingresa el primer umbral: "))
    umbral2 = int(input("Ingresa el segundo umbral: "))
    op_extension = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                op_extension[x, y] = 0
            else:
                op_extension[x, y] = (imagen[x, y] - umbral1) * (255 / (umbral2 - umbral1))
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
    reduccion_gris = np.zeros_like(imagen, dtype=np.uint8)
    for i in range(n_reducidos):
        if i == 0:
            reduccion_gris[imagen <= umbrales[i]] = i * (256 // n_reducidos)
        elif i == n_reducidos - 1:
            reduccion_gris[imagen > umbrales[i - 1]] = i * (256 // n_reducidos)
        else:
            reduccion_gris[(imagen > umbrales[i - 1]) & (imagen <= umbrales[i])] = i * (256 // n_reducidos)
    cv2.imshow('Imagen operador reduccion de nivel de gris', reduccion_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transformacion_punto_a_punto(imagen):
    transformacion = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacion[x, y] = imagen[x, y] - negativo[x, y]
            if transformacion[x, y] > 255:
                transformacion[x, y] = 255
            if transformacion[x, y] <= 0:
                transformacion[x, y] = 0
    cv2.imshow('Imagen transformacion punto a punto', transformacion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transformacion_punto_a_punto_adicion(imagen):
    transformacion_adicion = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacion_adicion[x, y] = round((imagen[x, y] + negativo[x, y]) / 2)
            if transformacion_adicion[x, y] > 255:
                transformacion_adicion[x, y] = 255
            elif transformacion_adicion[x, y] < 0:
                transformacion_adicion[x, y] = 0
    cv2.imshow('Imagen transformacion punto a punto ADICION', transformacion_adicion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transformacion_punto_a_punto_sustraccion(imagen):
    transformacion_sustraccion = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacion_sustraccion[x, y] = round(2 * (imagen[x, y] - negativo[x, y]))
            if transformacion_sustraccion[x, y] > 255:
                transformacion_sustraccion[x, y] = 255
            elif transformacion_sustraccion[x, y] < 0:
                transformacion_sustraccion[x, y] = 0
    cv2.imshow('Imagen transformacion punto a punto SUSTRACCION', transformacion_sustraccion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def operador_vecindad(imagen, x, y, mascara):
    ancho, alto = imagen.shape[:2]
    m_ancho, m_alto = mascara.shape[:2]
    vecindad = np.zeros_like(imagen, dtype=np.uint8)
    for i in range(ancho):
        for j in range(alto):
            suma_vecindad = np.sum(imagen[max(0, i - m_ancho // 2):min(i + m_ancho // 2 + 1, ancho),
                                          max(0, j - m_alto // 2):min(j + m_alto // 2 + 1, alto)])
            valor_operador = round(2 * (imagen[i, j] - suma_vecindad / 9))
            vecindad[i, j] = np.clip(valor_operador, 0, 255)
    cv2.imshow('Imagen con Operador de Vecindad', vecindad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aplicar_convolucion(imagen):
    kernel = []
    print("Ingrese los valores del kernel (presione la tecl_Enter después de ingresar cada valor):")
    for i in range(3):
        fila = input().split()
        fila = [float(val) for val in fila]
        kernel.append(fila)
    kernel = np.array(kernel)

    convolucion = cv2.filter2D(imagen, -1, kernel)

    cv2.imshow('Imagen con Convolución', convolucion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aplicar_transformacion(imagen):
    opciones = ["1. Traslación", "2. Rotación", "3. Escalado"]
    print("\n".join(opciones))
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == '1':
        dx = int(input("Ingrese el desplazamiento en x: "))
        dy = int(input("Ingrese el desplazamiento en y: "))
        matriz_translacion = np.float32([[1, 0, dx], [0, 1, dy]])
        imagen_transformada = cv2.warpAffine(imagen, matriz_translacion, (imagen.shape[1], imagen.shape[0]))

    elif opcion == '2':
        grados = float(input("Ingrese el ángulo de rotación (en grados): "))
        matriz_rotacion = cv2.getRotationMatrix2D((imagen.shape[1] / 2, imagen.shape[0] / 2), grados, 1)
        imagen_transformada = cv2.warpAffine(imagen, matriz_rotacion, (imagen.shape[1], imagen.shape[0]))

    elif opcion == '3':
        factor_escala = float(input("Ingrese el factor de escala: "))
        imagen_transformada = cv2.resize(imagen, None, fx=factor_escala, fy=factor_escala)

    else:
        print("Opción inválida")
        return

    cv2.imshow('Imagen transformada', imagen_transformada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    imagen = cv2.imread('./Imagenes/ex2p.jpg', cv2.IMREAD_GRAYSCALE)

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
        print("15. Aplicar Convolución")
        print("16. Aplicar Transformación")
        print("17. Salir")

        opcion = input("Selecciona una opción (1-17): ")

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
            x = int(input("Ingrese la posición x del punto central: "))
            y = int(input("Ingrese la posición y del punto central: "))
            mascara = np.ones((3, 3), dtype=np.float32)
            operador_vecindad(imagen, x, y, mascara)
        elif opcion == '15':
            aplicar_convolucion(imagen)
        elif opcion == '16':
            aplicar_transformacion(imagen)
        elif opcion == '17':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
