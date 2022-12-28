#-- Funciones que vamos a utilizar --
import pandas as pd
import xlsxwriter
from tkinter import Tk, Label, Button, Frame, Entry

#-- Función correspondiente a la opción 1
class Funciones():

    def listarProductos(producto, frame_lista):

        contador = 1
        for prod in producto:
            datos = "{0} - Código: {1} | Nombre: {2} (${3} pesos)"
            prodTk = Label(frame_lista, text=datos.format(contador, prod[0], prod[1], prod[2]))
            prodTk.pack()
            contador = contador + 1
            

def listarProductos(producto):
    print("\nProductos: \n")
    contador = 1
    for prod in producto:
        datos = "{0} - Código: {1} | Nombre: {2} (${3} pesos)"
        print(datos.format(contador, prod[0], prod[1], prod[2]))
        contador = contador + 1
    print(" ")

#-- Función correspondiente a la opción 2
def pedirDatosProducto():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese código de barras: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("--> Código incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    precioCorrecto = False
    while(not precioCorrecto):
        precio = input("Ingrese precio: ")
        precio = float(precio.replace(",", "."))
        if precio:
            if (precio > 0):
                precioCorrecto = True
                precio = precio
            else:
                print("--> El precio debe ser mayor a 0.")
        else:
            print("--> Precio Incorrecto: Debe ser un número únicamente.")

    producto = (codigo, nombre, precio)
    return producto

#-- Función correspondiente a la opción 3
def pedirDatosActualizacion(producto):
    listarProductos(producto)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del Producto a editar: ")
    for prod in producto:
        if prod[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        editar = input("¿Desea editar el nombre? Y/N: ")
        editarNombre = False
        while(not editarNombre):
            if (editar.lower() == "y"):
                editarNombre = True
                nombre = input("Ingrese nuevo nombre: ")
            elif (editar.lower() == "n"):
                editarNombre = True
                nombre = prod[1]
            else:
                print("--> Ingrese Y o N")

        edPrecio = input("¿Desea editar el precio? Y/N: ")
        editarPrecio = False
        while(not editarPrecio):
            if (edPrecio.lower() == "n"):
                precio = prod[2]
                editarPrecio = True
            elif (edPrecio.lower() == "y"):
                precioCorrecto = False
                while(not precioCorrecto):
                    precio = input("Ingrese nuevo Precio: ")
                    precio = float(precio.replace(",", "."))
                    if precio:
                        if (precio > 0):
                            precioCorrecto = True
                            precio = precio
                        else:
                            print("--> El precio debe ser mayor a 0.")
                    else:
                        print("--> Precio Incorrecto: Debe ser un número únicamente.")
                editarPrecio = True
            else:
                print("--> Ingrese Y o N")
        
        producto = (codigoEditar, nombre, precio)
    else:
        producto = None
        
    return producto

#-- Función correspondiente a la opción 4
def pedirDatosEliminacion(producto):
    listarProductos(producto)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del producto a eliminar: ")
    for prod in producto:
        if prod[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

#-- Función correspondiente a la opción 5
def exportarDatosProducto(producto, nombreArchivo):
	workbook = xlsxwriter.Workbook(nombreArchivo)
	worksheet = workbook.add_worksheet()
	row = 0
	col = 0
	for prod in producto:
		for p in prod:
			worksheet.write(row, col, p)
			col += 1
		row += 1
		col = 0

	workbook.close()