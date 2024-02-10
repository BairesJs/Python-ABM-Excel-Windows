#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter.font as tkFont  # Importar tkinter.font

# Función para cargar y mostrar datos desde un archivo Excel en una tabla
def mostrar_excel_tabla():
    # Cargar el archivo Excel
    archivo_excel = "db.xlsx"  # Reemplaza con la ruta de tu archivo Excel
    try:
        # Leer el archivo Excel y cargarlo en un DataFrame
        df = pd.read_excel(archivo_excel)
        
        # Crear una ventana para mostrar la tabla
        ventana_tabla = tk.Toplevel()
        ventana_tabla.title("Tabla de Datos desde Excel")

        # Crear un Treeview
        tree = ttk.Treeview(ventana_tabla)
        tree["columns"] = ("",) + tuple(df.columns)  # Agregar una columna vacía al principio
        tree.heading("", text="")
        tree.column("", width=10)  # Ancho de la columna vacía

        for col in df.columns:
            tree.heading(col, text=col)
            # Ajustar el ancho de la columna (en este ejemplo, se ajusta al ancho del encabezado)
            tree.column(col, width=tkFont.Font().measure(col))

        # Insertar datos en la tabla
        for idx, row in df.iterrows():
            formatted_row = [f'{val:.2f}' if isinstance(val, (float)) else val for val in row]  # Formatear a 2 decimales
            tree.insert("", "end", iid=idx, values=("",) + tuple(formatted_row))
            # Ajustar el ancho de la columna basado en el contenido
            for i, item in enumerate(formatted_row):
                col_width = tkFont.Font().measure(str(item))
                if tree.column(df.columns[i], width=None) < col_width:
                    tree.column(df.columns[i], width=col_width)

        tree.pack(expand=True, fill="both")
    except FileNotFoundError:
        print("Archivo no encontrado.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Excel en Tabla")

# Crear un menú
menu = tk.Menu(ventana)
ventana.config(menu=menu)

# Crear un menú desplegable "Archivo"
archivo_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Mostrar Excel en Tabla", command=mostrar_excel_tabla)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
