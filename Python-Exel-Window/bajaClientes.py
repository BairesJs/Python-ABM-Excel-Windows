#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import load_workbook

def eliminar_registro():
    def confirmar_eliminacion():
        # Obtener el ID a eliminar del usuario
        id_a_eliminar = int(entry_id_eliminar.get())
        ventana_eliminar.destroy()  # Cerrar la ventana después de eliminar

        # Leer el archivo Excel y verificar si el ID existe en el DataFrame
        try:
            df = pd.read_excel("db.xlsx")
            if id_a_eliminar in df['id'].values:
                # Eliminar la fila correspondiente al ID
                df.drop(df[df['id'] == id_a_eliminar].index, inplace=True)

                # Guardar el DataFrame actualizado en el archivo Excel
                with pd.ExcelWriter("db.xlsx", engine="openpyxl", mode="w") as writer:
                    df.to_excel(writer, index=False)

                messagebox.showinfo("Éxito", f"Registro con ID {id_a_eliminar} eliminado.")
            else:
                messagebox.showerror("Error", f"No existe un registro con el ID {id_a_eliminar}.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró la base de datos.")

    # Crear la ventana de eliminación
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Registro")

    
    ancho_pantalla = ventana_eliminar.winfo_screenwidth()
    alto_pantalla = ventana_eliminar.winfo_screenheight()

    # Definir el tamaño y posición de la ventana
    ancho_ventana = 400
    alto_ventana = 300

    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2

    ventana_eliminar.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    
    # Crear etiqueta y entrada para el ID a eliminar
    tk.Label(ventana_eliminar, text="ID a eliminar:").grid(row=0, column=0, padx=10, pady=5)
    entry_id_eliminar = tk.Entry(ventana_eliminar)
    entry_id_eliminar.grid(row=0, column=1, padx=10, pady=5)

    # Botón para confirmar la eliminación
    boton_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion)
    boton_confirmar.grid(row=1, column=0, columnspan=2, pady=10)
    
    # Ejecutar el bucle principal de la ventana de eliminación
    ventana_eliminar.mainloop()

# Llamar a la función para ejecutar la eliminación de registros

