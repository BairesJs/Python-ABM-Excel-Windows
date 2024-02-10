#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from altaCliente2 import contenido_alta_cliente
from listadoClientes4 import mostrar_excel_tabla
from bajaClientes import eliminar_registro
from modificarClientes3 import contenido_editar_cliente


# Funciones para las opciones del menú
def alta_cliente():
    #messagebox.showinfo("Alta de Cliente", "Función de Alta de Cliente")
    contenido_alta_cliente()

def baja_cliente():
    #messagebox.showinfo("Baja de Cliente", "Función de Baja de Cliente")
    eliminar_registro()

def modificacion_cliente():
    #messagebox.showinfo("Modificación de Cliente", "Función de Modificación de Cliente")
    contenido_editar_cliente()

def lista_cliente():
    #messagebox.showinfo("Listado de Clientes", "Función de Listado de Clientes")
    mostrar_excel_tabla()

# Crear la ventana principal
ventana = tk.Tk()
#ventana.geometry("800x400")  # Por ejemplo, 400 píxeles de ancho y 300 píxeles de alto

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Definir el tamaño y posición de la ventana
ancho_ventana = 800
alto_ventana = 400

x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


ventana.title("Menú de Clientes")

# Crear un menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

# Crear un menú desplegable para las opciones de cliente
menu_cliente = tk.Menu(menu_principal)
menu_principal.add_cascade(label="Clientes", menu=menu_cliente)
menu_cliente.add_command(label="Alta", command=alta_cliente)
menu_cliente.add_command(label="Baja", command=baja_cliente)
menu_cliente.add_command(label="Modificación", command=modificacion_cliente)
menu_cliente.add_command(label="Listado", command=lista_cliente)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
