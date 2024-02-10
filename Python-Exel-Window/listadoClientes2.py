import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter.font as tkFont

def mostrar_excel_tabla():
    archivo_excel = "db.xlsx"
    try:
        df = pd.read_excel(archivo_excel)

        ventana_tabla = tk.Toplevel()
        ventana_tabla.title("Tabla de Datos desde Excel")

        tree = ttk.Treeview(ventana_tabla)
        tree["columns"] = ("",) + tuple(df.columns)
        tree.heading("", text="")
        tree.column("", width=10)

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=tkFont.Font().measure(col))

        for idx, row in df.iterrows():
            formatted_row = [f'{val:.2f}' if isinstance(val, (float)) else val for val in row]
            tree.insert("", "end", iid=idx, values=("",) + tuple(formatted_row))
            for i, item in enumerate(formatted_row):
                col_width = tkFont.Font().measure(str(item))
                if tree.column(df.columns[i], width=None) < col_width:
                    tree.column(df.columns[i], width=col_width)

        tree.pack(expand=True, fill="both")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def listado_clientes():
    mostrar_excel_tabla()

if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Mostrar Excel en Tabla")

    # Llamar a la función para mostrar la tabla
    listado_clientes()

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()
