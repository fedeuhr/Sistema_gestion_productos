from conexion import ConnectBD
from funciones import Funciones
import os
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        print(container)

        container['background'] = '#36464e'
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
  
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def close (self):
        self.destroy()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Startpage")

        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(SECONDARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        baseDatos = ConnectBD()
         
        tk.Frame.__init__(self, parent)
        producto = baseDatos.listarProductos()
        page_number = [0, 9]

        def pageNumber(self, page_number, producto, label_list):

            for lab in label_list:
                lab.destroy()

            print(label_list)
            page_ant = page_number[0] + 10
            page_post = page_number[1] + 10
            temp_page = [page_ant, page_post]
            page_number = temp_page
            print(list(page_number)) #quitar luego
            list_product(self, producto, page_number)

        def pageNumberBack(self, page_number, producto, label_list):

            for lab in label_list:
                lab.destroy()

            print(label_list)
            page_ant = page_number[0] - 10
            page_post = page_number[1] - 10
            temp_page = [page_ant, page_post]
            page_number = temp_page
            print(list(page_number)) #quitar luego
            list_product(self, producto, page_number)
        

        def list_product(self, producto, page_number):

            label_list = []

            if len(producto) > 9:

                if page_number[1] > 9:
                    cont = page_number[0]
                else:
                    cont = 1

                start = 0

                for prod in producto[page_number[0]:page_number[1]]:
                    datos = "{0} - Código: {1} | Nombre: {2} (${3} pesos)"
                    label = ttk.Label(self, text=datos.format(cont, prod[0], prod[1], prod[2]))
                    label_list.append(label)
                    label_list[start].grid(row = cont, columnspan = 4, padx = 10, pady = 10)
                    start += 1
                    cont += 1

                buttonPaginateBack = ttk.Button(self, text="Atras", command = lambda : pageNumberBack(self, page_number, producto, label_list))
                if page_number[0] == 0:
                    buttonPaginateBack['state'] = DISABLED
                buttonPaginateBack.grid(row = 4, column = 4, padx = 10, pady = 10)

                #buttonPaginate = ttk.Button(self, text ="Siguiente", command = lambda : pageNumber(1))
                buttonPaginate = ttk.Button(self, text ="Siguiente", command = lambda : pageNumber(self, page_number, producto, label_list))
                buttonPaginate.grid(row = 4, column = 5, padx = 10, pady = 10)

                
            elif len(producto) <= 9:
                cont = 1
                for prod in producto:
                    datos = "{0} - Código: {1} | Nombre: {2} (${3} pesos)"
                    label = ttk.Label(self, text=datos.format(cont, prod[0], prod[1], prod[2]))
                    label.grid(row = cont, columnspan = 4, padx = 10, pady = 10)
                    cont += 1

            else:
                label = ttk.Label(self, text="No hay productos para mostrar.")
                label.grid(row = 2, column = 4, padx = 10, pady = 10)


        list_product(self, producto, page_number)

        button1 = ttk.Button(self, text ="Listar productos", bootstyle=LIGHT,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(SECONDARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)

        baseDatos = ConnectBD()
        producto = baseDatos.listarProductos()

        def registrarProducto (self):

            codigoLabel = ttk.Label(self, text = "Ingrese el código del Producto:", bootstyle=PRIMARY)
            codigoLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            codigo = ttk.Entry(self, bootstyle=PRIMARY)
            codigo.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            codigoError = ttk.Label(self, text = "El producto ingresado debe tener 6 caracteres", bootstyle=DANGER)
            codigoErrorTwo = ttk.Label(self, text = "El codigo Ingresado ya está en uso", bootstyle=DANGER)

            nombreLabel = ttk.Label(self, text = "Ingrese nombre del producto:", bootstyle=PRIMARY)
            nombreLabel.grid(row = 5, columnspan = 2, padx = 10, pady = 10)
            nombre = ttk.Entry(self, bootstyle=PRIMARY)
            nombre.grid(row = 6, columnspan = 2, padx = 10, pady = 10)
            nombreError = ttk.Label(self, text = "Debe ingresar un nombre.", bootstyle=DANGER)

            precioLabel = ttk.Label(self, text = "Ingrese Precio:", bootstyle=PRIMARY)
            precioLabel.grid(row = 8, columnspan = 2, padx = 10, pady = 10)
            precio = ttk.Entry(self, bootstyle=PRIMARY)
            precio.grid(row = 9, columnspan = 2, padx = 10, pady = 10)
            precioError = ttk.Label(self, text = "El valor debe ser mayor a $0.", bootstyle=DANGER)

            buttonRegistrar = ttk.Button(self, text = "Registrar Producto", bootstyle=PRIMARY, command = lambda : registrarProductoSend(self, codigo, nombre, precio, producto))
            buttonRegistrar.grid(row = 11, columnspan = 2, padx = 10, pady = 10)
            registroOk = ttk.Label(self, text = "El producto se registró satisfactoriamente!", bootstyle=SUCCESS)

            def registrarProductoSend (self, codigo, nombre, precio, producto):
                
                cod = codigo.get()
                nom = nombre.get()
                pre = precio.get()

                if len(cod) != 6:
                    codigoError.grid(row = 4, columnspan = 2, padx = 10, pady = 10)
                else:
                    codigoOk = False
                    for prod in producto:
                        if prod[0] == cod:
                            codigoError.destroy()
                            codigoErrorTwo.grid(row = 4, columnspan = 2, padx = 10, pady = 10)
                        else:
                            codigoOk = True

                nombreOk = False
                if nom == "":
                    nombreError.grid(row = 7, columnspan = 2, padx = 10, pady = 10)
                else:
                    nombreOk = True

                pre = float(pre.replace(",", "."))
                precioOk = False
                if pre > 0:
                    precioOk = True
                else:
                    precioError.grid(row = 10, columnspan = 2, padx = 10, pady = 10)

                if codigoOk == True and nombreOk == True and precioOk == True:
                    producto = (cod, nom, pre)
                    baseDatos.registrarProducto(producto)
                    registroOk.grid(row = 12, columnspan = 2, padx = 10, pady = 10)
                            


        registrarProducto(self)

        button1 = ttk.Button(self, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=LIGHT,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 2, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 3, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 4, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(SECONDARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 5, padx = 10, pady = 10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 3")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)

        baseDatos = ConnectBD()
        producto = baseDatos.listarProductos()

        def actualizarProducto (self, producto):

            actualizarLabel = ttk.Label(self, text = "Ingrese código del producto a modificar:", bootstyle=PRIMARY)
            actualizarLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            actualizarLabelEntry = ttk.Entry(self, bootstyle=PRIMARY)
            actualizarLabelEntry.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            
            

            update_list = []

            buttonActualizarCheck = ttk.Button(self, text = "Buscar Producto", bootstyle=PRIMARY, command = lambda : search(self, actualizarLabelEntry, producto, update_list))
            buttonActualizarCheck.grid(row = 5, columnspan = 2, padx = 10, pady = 10)

            def search (self, actualizarLabelEntry, producto, update_list):
                clearUpdate (self, update_list)
                checkUpdate (self, actualizarLabelEntry, producto)

            def clearUpdate (self, update_list):
                for upd in update_list:
                    upd.destroy()

            def checkUpdate (self, actualizarLabelEntry, producto):

                codigoCheck = actualizarLabelEntry.get()

                codigoFound = False

                for prod in producto:
                    if prod[0] == codigoCheck:
                        codigoFound = True
                        prodUpdate = (prod[0], prod[1], prod[2])
                
                nombreUpdate = (prodUpdate[1]) if codigoFound == True  else "None"
                nameProductoAnterior = ttk.Label(self, text = "Nombre anterior: " + (nombreUpdate))
                update_list.append(nameProductoAnterior)
                nameProductoAnterior.grid(row = 4, column = 4, padx = 10, pady = 10)

                newName = ttk.Entry(self, bootstyle=SUCCESS)
                update_list.append(newName)
                newName.grid(row = 5, column = 4, padx = 10, pady = 10)

                precioUpdate = str(prodUpdate[2]) if codigoFound == True else "None"
                precioProductoAnterior = ttk.Label(self, text = "Precio anterior: " + (precioUpdate))
                update_list.append(precioProductoAnterior)
                precioProductoAnterior.grid(row = 6, column = 4, padx = 10, pady = 10)

                newPrecio = ttk.Entry(self, bootstyle=SUCCESS)
                update_list.append(newPrecio)
                newPrecio.grid(row = 7, column = 4, padx = 10, pady = 10)

                style = SUCCESS if codigoFound == True else DANGER
                textAlert = "Se encontró el producto" if codigoFound == True else "El producto seleccionado no existe"

                actualizarLabelInfo = ttk.Label(self, text = (textAlert), bootstyle=(style))
                update_list.append(actualizarLabelInfo)
                actualizarLabelInfo.grid(row = 6, columnspan = 2, padx = 10, pady = 10)


 

        actualizarProducto(self, producto)
  
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=LIGHT,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(SECONDARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

        """ if existeCodigo:
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
            producto = None """

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 4")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)
 
        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=LIGHT,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(SECONDARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 5")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=LIGHT,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(SECONDARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

def menu():

    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("- - - - - - - - - - - - - -  MENÚ PRINCIPAL  - - - - - - - - - - - - - -")
            print("1) Listar productos")
            print("2) Registrar producto")
            print("3) Actualizar producto")
            print("4) Eliminar producto")
            print("5) Exportar en Excel")
            print("6) Salir")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            opcion = int(input("--> Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("--> Opción incorrecta, ingrese nuevamente.")
            elif opcion == 6:
                continuar = False
                print("--> ¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    baseDatos = ConnectBD()

    if opcion == 1:
        producto = baseDatos.listarProductos()
        if len(producto) > 0:
            funciones.listarProductos(producto)
        else:
            print("--> No se encontraron Productos.")

    elif opcion == 2:
        producto = funciones.pedirDatosProducto()
        baseDatos.registrarProducto(producto)

    elif opcion == 3:
        producto = baseDatos.listarProductos()
        if len(producto) > 0:
            producto = funciones.pedirDatosActualizacion(producto)
            if producto:
                baseDatos.actualizarProducto(producto)
            else:
                print("--> Código de producto a actualizar no encontrado.\n")
        else:
            print("--> No se encontraron productos.")

    elif opcion == 4:
        producto = baseDatos.listarProductos()
        if len(producto) > 0:
            codigoEliminar = funciones.pedirDatosEliminacion(producto)
            if not(codigoEliminar == ""):
                baseDatos.eliminarProducto(codigoEliminar)
            else:
                print("--> Código de producto no encontrado.\n")
        else:
            print("--> No se encontraron productos.")

    elif opcion == 5:
        producto = baseDatos.listarProductos()

        if len(producto) > 0:
            inputArchivo = input("ingrese nombre de archivo: ")
            extension = ".xlsx"
            nombreArchivo = inputArchivo + extension
            funciones.exportarDatosProducto(producto, nombreArchivo)
            os.system(nombreArchivo)
        else:
            print("--> No se encontraron Productos.")
     
    else:
        print("--> Opción no válida.")

#menu()

app = tkinterApp()
app.mainloop()