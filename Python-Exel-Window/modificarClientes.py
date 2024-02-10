#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
import pandas as pd
from openpyxl import load_workbook

# Inicializar 'ultimo_id' como una variable global
ultimo_id = 0

def contenido_alta_cliente():
    # Declarar 'ultimo_id' como global para poder modificarlo
    global ultimo_id

    def agregar_informacion():
        global ultimo_id  # Acceder a la variable en el ámbito global
        #nonlocal df          # Acceder al DataFrame

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
        guardar_datos()

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Información agregada a la base de datos.")
        ventana.destroy()

    def buscar_registro():
        id_a_buscar = askinteger("Buscar Registro", "Introduce el ID a buscar:")
        if id_a_buscar is not None:
            registro = df[df['id'] == id_a_buscar]
            if not registro.empty:
                entry_nombre.delete(0, tk.END)
                entry_nombre.insert(tk.END, registro['nombre'].values[0])
                entry_direccion.delete(0, tk.END)
                entry_direccion.insert(tk.END, registro['direccion'].values[0])
                entry_telefono.delete(0, tk.END)
                entry_telefono.insert(tk.END, registro['telefono'].values[0])
                entry_email.delete(0, tk.END)
                entry_email.insert(tk.END, registro['email'].values[0])
            else:
                messagebox.showerror("Error", f"No existe un registro con el ID {id_a_buscar}.")

    def guardar_datos():
        global df  # Acceder al DataFrame

        # Asegurar que haya al menos una fila de datos para evitar el error de 'At least one sheet must be visible'
        if df.empty:
            df = pd.DataFrame(columns=["id", "nombre", "direccion", "telefono", "email"])
            df.loc[0] = [0, '', '', '', '']

        # Guardar el DataFrame actualizado en el archivo Excel
        with pd.ExcelWriter("db.xlsx", engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, index=False)

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

    ventana.title("Gestión de Base de Datos")

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
    boton_agregar.grid(row=4, column=0, pady=10)

    # Botón para buscar un registro
    boton_buscar = tk.Button(ventana, text="Buscar Registro", command=buscar_registro)
    boton_buscar.grid(row=4, column=1, pady=10)

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
contenido_alta_cliente()
