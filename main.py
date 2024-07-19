import sys
import cv2
import tkinter as tk

import numpy as np
from PyQt6 import QtWidgets, QtGui, QtCore
from Principal import Ui_uno  # Importar la clase generada para la ventana principal
from CargarImagen import Ui_DOS  # Importar la clase generada para la segunda ventana
from EditarCargada import Ui_Form  # Importar la clase generada para la nueva ventana
from PyQt6.QtWidgets import QFileDialog
from Camara import CameraApp


class MainWindow(QtWidgets.QMainWindow, Ui_uno):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.EditarFoto.clicked.connect(self.show_edit_window)  # Conectar el botón con la función para mostrar la segunda ventana
        
    def show_edit_window(self):
        self.edit_window = EditWindow(self)
        self.edit_window.show()
        self.hide()  # Ocultar la ventana principal

class EditWindow(QtWidgets.QWidget, Ui_DOS):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.image_path = None  # Variable para almacenar la ruta de la imagen temporal
        self.VolverVentanaPrincipal.clicked.connect(self.return_to_main)  # Conectar el botón "Volver" para cerrar la segunda ventana
        self.CargarImagen.clicked.connect(self.load_image)  # Conectar el botón "Cargar Imagen" para cargar la imagen
        self.IraEditarCargada.clicked.connect(self.show_image_edit_window)  # Conectar el botón "Aceptar" para mostrar la nueva ventana
        self.Camara.clicked.connect(self.open_camera)

    def open_camera(self):
        root = tk.Tk()
        app = CameraApp(root)
        root.mainloop()

    def load_image(self):
        # Abrir un cuadro de diálogo para seleccionar una imagen
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Seleccionar Imagen", "", "Archivos de Imagen (*.png *.jpg *.bmp);;Todos los archivos (*)")
        if file_name:
            # Guardar la imagen temporalmente
            image = cv2.imread(file_name)
            temp_image_path = "./Imagenes/imagen.png"
            cv2.imwrite(temp_image_path, image)
            self.image_path = temp_image_path  # Almacenar la ruta de la imagen temporal
            # Cargar la imagen usando QPixmap
            pixmap = QtGui.QPixmap(temp_image_path)
            # Crear una escena y agregar el pixmap a la escena
            scene = QtWidgets.QGraphicsScene()
            pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(pixmap_item)
            # Establecer la escena en el QGraphicsView
            self.Previsualizacion.setScene(scene)
            self.Previsualizacion.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def show_image_edit_window(self):
        if self.image_path:
            self.image_edit_window = ImageEditWindow(self.image_path, self)
            self.image_edit_window.show()
            self.hide()  # Ocultar la ventana actual

    def return_to_main(self):
        self.main_window.show()  # Mostrar la ventana principal
        self.close()  # Cerrar la ventana actual

class ImageEditWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, image_path, edit_window):
        super().__init__()
        self.setupUi(self)
        self.edit_window = edit_window
        self.image_path = image_path
        self.original_image2 = cv2.imread(image_path, cv2.IMREAD_COLOR)

        self.original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.load_image(image_path)
        self.GuardarIMG1.clicked.connect(self.save_image)
        self.is_inverted = False  # Variable de estado para rastrear si el umbral está invertido
        self.is_double_inverted = False  # Variable de estado para rastrear si el umbral doble está invertido
        self.VolveraVentanaCargar.clicked.connect(self.return_to_edit_window)  # Conectar el botón "Salir" para cerrar la ventana
        self.pushButton.clicked.connect(self.convert_to_grayscale)  # Conectar el botón "Escala Gris" para convertir la imagen
        self.pushButton_2.clicked.connect(self.convert_to_negative)  # Conectar el botón "Negativa" para convertir la imagen
        self.pushButton_3.clicked.connect(self.toggle_invert_threshold)  # Conectar el botón "Invertir" para invertir el umbral
        self.AplicarUmbral.clicked.connect(self.apply_threshold)  # Conectar el botón "Aplicar" al umbral
        self.pushButton_4.clicked.connect(self.apply_double_threshold)
        self.pushButton_5.clicked.connect(self.toggle_invert_double_threshold)
        self.AplicarPuntoaPunto.clicked.connect(self.apply_point_to_point_transform)
        self.AplicarAdicion.clicked.connect(self.apply_addition_transform)
        self.AplicarSustraccion.clicked.connect(self.apply_subtraction_transform)
        self.AplicarMascara.clicked.connect(self.apply_mask)
        self.trasladoejex.valueChanged.connect(self.apply_translation)
        self.trasladoejey.valueChanged.connect(self.apply_translation)
        self.AplicarTraslacion.clicked.connect(self.apply_translation)
        self.AplicarEsacalado.clicked.connect(self.apply_scaling)
        self.horizontalSlider.valueChanged.connect(self.update_rotation_label)
        self.AplicarRotacion.clicked.connect(self.apply_rotation)
        self.label_rotacion = QtWidgets.QLabel(self)  # Crear una etiqueta para mostrar el ángulo de rotación
        self.label_rotacion.setGeometry(QtCore.QRect(640, 420, 160, 22))
        self.label_rotacion.setObjectName("label_rotacion")
        self.Desenfoque.clicked.connect(self.apply_blur)
        self.gausiano.clicked.connect(self.apply_gaussian_blur)
        self.mediana.clicked.connect(self.apply_median_blur)
        self.Bilateral.clicked.connect(self.apply_bilateral_filter)
        self.DOSD.clicked.connect(self.apply_2D_filter)
        self.dilatacion.clicked.connect(self.apply_dilation)
        self.erosion.clicked.connect(self.apply_erosion)
        self.apertura.clicked.connect(self.apply_opening)
        self.cierre.clicked.connect(self.apply_closing)
        self.visualizarcontornos.clicked.connect(self.visualize_contours)
        self.contarcontornos.clicked.connect(self.count_contours)
        self.truncar.clicked.connect(self.apply_truncation)
        self.Ajustaracero.clicked.connect(self.adjust_to_zero)
        self.Ajustaraceroinv.clicked.connect(self.adjust_to_zero_inv)
        self.otsu.clicked.connect(self.apply_otsu)
        self.asaptativa.clicked.connect(self.apply_adaptive_threshold)
        self.rojo.clicked.connect(self.segmentar_rojo)
        self.azul.clicked.connect(self.segmentar_azul)
        self.verde.clicked.connect(self.segmentar_verde)
        self.violeta.clicked.connect(self.segmentar_violeta)
        self.Amarillo.clicked.connect(self.segmentar_amarillo)
        self.umbral1.setRange(0, 256)
        self.umbral1.valueChanged.connect(self.apply_threshold)  # Conectar el QSlider a la función de umbral
        self.label_invert_status = QtWidgets.QLabel(self)  # Crear una etiqueta para mostrar el estado de inversión
        self.label_invert_status.setGeometry(QtCore.QRect(230, 160, 150, 24))
        self.label_invert_status.setText("Umbral Normal")  # Texto inicial de la etiqueta
        self.label_num_contours = QtWidgets.QLabel(self)
        self.label_num_contours.setGeometry(QtCore.QRect(630, 480, 200, 24))
        self.label_num_contours.setObjectName("label_num_contours")

        # Configurar los QSliders para el umbral doble
        self.umbral2.setRange(0, 256)
        self.umbral3.setRange(0, 256)
        self.umbral2.valueChanged.connect(self.apply_double_threshold)  # Conectar el QSlider al umbral doble
        self.umbral3.valueChanged.connect(self.apply_double_threshold)  # Conectar el QSlider al umbral doble
        self.AplicarUmbralDoble.clicked.connect(self.apply_double_threshold)  # Conectar el botón al umbral doble
        self.InvertirUmbralDoble.clicked.connect(self.toggle_invert_double_threshold)  # Conectar el botón para invertir el umbral doble

    def load_image(self, image_path):
        self.display_image(image_path)

    def display_image(self, image_path):
        pixmap = QtGui.QPixmap(image_path)
        pixmap = pixmap.scaled(self.Previsualizacion2.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        self.Previsualizacion2.setScene(scene)

    def convert_to_grayscale(self):
        gray_image = self.original_image
        temp_gray_image_path = "./Imagenes/imagen_grayscale.png"
        cv2.imwrite(temp_gray_image_path, gray_image)
        self.display_image(temp_gray_image_path)

    def convert_to_negative(self):
        gray_image = self.original_image
        negative_image = cv2.bitwise_not(gray_image)
        temp_negative_image_path = "./Imagenes/imagen_negative.png"
        cv2.imwrite(temp_negative_image_path, negative_image)
        self.display_image(temp_negative_image_path)

    def apply_threshold(self):
        threshold_value = self.umbral1.value()
        if self.is_inverted:
            _, threshold_image = cv2.threshold(self.original_image, threshold_value, 255, cv2.THRESH_BINARY_INV)
        else:
            _, threshold_image = cv2.threshold(self.original_image, threshold_value, 255, cv2.THRESH_BINARY)
        temp_threshold_image_path = "./Imagenes/imagen_threshold.png"
        cv2.imwrite(temp_threshold_image_path, threshold_image)
        self.display_image(temp_threshold_image_path)

    def toggle_invert_threshold(self):
        self.is_inverted = not self.is_inverted
        self.apply_threshold()  # Reaplicar el umbral con el nuevo estado de inversión
        if self.is_inverted:
            self.label_invert_status.setText("Umbral Invertido")
        else:
            self.label_invert_status.setText("Umbral Normal")

    def apply_double_threshold(self):
        threshold1 = self.umbral2.value()
        threshold2 = self.umbral3.value()
        if threshold1 > threshold2:
            threshold1, threshold2 = threshold2, threshold1  # Asegurarse de que threshold1 sea menor que threshold2
        if self.is_double_inverted:
            _, lower_thresh = cv2.threshold(self.original_image, threshold1, 255, cv2.THRESH_BINARY_INV)
            _, upper_thresh = cv2.threshold(self.original_image, threshold2, 255, cv2.THRESH_BINARY_INV)
            double_threshold_image = cv2.bitwise_or(lower_thresh, upper_thresh)
        else:
            _, lower_thresh = cv2.threshold(self.original_image, threshold1, 255, cv2.THRESH_BINARY)
            _, upper_thresh = cv2.threshold(self.original_image, threshold2, 255, cv2.THRESH_BINARY_INV)
            double_threshold_image = cv2.bitwise_and(lower_thresh, upper_thresh)
        temp_double_threshold_image_path = "./Imagenes/imagen_double_threshold.png"
        cv2.imwrite(temp_double_threshold_image_path, double_threshold_image)
        self.display_image(temp_double_threshold_image_path)

    def toggle_invert_double_threshold(self):
        self.is_double_inverted = not self.is_double_inverted
        self.apply_double_threshold()  # Reaplicar el umbral doble con el nuevo estado de inversión
        if self.is_double_inverted:
            self.label_invert_status.setText("Umbral Doble Invertido")
        else:
            self.label_invert_status.setText("Umbral Doble Normal")

    def apply_point_to_point_transform(self):
        transformacion = np.zeros_like(self.original_image, dtype=np.uint8)
        negativo = 255 - self.original_image

        for x in range(self.original_image.shape[0]):
            for y in range(self.original_image.shape[1]):
                transformacion[x,y] = self.original_image[x,y] - negativo[x,y]
                if transformacion[x,y] > 255:
                    transformacion[x,y] = 255
                if transformacion[x,y] < 0:
                    transformacion[x,y] = 0

        temp_transformacion_image_path = "./Imagenes/imagen_transformacion.png"
        cv2.imwrite(temp_transformacion_image_path, transformacion)
        self.display_image(temp_transformacion_image_path)

    def apply_addition_transform(self):
        transformacionad = np.zeros_like(self.original_image, dtype=np.uint8)
        negativo = 255 - self.original_image

        for x in range(self.original_image.shape[0]):
            for y in range(self.original_image.shape[1]):
                transformacionad[x, y] = round((self.original_image[x, y] + negativo[x, y]) / 2)
                if transformacionad[x, y] > 255:
                    transformacionad[x, y] = 255
                elif transformacionad[x, y] < 0:
                    transformacionad[x, y] = 0

        temp_transformacionad_image_path = "./Imagenes/imagen_transformacion_adicion.png"
        cv2.imwrite(temp_transformacionad_image_path, transformacionad)
        self.display_image(temp_transformacionad_image_path)

    def apply_subtraction_transform(self):
        transformacionsus = np.zeros_like(self.original_image, dtype=np.uint8)
        negativo = 255 - self.original_image

        for x in range(self.original_image.shape[0]):
            for y in range(self.original_image.shape[1]):
                transformacionsus[x, y] = round(2 * (self.original_image[x, y] - negativo[x, y]))
                if transformacionsus[x, y] > 255:
                    transformacionsus[x, y] = 255
                elif transformacionsus[x, y] < 0:
                    transformacionsus[x, y] = 0

        temp_transformacionsus_image_path = "./Imagenes/imagen_transformacion_sustraccion.png"
        cv2.imwrite(temp_transformacionsus_image_path, transformacionsus)
        self.display_image(temp_transformacionsus_image_path)

    def apply_mask(self):
        alto, ancho = self.original_image.shape

        mascara = np.array([[1, 2, 1],
                            [0, 0, 0],
                            [-1, -2, -1]])

        convolucion = np.zeros_like(self.original_image, dtype=np.uint8)

        for y in range(1, alto - 1):
            for x in range(1, ancho - 1):
                region = self.original_image[y - 1:y + 2, x - 1:x + 2]
                valor_pixel = int(np.sum(region * mascara))
                valor_pixel = max(0, min(valor_pixel, 255))
                convolucion[y, x] = valor_pixel

        temp_convolucion_image_path = "./Imagenes/imagen_con_mascara.png"
        cv2.imwrite(temp_convolucion_image_path, convolucion)
        self.display_image(temp_convolucion_image_path)

    def apply_translation(self):
        tx = self.trasladoejex.value()
        ty = self.trasladoejey.value()
        filas, columnas = self.original_image.shape
        imagen_traslada = np.zeros((filas + abs(ty), columnas + abs(tx)), dtype=np.uint8)
        
        for i in range(filas):
            for j in range(columnas):
                if ty >= 0:
                    if tx >= 0:
                        imagen_traslada[i + ty, j + tx] = self.original_image[i, j]
                    else:
                        imagen_traslada[i + ty, j] = self.original_image[i, j - abs(tx)]
                else:
                    if tx >= 0:
                        imagen_traslada[i, j + tx] = self.original_image[i - abs(ty), j]
                    else:
                        imagen_traslada[i, j] = self.original_image[i - abs(ty), j - abs(tx)]

        temp_imagen_traslada_path = "./Imagenes/imagen_traslada.png"
        cv2.imwrite(temp_imagen_traslada_path, imagen_traslada)
        self.display_image(temp_imagen_traslada_path)

    def apply_scaling(self):
        escala_x = self.trasladoejex.value() / 100.0  # Ajustar la escala para que sea un factor entre 0 y 1
        escala_y = self.trasladoejey.value() / 100.0  # Ajustar la escala para que sea un factor entre 0 y 1
        filas, columnas = self.original_image.shape
        filas1 = int(filas * escala_x)
        columnas1 = int(columnas * escala_y)
        imagen_escalada = cv2.resize(self.original_image, (columnas1, filas1), interpolation=cv2.INTER_LINEAR)

        temp_imagen_escalada_path = "./Imagenes/imagen_escalada.png"
        cv2.imwrite(temp_imagen_escalada_path, imagen_escalada)
        self.display_image(temp_imagen_escalada_path)

    def update_rotation_label(self, value):
        self.label_rotacion.setText(f"Ángulo de rotación: {value}°")

    def apply_rotation(self):
        angulo = self.horizontalSlider.value()
        angulo_rad = np.deg2rad(angulo)
        filas, columnas = self.original_image.shape
        imagen_rotada = np.zeros_like(self.original_image, dtype=np.uint8)

        cx, cy = filas // 2, columnas // 2

        for i in range(filas):
            for j in range(columnas):

                x = i - cx
                y = j - cy

                x1 = round(x * np.cos(angulo_rad) - y * np.sin(angulo_rad))
                y1 = round(x * np.sin(angulo_rad) + y * np.cos(angulo_rad))

                x1 += cx
                y1 += cy

                if 0 <= x1 < filas and 0 <= y1 < columnas:
                    imagen_rotada[i, j] = self.original_image[x1, y1]

        temp_imagen_rotada_path = "./Imagenes/imagen_rotada.png"
        cv2.imwrite(temp_imagen_rotada_path, imagen_rotada)
        self.display_image(temp_imagen_rotada_path)

    def apply_blur(self):
        img_blur = cv2.blur(self.original_image, (7, 7))
        temp_image_path = "./Imagenes/imagen_blur.png"
        cv2.imwrite(temp_image_path, img_blur)
        self.display_image(temp_image_path)

    def apply_gaussian_blur(self):
        img_gaussian_blur = cv2.GaussianBlur(self.original_image, (7, 7), 3)
        temp_image_path = "./Imagenes/imagen_gaussian_blur.png"
        cv2.imwrite(temp_image_path, img_gaussian_blur)
        self.display_image(temp_image_path)

    def apply_median_blur(self):
        img_median_blur = cv2.medianBlur(self.original_image, 7)
        temp_image_path = "./Imagenes/imagen_median_blur.png"
        cv2.imwrite(temp_image_path, img_median_blur)
        self.display_image(temp_image_path)

    def apply_bilateral_filter(self):
        img_bilateral_filter = cv2.bilateralFilter(self.original_image, 9, 75, 75)
        temp_image_path = "./Imagenes/imagen_bilateral_filter.png"
        cv2.imwrite(temp_image_path, img_bilateral_filter)
        self.display_image(temp_image_path)

    def apply_2D_filter(self):
        # Debes definir 'filtro' antes de utilizarlo
        filtro = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], np.float32)
        img_2D_filter = cv2.filter2D(self.original_image, -1, filtro)
        temp_image_path = "./Imagenes/imagen_2D_filter.png"
        cv2.imwrite(temp_image_path, img_2D_filter)
        self.display_image(temp_image_path)

    def apply_dilation(self):
        filtro = np.ones((5,5),np.uint8)
        img_dilation = cv2.dilate(self.original_image, filtro, iterations=1)
        temp_image_path = "./Imagenes/imagen_dilation.png"
        cv2.imwrite(temp_image_path, img_dilation)
        self.display_image(temp_image_path)

    def apply_erosion(self):
        filtro = np.ones((5,5),np.uint8)
        img_erosion = cv2.erode(self.original_image, filtro, iterations=1)
        temp_image_path = "./Imagenes/imagen_erosion.png"
        cv2.imwrite(temp_image_path, img_erosion)
        self.display_image(temp_image_path)

    def apply_opening(self):
        filtro = np.ones((5,5),np.uint8)
        img_opening = cv2.morphologyEx(self.original_image, cv2.MORPH_OPEN, filtro)
        temp_image_path = "./Imagenes/imagen_opening.png"
        cv2.imwrite(temp_image_path, img_opening)
        self.display_image(temp_image_path)

    def apply_closing(self):
        filtro = np.ones((5,5),np.uint8)
        img_closing = cv2.morphologyEx(self.original_image, cv2.MORPH_CLOSE, filtro)
        temp_image_path = "./Imagenes/imagen_closing.png"
        cv2.imwrite(temp_image_path, img_closing)
        self.display_image(temp_image_path)

    def visualize_contours(self):
        cont, _ = cv2.findContours(self.original_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img_contours = self.original_image.copy()  # Copiar la imagen original para no modificarla
        img_contours = cv2.drawContours(img_contours, cont, -1, (0, 0, 255), 3)  # Dibujar contornos en rojo

        temp_image_path = "./Imagenes/imagen_contours.png"
        cv2.imwrite(temp_image_path, img_contours)
        self.display_image(temp_image_path)

    def count_contours(self):
        cont, _ = cv2.findContours(self.original_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        numcont = len(cont)
        self.label_num_contours.setText("Número de contornos: " + str(numcont))

    def apply_truncation(self):
        _, q2 = cv2.threshold(self.original_image, 90, 90, cv2.THRESH_TRUNC)
        temp_image_path = "./Imagenes/imagen_truncation.png"
        cv2.imwrite(temp_image_path, q2)
        self.display_image(temp_image_path)

    def adjust_to_zero(self):
        _, q2 = cv2.threshold(self.original_image, 90, 255, cv2.THRESH_TOZERO)
        temp_image_path = "./Imagenes/imagen_adjust_to_zero.png"
        cv2.imwrite(temp_image_path, q2)
        self.display_image(temp_image_path)

    def adjust_to_zero_inv(self):
        _, q2 = cv2.threshold(self.original_image, 90, 255, cv2.THRESH_TOZERO_INV)
        temp_image_path = "./Imagenes/imagen_adjust_to_zero_inv.png"
        cv2.imwrite(temp_image_path, q2)
        self.display_image(temp_image_path)

    def apply_otsu(self):
        _, q2 = cv2.threshold(self.original_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        temp_image_path = "./Imagenes/imagen_otsu.png"
        cv2.imwrite(temp_image_path, q2)
        self.display_image(temp_image_path)

    def apply_adaptive_threshold(self):
        q2 = cv2.adaptiveThreshold(self.original_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        temp_image_path = "./Imagenes/imagen_adaptive_threshold.png"
        cv2.imwrite(temp_image_path, q2)
        self.display_image(temp_image_path)

    def segmentar_rojo(self):
        # Convertir la imagen a espacio de color HSV
        hsv_image = cv2.cvtColor(self.original_image2, cv2.COLOR_BGR2HSV)

        # Definir el rango de color rojo en HSV
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        # Aplicar la máscara para segmentar el color rojo
        mask = cv2.inRange(hsv_image, lower_red, upper_red)
        segmented_image = cv2.bitwise_and(self.original_image2, self.original_image2, mask=mask)

        # Guardar y mostrar la imagen segmentada
        temp_image_path = "./Imagenes/imagen_segmentada_rojo.png"
        cv2.imwrite(temp_image_path, segmented_image)
        self.display_image(temp_image_path)

    def segmentar_azul(self):
        # Convertir la imagen a espacio de color HSV
        hsv_image = cv2.cvtColor(self.original_image2, cv2.COLOR_BGR2HSV)

        # Definir el rango de color azul en HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # Aplicar la máscara para segmentar el color azul
        mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        segmented_image = cv2.bitwise_and(self.original_image2, self.original_image2, mask=mask)

        # Guardar y mostrar la imagen segmentada
        temp_image_path = "./Imagenes/imagen_segmentada_azul.png"
        cv2.imwrite(temp_image_path, segmented_image)
        self.display_image(temp_image_path)

    def segmentar_verde(self):
        # Convertir la imagen a espacio de color HSV
        hsv_image = cv2.cvtColor(self.original_image2, cv2.COLOR_BGR2HSV)

        # Definir el rango de color verde en HSV
        lower_green = np.array([36, 25, 25])
        upper_green = np.array([70, 255, 255])

        # Aplicar la máscara para segmentar el color verde
        mask = cv2.inRange(hsv_image, lower_green, upper_green)
        segmented_image = cv2.bitwise_and(self.original_image2, self.original_image2, mask=mask)

        # Guardar y mostrar la imagen segmentada
        temp_image_path = "./Imagenes/imagen_segmentada_verde.png"
        cv2.imwrite(temp_image_path, segmented_image)
        self.display_image(temp_image_path)

    def segmentar_violeta(self):
        # Convertir la imagen a espacio de color HSV
        hsv_image = cv2.cvtColor(self.original_image2, cv2.COLOR_BGR2HSV)

        # Definir el rango de color violeta en HSV
        lower_violet = np.array([120, 50, 50])
        upper_violet = np.array([140, 255, 255])

        # Aplicar la máscara para segmentar el color violeta
        mask = cv2.inRange(hsv_image, lower_violet, upper_violet)
        segmented_image = cv2.bitwise_and(self.original_image2, self.original_image2, mask=mask)

        # Guardar y mostrar la imagen segmentada
        temp_image_path = "./Imagenes/imagen_segmentada_violeta.png"
        cv2.imwrite(temp_image_path, segmented_image)
        self.display_image(temp_image_path)

    def segmentar_amarillo(self):
        # Convertir la imagen a espacio de color HSV
        hsv_image = cv2.cvtColor(self.original_image2, cv2.COLOR_BGR2HSV)

        # Definir el rango de color amarillo en HSV
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        # Aplicar la máscara para segmentar el color amarillo
        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
        segmented_image = cv2.bitwise_and(self.original_image2, self.original_image2, mask=mask)

        # Guardar y mostrar la imagen segmentada
        temp_image_path = "./Imagenes/imagen_segmentada_amarillo.png"
        cv2.imwrite(temp_image_path, segmented_image)
        self.display_image(temp_image_path)



    def save_image(self):
        # Obtener la ruta de destino del archivo usando el diálogo de guardar archivo
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Guardar Imagen", "", "Archivos de imagen (*.png *.jpg *.bmp);;Todos los archivos (*)")
        
        if file_path:  # Si se selecciona una ruta de archivo válida
            # Guardar la imagen actualmente visualizada en el QGraphicsView
            pixmap = self.Previsualizacion2.scene().items()[0].pixmap()
            pixmap.save(file_path)

    def return_to_edit_window(self):
        self.edit_window.show()  # Mostrar la ventana de edición de imagen
        self.close()  # Cerrar la ventana actual

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())