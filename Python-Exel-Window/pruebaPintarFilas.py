#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox

# Ejemplo de datos
data = [
    ("Alice", "Smith", 25),
    ("Bob", "Johnson", 30),
    ("Charlie", "Brown", 35),
    # ... más datos ...
]

def apply_alternating_row_colors(tree):
    # Establecer colores alternantes para las filas
    style = Style()
    style.configure("Treeview", rowevenbackground='#f0f0ff', rowoddbackground='#ffffff')

def mostrar_tabla():
    # Crear ventana y Treeview
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title("Tabla de Datos")
    
    tree = ttk.Treeview(ventana_tabla, columns=("Nombre", "Apellido", "Edad"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Edad", text="Edad")
    
    # Aplicar estilos de filas alternantes
    apply_alternating_row_colors(tree)
    
    for i, (nombre, apellido, edad) in enumerate(data, start=1):
        tree.insert("", "end", iid=i, values=(nombre, apellido, edad))
    
    tree.pack(expand=True, fill="both")

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Ejemplo de Tabla con Filas Alternantes")
    
    boton_mostrar_tabla = tk.Button(ventana, text="Mostrar Tabla", command=mostrar_tabla)
    boton_mostrar_tabla.pack(pady=10)
    
    ventana.mainloop()
