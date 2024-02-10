#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter.font as tkFont

def mostrar_excel_tabla():
    
    archivo_excel = "db.xlsx"
    try:
        df = pd.read_excel(archivo_excel)

        # Limpiar cualquier widget en la ventana principal
        for widget in ventana.winfo_children():
            widget.destroy()

        # Crear un marco para contener el Treeview y la barra de desplazamiento
        marco = ttk.Frame(ventana)
        marco.pack(expand=True, fill="both")
        

        # Crear una barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(marco, orient="vertical")

        # Crear el Treeview con la barra de desplazamiento vertical
        tree = ttk.Treeview(marco, columns=tuple(df.columns), yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=tkFont.Font().measure(col))

        for idx, row in df.iterrows():
            formatted_row = [f'{val:.2f}' if isinstance(val, (float)) else val for val in row]
            tree.insert("", "end", iid=idx, values=tuple(formatted_row))
            for i, item in enumerate(formatted_row):
                col_width = tkFont.Font().measure(str(item))
                if tree.column(df.columns[i], width=None) < col_width:
                    tree.column(df.columns[i], width=col_width)

        # Ubicar la barra de desplazamiento en el lado derecho y configurar el tamaño del árbol
        scrollbar.pack(side="right", fill="y")
        tree.pack(expand=True, fill="both")

    except FileNotFoundError:
        print("Archivo no encontrado.")

def listado_clientes():
    mostrar_excel_tabla()

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Mostrar Excel en Tabla")

    # Obtener el tamaño de la pantalla y posicionar la ventana en el centro
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 800
    alto_ventana = 400
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Llamar a la función para mostrar la tabla
    listado_clientes()

    # Mostrar la ventana principal
    ventana.mainloop()
