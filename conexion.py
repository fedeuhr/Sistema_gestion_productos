import mysql.connector
import os
import dotenv

class ConnectBD():

    dotenv.load_dotenv()

    def __init__(self):
        self.conexion = mysql.connector.connect(
                host=os.getenv('HOST'),
                port=os.getenv('PORT'),
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                db=os.getenv('DATABASE')
            )

    def registrarProducto(self, producto):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = "INSERT INTO producto (codigo, nombre, precio) VALUES ('{0}', '{1}', {2})"
            cursor.execute(sql.format(producto[0], producto[1], producto[2]))
            self.conexion.commit()
            print("¡Producto registrado!\n")

    def listarProductos(self):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM producto ORDER BY nombre ASC"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

    def actualizarProducto(self, producto):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = "UPDATE producto SET nombre = '{0}', precio = {1} WHERE codigo = '{2}'"
            cursor.execute(sql.format(producto[1], producto[2], producto[0]))
            self.conexion.commit()
            print("¡Producto actualizado!\n")

    def eliminarProducto(self, codigoProductoEliminar):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = "DELETE FROM producto WHERE codigo = '{0}'"
            cursor.execute(sql.format(codigoProductoEliminar))
            self.conexion.commit()
            print("¡Producto eliminado!\n")