import numpy as np
import cv2
import matplotlib.pyplot as plt

# Lee la imagen en escala de grises
imagen = cv2.imread('./Imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE)
#imagen = cv2.imread('./Imagenes/lena.jpg', 0)
# Inicializa un vector para contar las ocurrencias de cada nivel de intensidad
vector = [0] * 256

for x in imagen:
    for pixel in x:
        vector[pixel] += 1

# Imprime la cantidad de cada nivel de intensidad
for i in range(256):
    cantidad = vector[i]
    print(f"{i}:", cantidad)
    
print("----------------------------------------------------------")
# Calcula la suma total de los recuentos de ocurrencias
total_ocurrencias = sum(vector)

# Calcula la probabilidad de concurrencia para cada nivel de intensidad
probabilidades = []
for ocurrencias in vector:
    probabilidad = ocurrencias / total_ocurrencias
    # agregar un elemento al final de una lista existente
    probabilidades.append(probabilidad)

# Imprime la cantidad y la probabilidad de cada nivel de intensidad
for i in range(256):
    cantidad = vector[i]
    probabilidad = probabilidades[i]
    print(f"Nivel {i}: Cantidad: {cantidad}, Probabilidad: {probabilidad}")

# Calcular la probabilidad acumulativa
probabilidad_acumulativa = [probabilidades[0]]
for i in range(1, 256):
    print(probabilidad_acumulativa.append(probabilidad_acumulativa[i-1] + probabilidades[i]))

# Imprimir la probabilidad acumulativa
print("Probabilidad acumulativa:")
for i in range(256):
    print(f"Nivel {i}: {probabilidad_acumulativa[i]}")

# Calcular la ecualización
ecualizacion = [int(round(p * 255)) for p in probabilidad_acumulativa]

# Imprimir la ecualización
print("\nEcualización:")
for i in range(256):
    print(f"Nivel {i}: {ecualizacion[i]}")

# Muestra la imagen original
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crea la gráfica del histograma de intensidades
plt.figure(figsize=(10, 6))
# Utiliza un mapa de colores para el color de las barras
plt.bar(range(256), vector, color=plt.cm.viridis(np.linspace(0, 1, 256)))
plt.title("Grafíca del Vector")
plt.xlabel("Valor de Intensidad")
plt.ylabel("Cantidad de Píxeles")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
