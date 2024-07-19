import numpy as np
import cv2
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


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
    umbral = simpledialog.askinteger("Entrada", "Ingresa el umbral:")
    if umbral is not None:
        umbralizada = np.zeros_like(imagen, dtype=np.uint8)
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                umbralizada[x, y] = 0 if imagen[x, y] <= umbral else 255
        cv2.imshow('Imagen umbral', umbralizada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def aplicar_umbral_invertido(imagen):
    umbral = simpledialog.askinteger("Entrada", "Ingresa el umbral:")
    if umbral is not None:
        umbral_invertido = np.zeros_like(imagen, dtype=np.uint8)
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                umbral_invertido[x, y] = 255 if imagen[x, y] <= umbral else 0
        cv2.imshow('Imagen umbral invertido', umbral_invertido)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def aplicar_umbral_doble(imagen):
    umbral1 = simpledialog.askinteger("Entrada", "Ingresa el primer umbral:")
    umbral2 = simpledialog.askinteger("Entrada", "Ingresa el segundo umbral:")
    if umbral1 is not None and umbral2 is not None:
        umbraldoble = np.zeros_like(imagen, dtype=np.uint8)
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                    umbraldoble[x, y] = 255
                else:
                    umbraldoble[x, y] = 0
        cv2.imshow('Imagen umbral doble', umbraldoble)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def aplicar_umbral_doble_invertido(imagen):
    umbral1 = simpledialog.askinteger("Entrada", "Ingresa el primer umbral:")
    umbral2 = simpledialog.askinteger("Entrada", "Ingresa el segundo umbral:")
    if umbral1 is not None and umbral2 is not None:
        umbraldoble_invertido = np.zeros_like(imagen, dtype=np.uint8)
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                    umbraldoble_invertido[x, y] = 0
                else:
                    umbraldoble_invertido[x, y] = 255
        cv2.imshow('Imagen umbral doble invertido', umbraldoble_invertido)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def aplicar_umbral_escala_grises(imagen):
    umbral1 = simpledialog.askinteger("Entrada", "Ingresa el primer umbral:")
    umbral2 = simpledialog.askinteger("Entrada", "Ingresa el segundo umbral:")
    if umbral1 is not None and umbral2 is not None:
        umbralgris = np.zeros_like(imagen, dtype=np.uint8)
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                    umbralgris[x, y] = 255
                else:
                    umbralgris[x, y] = imagen[x, y]
        cv2.imshow('Imagen umbral de la escala de grises', umbralgris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def aplicar_umbral_invertido_escala_grises(imagen):
    umbral1 = simpledialog.askinteger("Entrada", "Ingresa el primer umbral:")
    umbral2 = simpledialog.askinteger("Entrada", "Ingresa el segundo umbral:")
    if umbral1 is not None and umbral2 is not None:
        umbralgris_invertido = np.zeros_like(imagen, dtype=np.uint8)
        for x in range(imagen.shape[0]):
            for y in range(imagen.shape[1]):
                if imagen[x, y] <= umbral1 or imagen[x, y] >= umbral2:
                    umbralgris_invertido[x, y] = 255
                else:
                    umbralgris_invertido[x, y] = 255 - imagen[x, y]
        cv2.imshow('Imagen umbral de la escala de grises invertido', umbralgris_invertido)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def operador_extension(imagen):
    umbral1 = simpledialog.askinteger("Entrada", "Ingresa el primer umbral:")
    umbral2 = simpledialog.askinteger("Entrada", "Ingresa el segundo umbral:")
    if umbral1 is not None and umbral2 is not None:
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
        umbral_str = simpledialog.askstring("Entrada", "Ingresa un umbral (o 't' para terminar):")
        if umbral_str is None or umbral_str.lower() == 't':
            break
        else:
            umbrales.append(int(umbral_str))
    if umbrales:
        umbrales.sort()
        n_reducidos = len(umbrales) + 1
        reducciongris = np.zeros_like(imagen, dtype=np.uint8)
        for i in range(n_reducidos):
            if i == 0:
                reducciongris[imagen <= umbrales[i]] = i * (256 // n_reducidos)
            elif i == n_reducidos - 1:
                reducciongris[imagen > umbrales[i - 1]] = i * (256 // n_reducidos)
            else:
                reducciongris[(imagen > umbrales[i - 1]) & (imagen <= umbrales[i])] = i * (256 // n_reducidos)
        cv2.imshow('Imagen operador reduccion de nivel de gris', reducciongris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def transformacion_punto_a_punto(imagen):
    transformacion = np.zeros_like(imagen, dtype=np.uint8)
    negativo = 255 - imagen
    for x in range(imagen.shape[0]):
        for y in range(imagen.shape[1]):
            transformacion[x, y] = imagen[x, y] - negativo[x, y]
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
            transformacionsus[x, y] = round(2 * (imagen[x, y] - negativo[x, y]))
            if transformacionsus[x, y] > 255:
                transformacionsus[x, y] = 255
            elif transformacionsus[x, y] < 0:
                transformacionsus[x, y] = 0
    cv2.imshow('Imagen transformacion punto a punto SUSTRACCION', transformacionsus)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def operador_vecindad(imagen):
    ancho, alto = imagen.shape[:2]
    vecindad = np.zeros_like(imagen, dtype=np.uint8)
    for x in range(ancho):
        for y in range(alto):
            suma_vecindad = np.sum(imagen[max(0, x - 1):min(x + 2, ancho), max(0, y - 1):min(y + 2, alto)])
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

    def on_button_click(option):
        if option == '1':
            mostrar_imagen_bn(imagen)
        elif option == '2':
            mostrar_imagen_negativa(imagen)
        elif option == '3':
            aplicar_umbral(imagen)
        elif option == '4':
            aplicar_umbral_invertido(imagen)
        elif option == '5':
            aplicar_umbral_doble(imagen)
        elif option == '6':
            aplicar_umbral_doble_invertido(imagen)
        elif option == '7':
            aplicar_umbral_escala_grises(imagen)
        elif option == '8':
            aplicar_umbral_invertido_escala_grises(imagen)
        elif option == '9':
            operador_extension(imagen)
        elif option == '10':
            operador_reduccion_nivel_gris(imagen)
        elif option == '11':
            transformacion_punto_a_punto(imagen)
        elif option == '12':
            transformacion_punto_a_punto_adicion(imagen)
        elif option == '13':
            transformacion_punto_a_punto_sustraccion(imagen)
        elif option == '14':
            operador_vecindad(imagen)
        elif option == '15':
            root.quit()

    root = tk.Tk()
    root.title("Procesamiento de Imágenes")

    options = [
        "1. Mostrar Imagen B/N",
        "2. Mostrar Imagen Negativa",
        "3. Aplicar Umbral",
        "4. Aplicar Umbral Invertido",
        "5. Aplicar Umbral Doble",
        "6. Aplicar Umbral Doble Invertido",
        "7. Aplicar Umbral a Escala de Grises",
        "8. Aplicar Umbral Invertido a Escala de Grises",
        "9. Operador de Extensión",
        "10. Operador de Reducción de Nivel de Gris",
        "11. Transformación Punto a Punto",
        "12. Transformación Punto a Punto con Adición",
        "13. Transformación Punto a Punto con Sustracción",
        "14. Operador de Vecindad",
        "15. Salir"
    ]

    for option in options:
        btn = tk.Button(root, text=option, command=lambda opt=option.split('.')[0]: on_button_click(opt))
        btn.pack(fill='both')

    root.mainloop()


if __name__ == "__main__":
    main()
