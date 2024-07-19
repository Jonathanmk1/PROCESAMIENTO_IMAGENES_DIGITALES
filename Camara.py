import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Segmentación de Color")

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise IOError("No se pudo abrir la cámara.")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.color_label = ttk.Label(self.frame, text="Selecciona un color:")
        self.color_label.grid(row=0, column=0, padx=5, pady=5)

        self.colors = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Morado"]
        self.color_var = tk.StringVar()
        self.color_var.set(self.colors[0])

        self.color_menu = ttk.OptionMenu(self.frame, self.color_var, *self.colors)
        self.color_menu.grid(row=0, column=1, padx=5, pady=5)

        self.quit_button = ttk.Button(self.frame, text="Salir", command=self.quit)
        self.quit_button.grid(row=0, column=2, padx=5, pady=5)

        self.camera_label = ttk.Label(self.frame)
        self.camera_label.grid(row=1, column=0, columnspan=3)

        self.update()

    def update(self):
        ret, foto = self.cap.read()

        if ret:
            img = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)

            # Convertir imagen a formato HSV
            hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

            # Rangos de colores para la segmentación
            colors_range = {
                "Rojo": ([0, 100, 100], [10, 255, 255]),
                "Verde": ([45, 100, 100], [75, 255, 255]),
                "Azul": ([90, 100, 100], [130, 255, 255]),
                "Amarillo": ([20, 100, 100], [30, 255, 255]),
                "Naranja": ([10, 100, 100], [25, 255, 255]),
                "Morado": ([130, 100, 100], [160, 255, 255])
            }

            selected_color = self.color_var.get()
            lower_range = np.array(colors_range[selected_color][0])
            upper_range = np.array(colors_range[selected_color][1])

            # Filtrar colores dentro del rango
            mask = cv2.inRange(hsv_img, lower_range, upper_range)
            result = cv2.bitwise_and(img, img, mask=mask)

            imgtk = ImageTk.PhotoImage(image=Image.fromarray(result))

            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)

        self.master.after(10, self.update)

    def quit(self):
        self.cap.release()
        self.master.destroy()

def main():
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
