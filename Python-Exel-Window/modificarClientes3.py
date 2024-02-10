#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
import pandas as pd

# Inicializar 'ultimo_id' como una variable global
ultimo_id = 0
df = pd.DataFrame(columns=["id", "nombre", "direccion", "telefono", "email"])

# Variable para almacenar el ID del registro a modificar
id_a_modificar = None

def contenido_editar_cliente():
    # Declarar 'ultimo_id' y 'df' como globales para poder modificarlos
    global ultimo_id
    global df

    def agregar_informacion():
        global df
        global id_a_modificar

        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        email = entry_email.get()

        if id_a_modificar is not None:
            # Actualizar el registro en el DataFrame
            df.loc[id_a_modificar, 'nombre'] = nombre
            df.loc[id_a_modificar, 'direccion'] = direccion
            df.loc[id_a_modificar, 'telefono'] = telefono
            df.loc[id_a_modificar, 'email'] = email

            # Guardar el DataFrame actualizado en el archivo Excel
            df.to_excel("db.xlsx", index=False)

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Información modificada en la base de datos.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se ha seleccionado ningún registro para modificar.")

    def buscar_registro():
        global id_a_modificar
        id_a_modificar = askinteger("Modificar Registro", "Introduce el ID a modificar:")
        if id_a_modificar is not None:
            registro = df[df['id'] == id_a_modificar]
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
                messagebox.showerror("Error", f"No existe un registro con el ID {id_a_modificar}.")

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

    # Botón para modificar información
    boton_modificar = tk.Button(ventana, text="Modificar Registro", command=agregar_informacion)
    boton_modificar.grid(row=4, column=0, columnspan=2, pady=10)

    # Botón para buscar un registro
    boton_buscar = tk.Button(ventana, text="Buscar Registro", command=buscar_registro)
    boton_buscar.grid(row=5, column=0, columnspan=2, pady=10)

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

