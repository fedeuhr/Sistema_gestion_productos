from conexion import ConnectBD
from funciones import Funciones
import os
import tkinter as tk
from tkinter import ttk

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
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

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Startpage")

        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel",
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir",
        command = "")
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        baseDatos = ConnectBD()
         
        tk.Frame.__init__(self, parent)
        producto = baseDatos.listarProductos()
        page_number = [0, 9]

        def pageNumber(self, page_number, producto):
            page_ant = page_number[0] + 10
            page_post = page_number[1] + 10
            temp_page = [page_ant, page_post]
            page_number = temp_page
            print(list(page_number))
            list_product(self, producto, page_number)
            #self.tkraise()

        def list_product(self, producto, page_number):
            if len(producto) > 9:

                cont = 1

                for prod in producto[page_number[0]:page_number[1]]:
                    datos = "{0} - Código: {1} | Nombre: {2} (${3} pesos)"
                    label = ttk.Label(self, text=datos.format(cont, prod[0], prod[1], prod[2]))
                    label.grid(row = cont, columnspan = 4, padx = 10, pady = 10)
                    cont += 1

                #buttonPaginate = ttk.Button(self, text ="Siguiente", command = lambda : pageNumber(1))
                buttonPaginate = ttk.Button(self, text ="Siguiente", command = lambda : pageNumber(self, page_number, producto))
                buttonPaginate.grid(row = 4, column = 4, padx = 10, pady = 10)
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

        list_product(producto)

        button1 = ttk.Button(self, text ="Listar productos",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel",
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir",
        command = lambda : controller.show_frame(Page2))
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 2, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 3, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel",
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 4, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir",
        command = lambda : controller.show_frame(Page2))
        button6.grid(row = 0, column = 5, padx = 10, pady = 10)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 3")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel",
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir",
        command = lambda : controller.show_frame(Page2))
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 4")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel",
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir",
        command = lambda : controller.show_frame(Page2))
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 5")
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Listar productos",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel",
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir",
        command = lambda : controller.show_frame(Page2))
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