from conexion import ConnectBD
import os
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import xlsxwriter
from PIL import ImageTk, Image  

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
            frame['background'] = '#2b3e50'
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

        menuBar = ttk.Label(self)
        menuBar['background'] = '#4e5d6c'
        menuBar.grid()

        path = "./assets/images/sgp_logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = ttk.Label(menuBar, image=img)
        panel['background'] = '#4e5d6c'
        panel.photo = img
        panel.grid(column=0, row=0, padx = 10, pady = 10)

        button1 = ttk.Button(menuBar, text ="Listar productos", bootstyle=DARK,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(menuBar, text ="Registrar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(menuBar, text ="Actualizar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(menuBar, text ="Eliminar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(menuBar, text ="Exportar en Excel", bootstyle=DARK,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(menuBar, text ="Salir", bootstyle=(DARK, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10, sticky=E)


class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        baseDatos = ConnectBD()
        tk.Frame.__init__(self, parent)
        producto = baseDatos.listarProductos()
        page_number = [0, 9]

        menuBar = ttk.Label(self)
        menuBar['background'] = '#4e5d6c'
        menuBar.grid()

        def pageNumber(self, page_number, producto, label_list):

            for lab in label_list:
                lab.destroy()

            page_ant = page_number[0] + 10
            page_post = page_number[1] + 10
            temp_page = [page_ant, page_post]
            page_number = temp_page
            list_product(self, producto, page_number)

        def pageNumberBack(self, page_number, producto, label_list):

            for lab in label_list:
                lab.destroy()

            page_ant = page_number[0] - 10
            page_post = page_number[1] - 10
            temp_page = [page_ant, page_post]
            page_number = temp_page
            list_product(self, producto, page_number)

        def list_product(self, producto, page_number):

            label_list = []

            if len(producto) > 9:

                if page_number[1] > 9:
                    cont = page_number[0]
                else:
                    cont = 1
                start = 0

                prodFrame = ttk.Label(self, bootstyle=PRIMARY)

                for prod in producto[page_number[0]:page_number[1]]:
                    datos = "[ {0} ] - Código: {1}  ||  Nombre: {2} (${3} pesos)"
                    label = ttk.Label(prodFrame, text=datos.format(cont, prod[0], prod[1], prod[2]), bootstyle = LIGHT)
                    label['background'] = '#32465a'
                    label_list.append(label)
                    label_list[start].grid(row = cont, column = 1, padx = 10, pady = 10)
                    start += 1
                    cont += 1
                
                prodFrame['background'] = '#32465a'
                prodFrame.grid(row=1, column = 0, padx = 20, pady = 20)
                label_list.append(prodFrame)
                

                buttonFrame = ttk.Label(self)
                buttonFrame['background'] = '#32465a'
                buttonFrame.grid(row=2, column = 0, padx = 20, pady = 20, sticky=S)

                buttonPaginateBack = ttk.Button(buttonFrame, text="Atras", command = lambda : pageNumberBack(self, page_number, producto, label_list))
                if page_number[0] == 0:
                    buttonPaginateBack['state'] = DISABLED
                buttonPaginateBack.grid(row = 0, column = 0, padx = 10, pady = 10)

                buttonPaginate = ttk.Button(buttonFrame, text ="Siguiente", command = lambda : pageNumber(self, page_number, producto, label_list))
                if page_number[1] > len(producto):
                    buttonPaginate['state'] = DISABLED
                buttonPaginate.grid(row = 0, column = 1, padx = 10, pady = 10)
  
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

        path = "./assets/images/sgp_logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = ttk.Label(menuBar, image=img)
        panel['background'] = '#4e5d6c'
        panel.photo = img
        panel.grid(column=0, row=0, padx = 10, pady = 10)

        button1 = ttk.Button(menuBar, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(menuBar, text ="Registrar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(menuBar, text ="Actualizar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(menuBar, text ="Eliminar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(menuBar, text ="Exportar en Excel", bootstyle=DARK,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(menuBar, text ="Salir", bootstyle=(DARK, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        baseDatos = ConnectBD()
        producto = baseDatos.listarProductos()

        menuBar = ttk.Label(self)
        menuBar['background'] = '#4e5d6c'
        menuBar.grid()

        def registrarProducto (self):

            registroFrame = ttk.Label(self, bootstyle=PRIMARY)
            registroFrame['background'] = '#32465a'
            registroFrame.grid(row=1, column = 0, padx = 20, pady = 20)

            codigoLabel = ttk.Label(registroFrame, text = "Ingrese el código del Producto:", bootstyle=LIGHT)
            codigoLabel['background'] = '#32465a'
            codigoLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            codigo = ttk.Entry(registroFrame, bootstyle=DARK)
            codigo.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            codigoError = ttk.Label(registroFrame, text = "El producto ingresado debe tener 6 caracteres", bootstyle=DANGER)
            codigoError['background'] = '#32465a'
            codigoErrorTwo = ttk.Label(registroFrame, text = "El codigo Ingresado ya está en uso", bootstyle=DANGER)
            codigoErrorTwo['background'] = '#32465a'

            nombreLabel = ttk.Label(registroFrame, text = "Ingrese nombre del producto:", bootstyle=LIGHT)
            nombreLabel['background'] = '#32465a'
            nombreLabel.grid(row = 5, columnspan = 2, padx = 10, pady = 10)
            nombre = ttk.Entry(registroFrame, bootstyle=DARK)
            nombre.grid(row = 6, columnspan = 2, padx = 10, pady = 10)
            nombreError = ttk.Label(registroFrame, text = "Debe ingresar un nombre.", bootstyle=DANGER)
            nombreError['background'] = '#32465a'

            precioLabel = ttk.Label(registroFrame, text = "Ingrese Precio:", bootstyle=LIGHT)
            precioLabel['background'] = '#32465a'
            precioLabel.grid(row = 8, columnspan = 2, padx = 10, pady = 10)
            precio = ttk.Entry(registroFrame, bootstyle=DARK)
            precio.grid(row = 9, columnspan = 2, padx = 10, pady = 10)
            precioError = ttk.Label(registroFrame, text = "El valor debe ser mayor a $0.", bootstyle=DANGER)
            precioError['background'] = '#32465a'

            buttonRegistrar = ttk.Button(registroFrame, text = "Registrar Producto", bootstyle=DARK, command = lambda : registrarProductoSend(self, codigo, nombre, precio, producto))
            buttonRegistrar.grid(row = 11, columnspan = 2, padx = 10, pady = 10)
            registroOk = ttk.Label(registroFrame, text = "El producto se registró satisfactoriamente!", bootstyle=SUCCESS)
            registroOk['background'] = '#32465a'

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

        path = "./assets/images/sgp_logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = ttk.Label(menuBar, image=img)
        panel['background'] = '#4e5d6c'
        panel.photo = img
        panel.grid(column=0, row=0, padx = 10, pady = 10)

        button1 = ttk.Button(menuBar, text ="Listar productos", bootstyle=DARK,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(menuBar, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(menuBar, text ="Actualizar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(menuBar, text ="Eliminar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(menuBar, text ="Exportar en Excel", bootstyle=DARK,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(menuBar, text ="Salir", bootstyle=(DARK, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuBar = ttk.Label(self)
        menuBar['background'] = '#4e5d6c'
        menuBar.grid()

        def actualizarProducto (self):

            baseDatos = ConnectBD()

            actualizarFrame = ttk.Label(self, bootstyle=PRIMARY)
            actualizarFrame['background'] = '#32465a'
            actualizarFrame.grid(row=1, column = 0, padx = 20, pady = 20)

            actualizarLabel = ttk.Label(actualizarFrame, text = "Ingrese código del producto a modificar:", bootstyle=LIGHT)
            actualizarLabel['background'] = '#32465a'
            actualizarLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            actualizarLabelEntry = ttk.Entry(actualizarFrame, bootstyle=DARK)
            actualizarLabelEntry.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            
            update_list = []

            buttonActualizarCheck = ttk.Button(actualizarFrame, text = "Buscar Producto", bootstyle=DARK, command = lambda : search(self, actualizarLabelEntry, update_list))
            buttonActualizarCheck.grid(row = 5, columnspan = 2, padx = 10, pady = 10)

            def search (self, actualizarLabelEntry, update_list):
                producto = baseDatos.listarProductos()
                clearUpdate (self, update_list)
                checkUpdate (self, actualizarLabelEntry, producto)

            def clearUpdate (self, update_list):
                for upd in update_list:
                    upd.destroy()

            def checkUpdate (self, actualizarLabelEntry, producto):
                codigoCheck = actualizarLabelEntry.get()
                codigoFound = False

                actualizarFrameResult = ttk.Label(self, bootstyle=PRIMARY)
                actualizarFrameResult['background'] = '#32465a'
                actualizarFrameResult.grid(row=2, column = 0, padx = 20, pady = 20)

                if codigoCheck != '':

                    for prod in producto:
                        if prod[0] == codigoCheck:
                            codigoFound = True
                            prodUpdate = (prod[0], prod[1], prod[2])
                    
                    newNameUpdate = prodUpdate[1]
                    newPrecioUpdate = prodUpdate[2]

                    nombreUpdate = (prodUpdate[1]) if codigoFound == True  else "None"
                    nameProductoAnterior = ttk.Label(actualizarFrameResult, text = "Nombre anterior: " + (nombreUpdate), bootstyle=LIGHT)
                    nameProductoAnterior['background'] = '#32465a'
                    update_list.append(nameProductoAnterior)
                    nameProductoAnterior.grid(row = 4, column = 4, padx = 10, pady = 10)

                    nameStyle = DARK
                    newName = ttk.Entry(actualizarFrameResult, bootstyle=(nameStyle))
                    update_list.append(newName)
                    newName.grid(row = 5, column = 4, padx = 10, pady = 10)

                    precioUpdate = str(prodUpdate[2]) if codigoFound == True else "None"
                    precioProductoAnterior = ttk.Label(actualizarFrameResult, text = "Precio anterior: " + (precioUpdate), bootstyle=LIGHT)
                    precioProductoAnterior['background'] = '#32465a'
                    update_list.append(precioProductoAnterior)
                    precioProductoAnterior.grid(row = 6, column = 4, padx = 10, pady = 10)

                    precioStyle = DARK
                    newPrecio = ttk.Entry(actualizarFrameResult, bootstyle=(precioStyle))
                    update_list.append(newPrecio)
                    newPrecio.grid(row = 7, column = 4, padx = 10, pady = 10)

                    style = LIGHT if codigoFound == True else DANGER
                    textAlert = "Se encontró el producto" if codigoFound == True else "El producto seleccionado no existe"

                    actualizarLabelInfo = ttk.Label(self, text = (textAlert), bootstyle=(style))
                    actualizarLabelInfo['background'] = '#2b3e50'
                    update_list.append(actualizarLabelInfo)
                    actualizarLabelInfo.grid(row = 6, columnspan = 2, padx = 10, pady = 10)

                    def updateGo(self, codigo, newName, newNameUpdate, newPrecio, newPrecioUpdate):

                        n = newName.get()
                        p = newPrecio.get()

                        print(newNameUpdate)
                        print(n)
                        print(newPrecioUpdate)
                        print(p)

                        nombreOk = False
                        if n == "":
                            nameStyle = DANGER
                            n == newNameUpdate
                        else:
                            nameStyle = SUCCESS
                            nombreOk = True

                        if p != '':
                            newPrecioUpdate = float(p.replace(",", "."))

                            precioOk = False
                            if newPrecioUpdate > 0:
                                precioStyle = SUCCESS
                                precioOk = True
                            else:
                                precioStyle = DANGER

                        if nombreOk == True and precioOk == True:
                            productoUpdate = (codigo, n, newPrecioUpdate)
                            print(productoUpdate)
                            baseDatos.actualizarProducto(productoUpdate)
                            updateSuccess.grid(row = 10, column = 4, padx = 10, pady = 10)

                    updateButton = ttk.Button(actualizarFrameResult, text="Actualizar", command= lambda : updateGo(self, prodUpdate[0], newName, newNameUpdate, newPrecio, newPrecioUpdate), bootstyle=DARK)
                    update_list.append(updateButton)
                    updateButton.grid(row = 9, column = 4, padx = 10, pady = 10)

                    updateSuccess = ttk.Label(actualizarFrameResult, text = "El producto se registró Correctamente", bootstyle = SUCCESS)
                    update_list.append(updateSuccess)

        actualizarProducto(self)

        path = "./assets/images/sgp_logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = ttk.Label(menuBar, image=img)
        panel['background'] = '#4e5d6c'
        panel.photo = img
        panel.grid(column=0, row=0, padx = 10, pady = 10)
  
        button1 = ttk.Button(menuBar, text ="Listar productos", bootstyle=DARK,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(menuBar, text ="Registrar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(menuBar, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(menuBar, text ="Eliminar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(menuBar, text ="Exportar en Excel", bootstyle=DARK,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(menuBar, text ="Salir", bootstyle=(DARK, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuBar = ttk.Label(self)
        menuBar['background'] = '#4e5d6c'
        menuBar.grid()

        def eliminarProducto(self):
            baseDatos = ConnectBD()

            eliminarFrame = ttk.Label(self, bootstyle=PRIMARY)
            eliminarFrame['background'] = '#32465a'
            eliminarFrame.grid(row=1, column = 0, padx = 20, pady = 20)

            eliminarLabel = ttk.Label(eliminarFrame, text = "Ingrese código del producto a Eliminar:", bootstyle=LIGHT)
            eliminarLabel['background'] = '#32465a'
            eliminarLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            eliminarLabelEntry = ttk.Entry(eliminarFrame, bootstyle=DARK)
            eliminarLabelEntry.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            
            delete_list = []

            buttonActualizarCheck = ttk.Button(eliminarFrame, text = "Buscar Producto", bootstyle=DARK, command = lambda : searchDelete(self, eliminarLabelEntry, delete_list))
            buttonActualizarCheck.grid(row = 5, columnspan = 2, padx = 10, pady = 10)

            def searchDelete (self, eliminarLabelEntry, delete_list):
                producto = baseDatos.listarProductos()
                clearDelete (self, delete_list)
                checkDelete (self, eliminarLabelEntry, producto)

            def clearDelete (self, delete_list):
                for dlt in delete_list:
                    dlt.destroy()

            def checkDelete (self, eliminarLabelEntry, producto):
                codigoCheck = eliminarLabelEntry.get()
                codigoFound = False

                if codigoCheck != '':

                    for prod in producto:
                        if prod[0] == codigoCheck:
                            codigoFound = True
                            prodDelete = (prod[0], prod[1], prod[2])

                    if codigoFound == True:

                        eliminarFrameResult = ttk.Label(self, bootstyle=PRIMARY)
                        eliminarFrameResult['background'] = '#32465a'
                        eliminarFrameResult.grid(row=2, column = 0, padx = 20, pady = 20)

                        labelProdDelete = ttk.Label(eliminarFrameResult, text = "Producto: " + (prodDelete[1]), bootstyle=LIGHT)
                        labelProdDelete['background'] = '#32465a'
                        labelProdDelete.grid(row = 2, column = 4, padx = 10, pady = 10)

                        labelPriceDelete = ttk.Label(eliminarFrameResult, text = "Precio: " + str(prodDelete[2]), bootstyle=LIGHT)
                        labelPriceDelete['background'] = '#32465a'
                        labelPriceDelete.grid(row = 3, column = 4, padx = 10, pady = 10)

                        deleteButton = ttk.Button(eliminarFrameResult, text = "Eliminar", command = lambda : deleteSelect(self, codigoCheck), bootstyle=DARK)
                        deleteButton.grid(row = 4, column = 4, padx = 10, pady = 10)

                        def deleteSelect(self, codigoCheck):
                            baseDatos.eliminarProducto(codigoCheck)
                            eliminarLabelInfo = ttk.Label(eliminarFrameResult, text = "El producto se eliminó correctamente", bootstyle=SUCCESS)
                            eliminarLabelInfo['background'] = '#32465a'
                            delete_list.append(eliminarLabelInfo)
                            eliminarLabelInfo.grid(row = 6, columnspan = 2, padx = 10, pady = 10)

        eliminarProducto(self)

        path = "./assets/images/sgp_logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = ttk.Label(menuBar, image=img)
        panel['background'] = '#4e5d6c'
        panel.photo = img
        panel.grid(column=0, row=0, padx = 10, pady = 10)

        button1 = ttk.Button(menuBar, text ="Listar productos", bootstyle=DARK,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(menuBar, text ="Registrar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)
 
        button3 = ttk.Button(menuBar, text ="Actualizar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(menuBar, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(menuBar, text ="Exportar en Excel", bootstyle=DARK,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(menuBar, text ="Salir", bootstyle=(DARK, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        baseDatos = ConnectBD()

        menuBar = ttk.Label(self)
        menuBar['background'] = '#4e5d6c'
        menuBar.grid()

        excelFrame = ttk.Label(self, bootstyle=LIGHT)
        excelFrame['background'] = '#32465a'
        excelFrame.grid(row=1, column = 0, padx = 20, pady = 20)

        excelFormatLabel = ttk.Label(excelFrame, text="Selecciona el Formato del Archivo: ", bootstyle=LIGHT)
        excelFormatLabel['background'] = '#32465a'
        excelFormatLabel.grid(row = 1, column = 0, padx = 10, pady = 10)

        excelFormat = ttk.Combobox(excelFrame, values = ('.csv', '.xlsx'), bootstyle=DARK)
        excelFormat.set(".csv")
        excelFormat.grid(row = 2, column = 0, padx = 10, pady = 10)

        nameFileLabel = ttk.Label(excelFrame, text = "Ingrese el nombre del Archivo: ", bootstyle=LIGHT)
        nameFileLabel['background'] = '#32465a'
        nameFileLabel.grid(row = 3, column = 0, padx = 10, pady = 10)
        nameFile = ttk.Entry(excelFrame, bootstyle=DARK)
        nameFile.grid(row = 4, column = 0, padx = 10, pady = 10)

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

        def makeExport(self, excelFormat, nameFile):
            producto = baseDatos.listarProductos()
            name = nameFile.get()
            name = str(name)
            extension = excelFormat.get()
            if len(producto) > 0 and nameFile != '':
                nombreArchivo = name + str(extension)
                exportarDatosProducto(producto, nombreArchivo)
                os.system(nombreArchivo)

        exportButton = ttk.Button(excelFrame, text = "Exportar en Excel", command = lambda : makeExport(self, excelFormat, nameFile), bootstyle=DARK)
        exportButton.grid(row = 5, column = 0, padx = 10, pady = 10)

        path = "./assets/images/sgp_logo.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = ttk.Label(menuBar, image=img)
        panel['background'] = '#4e5d6c'
        panel.photo = img
        panel.grid(column=0, row=0, padx = 10, pady = 10)
        
        button1 = ttk.Button(menuBar, text ="Listar productos", bootstyle=DARK,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(menuBar, text ="Registrar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(menuBar, text ="Actualizar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(menuBar, text ="Eliminar producto", bootstyle=DARK,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(menuBar, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(menuBar, text ="Salir", bootstyle=(DARK, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

app = tkinterApp()

app.title("SGP - Sistema Gestion Productos")
app.iconbitmap("./assets/images/sgp.ico")            
app.geometry("%dx%d" % (825, 600))

app.mainloop()