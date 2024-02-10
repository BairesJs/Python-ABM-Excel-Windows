#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import load_workbook

def contenido_alta_cliente():
    # Variable para almacenar el último ID utilizado
    ultimo_id = 0

    # Función para agregar información a la base de datos (archivo Excel)
    def agregar_informacion():
        nonlocal ultimo_id  # Acceder a la variable en el ámbito superior
        nonlocal df          # Acceder al DataFrame

        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        email = entry_email.get()

        # Incrementar el ID
        ultimo_id += 1

        # Crear una nueva fila con la información ingresada
        nueva_fila = pd.DataFrame({"id": [ultimo_id], "nombre": [nombre], "direccion": [direccion],
                                "telefono": [telefono], "email": [email]})

        # Agregar la nueva fila al DataFrame
        df = pd.concat([df, nueva_fila], ignore_index=True)

        # Guardar el DataFrame actualizado en el archivo Excel
        with pd.ExcelWriter("db.xlsx", engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, index=False)

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Información agregada a la base de datos.")
        ventana.destroy()

    # Crear la ventana principal
    ventana = tk.Tk()
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Definir el tamaño y posición de la ventana
    ancho_ventana = 400
    alto_ventana = 300

    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Bloquear la interacción con la ventana anterior
    

    ventana.title("Agregar Información a la Base de Datos")

    # Crear etiquetas y entradas para la información
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Dirección:").grid(row=1, column=0, padx=10, pady=5)
    entry_direccion = tk.Entry(ventana)
    entry_direccion.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)
    entry_telefono = tk.Entry(ventana)
    entry_telefono.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Email:").grid(row=3, column=0, padx=10, pady=5)
    entry_email = tk.Entry(ventana)
    entry_email.grid(row=3, column=1, padx=10, pady=5)

    # Botón para agregar información
    boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_informacion)
    boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)
    

    # Leer el archivo Excel existente o crearlo si no existe
    try:
        df = pd.read_excel("db.xlsx")
        # Obtener el último ID utilizado
        if not df.empty:
            ultimo_id = df['id'].max()
    except FileNotFoundError:
        df = pd.DataFrame(columns=["id", "nombre", "direccion", "telefono", "email"])
        ultimo_id = 0

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()

# Llamar a la función para ejecutar el contenido

