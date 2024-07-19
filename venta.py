import tkinter as tk


def abrir_ventana():
    ventana = tk.Toplevel(root)
    ventana.title("Nueva Ventana")
    ventana.geometry("600x400")
    label = tk.Label(ventana, text="¡Bienvenido a la nueva ventana!")
    label.pack(pady=20)
    boton_cerrar = tk.Button(
        ventana, text="Cerrar ventana", command=ventana.destroy)
    boton_cerrar.pack(pady=10)


def salir():
    root.destroy()


root = tk.Tk()
root.title("Menú")

# Etiqueta de título
titulo = tk.Label(root, text="Menú")
titulo.pack(pady=10)

# Botón para abrir otra ventana
boton_abrir = tk.Button(
    root, text="1: Abrir otra ventana", command=abrir_ventana)
boton_abrir.pack(pady=5)

# Botón para salir
boton_salir = tk.Button(root, text="2: Salir", command=salir)
boton_salir.pack(pady=5)

root.mainloop()
