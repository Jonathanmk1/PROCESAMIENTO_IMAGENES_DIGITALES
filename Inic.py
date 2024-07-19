from PyQt6 import QtCore, QtGui, QtWidgets
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 49, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(160, 20, 411, 511))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.  = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conectar el botón a la función de umbralizar imagen|
        self.pushButton.clicked.connect(self.umbralizar_imagen)

        # Mostrar la imagen original al iniciar la aplicación
        self.mostrar_imagen_original()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "APLICAR UMBRAL"))
        self.pushButton.setText(_translate("MainWindow", "UMBRALIZAR"))

    def mostrar_imagen_original(self):
        # Cargar la imagen original
        pixmap = QtGui.QPixmap("./Imagenes/lena.jpg")
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        self.graphicsView.setScene(scene)

    def umbralizar_imagen(self):
        # Cargar la imagen
        image = cv2.imread("./Imagenes/lena.jpg", cv2.IMREAD_GRAYSCALE)

        # Aplicar umbralización
        _, umbralizada = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

        # Guardar la imagen umbralizada temporalmente
        cv2.imwrite("./Imagenes/umbralizada.png", umbralizada)

        # Mostrar la imagen umbralizada en QGraphicsView
        pixmap = QtGui.QPixmap("./Imagenes/umbralizada.png")
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        self.graphicsView.setScene(scene)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
