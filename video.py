import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("No se pudo abrir la camara")

while True:
    ret, foto = cap.read()
    foto = cv2.flip(foto, 1)
    bn = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    # Aplicar la binarización inversa
    _, umbral_binario_invertido = cv2.threshold(bn, 128, 255, cv2.THRESH_BINARY_INV)

    # Mostrar la imagen binarizada
    cv2.imshow("Camara - Umbral Binario Invertido", umbral_binario_invertido)

    if not ret:
        break

    # cv2.imshow("camara ", bn)
    t = cv2.waitKey(1)
    if t == 27:
        break
cap.release()
cv2.destroyAllWindows()
