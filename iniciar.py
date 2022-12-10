from conexion import ConnectBD
import funciones
import os

def menu():
    print(" _   _ _   _   ___     ___   + - - - - - - - - - - - - - - - - - - - - +")
    print("| | | | \ | | / _ \   |_  |  |S i s t e m a   p a r a   c o m e r c i o|")
    print("| | | |  \| |/ /_\ \    | |  |            p r o d u c t o s            |")
    print("| | | | . ` ||  _  |    | |  |                    &                    |")
    print("| |_| | |\  || | | |/\__/ /  |              p r e c i o s              |")
    print(" \___/\_| \_/\_| |_/\____/   + - - - - - - - - - - - - - - - - - - - - +")
    print("")
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

menu()