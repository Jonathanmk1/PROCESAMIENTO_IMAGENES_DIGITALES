import cv2
import numpy as np

imgColor = cv2.imread("./Imagenes/coins.png")
img = cv2.cvtColor(imgColor, cv2.COLOR_BGR2GRAY)

_, img2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

img3 = cv2.dilate(img2, kernel, iterations=1)
img4 = cv2.erode(img2, kernel, iterations=1)

# Aplicar Apertura
img9 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)

# Aplicar cierre
img10 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

cont, _ = cv2.findContours(img10, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
numcont = len(cont)
print("detecto :", numcont, "contornos")

total_dinero = 0
monedas_1 = 0
monedas_2 = 0

for i in range(numcont):
    c = cont[i]
    M = cv2.moments(c)
    area = cv2.contourArea(c)
    if area > 1000:
        if area < 2000:
            monedas_1 += 1
            total_dinero += 1
        else:
            monedas_2 += 1
            total_dinero += 2

print("total de monedas:", numcont)
print("total de monedas de $1:", monedas_1)
print("total de monedas de $2:", monedas_2)
print("total de dinero: $", total_dinero)

imgs = np.hstack((img, img2, img3))
imgs2 = np.hstack((img4, img9, img10))

# Apilar imágenes verticalmente
Imagenes = np.vstack((imgs, imgs2))

cv2.namedWindow("Escala de grises/Binaria/Dilate/Erocion/Apertura/Cierre", cv2.WINDOW_NORMAL)
cv2.imshow('Escala de grises/Binaria/Dilate/Erocion/Apertura/Cierre', Imagenes)
cv2.imshow("imagenColor", imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()
