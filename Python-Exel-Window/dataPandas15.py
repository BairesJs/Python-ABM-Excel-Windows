#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import load_workbook

# Función para agregar información a la base de datos (archivo Excel)
def agregar_informacion():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    email = entry_email.get()

    # Leer el archivo Excel existente o crearlo si no existe
    try:
        df = pd.read_excel("db.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["nombre", "dirección", "telefono", "email"])

    # Agregar una nueva fila con la información ingresada
    nueva_fila = pd.DataFrame({"nombre": [nombre], "direccion": [direccion],
                               "telefono": [telefono], "email": [email]})
    df = pd.concat([df, nueva_fila], ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo Excel
    with pd.ExcelWriter("db.xlsx", engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, index=False)

    # Mostrar un mensaje de éxito
    messagebox.showinfo("Éxito", "Información agregada a la base de datos.")

# Crear la ventana principal
ventana = tk.Tk()
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

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
