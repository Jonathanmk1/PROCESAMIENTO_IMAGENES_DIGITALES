import cv2
import numpy as  np

img_gris = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)
img_gris2 = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)

r, c = img_gris.shape
r, c = img_gris2.shape


def operador_identidad():
    I = np.zeros((r, c), dtype=np.uint8)
    
    for x in range(r):
        for y in range(c):
            I[x,y] = img_gris[x,y]
            
    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_identidad_inverso():
    I = np.zeros((r, c), dtype=np.uint8)
    
    for x in range(r):
        for y in range(c):
            I[x,y] = 255 - img_gris[x,y]
            
    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_umbral():
    umbral = 127
    
    I = np.zeros((r, c), dtype=np.uint8)
    
    for x in range(r):
        for y in range(c):
            if img_gris[x, y] > umbral:
                I[x,y] = 255
            else:
                I[x,y] = 0
            
    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_umbral_intervalo():
    umbral_inferior = 100
    umbral_superior = 200
    
    I = np.zeros((r, c), dtype=np.uint8)

    for x in range(r):
        for y in range(c):
            if umbral_inferior <= img_gris[x, y] <= umbral_superior:
                I[x, y] = 255
            else:
                I[x, y] = 0

    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_umbral_intervalo_invertido():
    umbral_inferior = 100
    umbral_superior = 200
    
    I = np.zeros((r, c), dtype=np.uint8)

    for x in range(r):
        for y in range(c):
            if umbral_inferior <= img_gris[x, y] <= umbral_superior:
                I[x, y] = 0
            else:
                I[x, y] = 255

    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_umbral_escala_de_grises():
    umbral = np.mean(img_gris)

    I = np.zeros((r, c), dtype=np.uint8)

    for x in range(r):
        for y in range(c):
            if img_gris[x, y] > umbral:
                I[x, y] = 255
            else:
                I[x, y] = 0

    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
    
def operador_umbral_escala_de_grises_inverso():
    umbral = np.mean(img_gris)

    I = np.zeros((r, c), dtype=np.uint8)

    for x in range(r):
        for y in range(c):
            if img_gris[x, y] > umbral:
                I[x, y] = 0  # Invertir asignación de píxeles
            else:
                I[x, y] = 255

    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_extension():
    I = np.zeros((r, c), dtype=np.uint8)

    for x in range(r):
        for y in range(c):
            # Verificar límites para vecindad de 8 píxeles
            x1 = max(0, x - 1)
            x2 = min(r, x + 2)
            y1 = max(0, y - 1)
            y2 = min(c, y + 2)
            # Calcular el promedio de la vecindad
            promedio = np.mean(img_gris[x1:x2, y1:y2])
            # Asignar el valor del promedio al píxel actual
            I[x, y] = promedio
            
    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def operador_niveles_grises():
    niveles = 4

    # Calcular el paso para dividir los niveles de intensidad
    paso = 256 // niveles

    I = np.zeros((r, c), dtype=np.uint8)

    for x in range(r):
        for y in range(c):
            # Calcular el índice del rango de intensidad en el que se encuentra el valor del píxel
            indice = img_gris[x, y] // paso
            # Asignar un valor específico a los píxeles dentro de ese rango
            I[x, y] = indice * (256 // niveles)

    cv2.imshow('Imagen GS', img_gris)
    cv2.imshow('Imagen I', I)
    cv2.waitKey(0)
    pass

def transformacion_punto_a_punto():

    # Crear una imagen de destino para la transformación
    resultado = np.zeros((r, c), dtype=np.uint8)

    # Iterar sobre los píxeles de las dos imágenes y aplicar la transformación
    for x in range(r):
        for y in range(c):
            # Aplicar la transformación punto a punto
            resultado[x, y] = min(img_gris[x, y] + img_gris2[x, y], 255)  # Suma de intensidades, truncada a 255

    # Mostrar las imágenes original y transformada
    cv2.imshow('Imagen 1', img_gris)
    cv2.imshow('Imagen 2', img_gris2)
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def transformacion_punto_a_punto_con_adicion():
    if img_gris.shape != img_gris2.shape:
        print("Las dimensiones de las imágenes no son iguales.")
        return
    
    resultado = cv2.add(img_gris, img_gris2)

    cv2.imshow('Imagen 1', img_gris)
    cv2.imshow('Imagen 2', img_gris2)
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
    
def transformacion_punto_a_punto_con_sustraccion():
    if img_gris.shape != img_gris2.shape:
        print("Las dimensiones de las imágenes no son iguales.")
        return
    
    resultado = cv2.subtract(img_gris, img_gris2)

    cv2.imshow('Imagen 1', img_gris)
    cv2.imshow('Imagen 2', img_gris2)
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def salir():
    print("¡Hasta luego!")
    exit()

def mostrar_menu():
    print("")
    print("---- Menú ----")
    print("1. Operador identidad")
    print("2. Operador identidad inverso")
    print("3. Operador umbral")
    print("4. Operador umbral intervalo")
    print("5. Operador umbral intervalo invertido")
    print("6. Operador umbral en escala de grises")
    print("7. Operador umbral en escala de grises inverso")
    print("8. Operador extension")
    print("9. Operador niveles grises")
    print("10. Transformacion de 2 imagenes punto a punto")
    print("11. Transformacion de 2 imagenes punto a punto reduccion")
    print("12. Transformacion de 2 imagenes punto a punto sustraccion")
    print("13. Salir")
    print("")

    opcion = input("Selecciona una opción: ")

    return opcion

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            operador_identidad()
        elif opcion == '2':
            operador_identidad_inverso()
        elif opcion == '3':
            operador_umbral()
        elif opcion == '4':
            operador_umbral_intervalo()
        elif opcion == '5':
            operador_umbral_intervalo_invertido()
        elif opcion == '6':
            operador_umbral_escala_de_grises()
        elif opcion == '7':
            operador_umbral_escala_de_grises_inverso()
        elif opcion == '8':
            operador_extension()
        elif opcion == '9':
            operador_niveles_grises()
        elif opcion == '10':
            transformacion_punto_a_punto()
        elif opcion == '11':
            transformacion_punto_a_punto_con_adicion()
        elif opcion == '12':
            transformacion_punto_a_punto_con_sustraccion()
        elif opcion == '13':
            salir()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
