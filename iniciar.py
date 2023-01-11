from conexion import ConnectBD
from funciones import Funciones
import os
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import xlsxwriter

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
  
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(PRIMARY, OUTLINE),
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

                for prod in producto[page_number[0]:page_number[1]]:
                    datos = "{0} - Código: {1} | Nombre: {2} (${3} pesos)"
                    label = ttk.Label(self, text=datos.format(cont, prod[0], prod[1], prod[2]), bootstyle = LIGHT)
                    label['background'] = '#2b3e50'
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
                if page_number[1] > len(producto):
                    buttonPaginate['state'] = DISABLED
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

        button1 = ttk.Button(self, text ="Listar productos", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(PRIMARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

        button1 = ttk.Button(self, text ="Listar productos", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 2, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 3, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 4, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(PRIMARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 5, padx = 10, pady = 10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def actualizarProducto (self):

            baseDatos = ConnectBD()

            actualizarLabel = ttk.Label(self, text = "Ingrese código del producto a modificar:", bootstyle=PRIMARY)
            actualizarLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            actualizarLabelEntry = ttk.Entry(self, bootstyle=PRIMARY)
            actualizarLabelEntry.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            
            update_list = []

            buttonActualizarCheck = ttk.Button(self, text = "Buscar Producto", bootstyle=PRIMARY, command = lambda : search(self, actualizarLabelEntry, update_list))
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

                if codigoCheck != '':

                    for prod in producto:
                        if prod[0] == codigoCheck:
                            codigoFound = True
                            prodUpdate = (prod[0], prod[1], prod[2])
                    
                    newNameUpdate = prodUpdate[1]
                    newPrecioUpdate = prodUpdate[2]

                    nombreUpdate = (prodUpdate[1]) if codigoFound == True  else "None"
                    nameProductoAnterior = ttk.Label(self, text = "Nombre anterior: " + (nombreUpdate))
                    update_list.append(nameProductoAnterior)
                    nameProductoAnterior.grid(row = 4, column = 4, padx = 10, pady = 10)

                    nameStyle = SUCCESS
                    newName = ttk.Entry(self, bootstyle=(nameStyle))
                    update_list.append(newName)
                    newName.grid(row = 5, column = 4, padx = 10, pady = 10)

                    precioUpdate = str(prodUpdate[2]) if codigoFound == True else "None"
                    precioProductoAnterior = ttk.Label(self, text = "Precio anterior: " + (precioUpdate))
                    update_list.append(precioProductoAnterior)
                    precioProductoAnterior.grid(row = 6, column = 4, padx = 10, pady = 10)

                    precioStyle = SUCCESS
                    newPrecio = ttk.Entry(self, bootstyle=(precioStyle))
                    update_list.append(newPrecio)
                    newPrecio.grid(row = 7, column = 4, padx = 10, pady = 10)

                    style = SUCCESS if codigoFound == True else DANGER
                    textAlert = "Se encontró el producto" if codigoFound == True else "El producto seleccionado no existe"

                    actualizarLabelInfo = ttk.Label(self, text = (textAlert), bootstyle=(style))
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

                    updateButton = ttk.Button(self, text="Actualizar", command= lambda : updateGo(self, prodUpdate[0], newName, newNameUpdate, newPrecio, newPrecioUpdate))
                    update_list.append(updateButton)
                    updateButton.grid(row = 9, column = 4, padx = 10, pady = 10)

                    updateSuccess = ttk.Label(self, text = "El producto se registró Correctamente", bootstyle = SUCCESS)
                    update_list.append(updateSuccess)

        actualizarProducto(self)
  
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(PRIMARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def eliminarProducto(self):
            baseDatos = ConnectBD()

            eliminarLabel = ttk.Label(self, text = "Ingrese código del producto a Eliminar:", bootstyle=PRIMARY)
            eliminarLabel.grid(row = 2, columnspan = 2, padx = 10, pady = 10)
            eliminarLabelEntry = ttk.Entry(self, bootstyle=PRIMARY)
            eliminarLabelEntry.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
            
            delete_list = []

            buttonActualizarCheck = ttk.Button(self, text = "Buscar Producto", bootstyle=PRIMARY, command = lambda : searchDelete(self, eliminarLabelEntry, delete_list))
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

                        labelProdDelete = ttk.Label(self, text = "Producto: " + (prodDelete[1]))
                        labelProdDelete.grid(row = 2, column = 4, padx = 10, pady = 10)

                        labelPriceDelete = ttk.Label(self, text = "Precio: " + str(prodDelete[2]))
                        labelPriceDelete.grid(row = 3, column = 4, padx = 10, pady = 10)

                        deleteButton = ttk.Button(self, text = "Eliminar", command = lambda : deleteSelect(self, codigoCheck))
                        deleteButton.grid(row = 4, column = 4, padx = 10, pady = 10)

                        def deleteSelect(self, codigoCheck):
                            baseDatos.eliminarProducto(codigoCheck)
                            eliminarLabelInfo = ttk.Label(self, text = "El producto se eliminó correctamente", bootstyle=SUCCESS)
                            delete_list.append(eliminarLabelInfo)
                            eliminarLabelInfo.grid(row = 6, columnspan = 2, padx = 10, pady = 10)

        eliminarProducto(self)      

        button1 = ttk.Button(self, text ="Listar productos", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)
 
        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(PRIMARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        baseDatos = ConnectBD()

        excelFormat = ttk.Combobox(self, values = ('.csv', '.xlsx'), bootstyle = PRIMARY)
        excelFormat.set(".csv")
        excelFormat.grid(row = 3, column = 4, padx = 10, pady = 10)

        nameFileLabel = ttk.Label(self, text = "Ingrese el nombre del Archivo: ", bootstyle=PRIMARY)
        nameFileLabel.grid(row = 4, column = 4, padx = 10, pady = 10)
        nameFile = ttk.Entry(self, bootstyle=PRIMARY)
        nameFile.grid(row = 5, column = 4, padx = 10, pady = 10)

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
            else:
                print("--> No se encontraron Productos.")

  
        exportButton = ttk.Button(self, text = "Exportar en Excel", command = lambda : makeExport(self, excelFormat, nameFile))
        exportButton.grid(row = 2, column = 4, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text ="Listar productos", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Registrar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Actualizar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 0, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Eliminar producto", bootstyle=PRIMARY,
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 0, column = 4, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="Exportar en Excel", bootstyle=SECONDARY,
        command = lambda : controller.show_frame(Page5))
        button5.grid(row = 0, column = 5, padx = 10, pady = 10)

        button6 = ttk.Button(self, text ="Salir", bootstyle=(PRIMARY, OUTLINE),
        command = lambda : controller.close())
        button6.grid(row = 0, column = 6, padx = 10, pady = 10)

app = tkinterApp()
app.mainloop()