# TP Integrador

UNAJ - Programa para Comercio 

# Pasos para Ejecutar el programa

1. Instalar laragon o xampp para ejecutar el servidor para mysql
2. Instalar MYSQL Workbench
3. Crear en localhost, un schema nuevo llamado productos. Consecuentemente importar datos del sql adjunto "productos", a fín de crear las tablas necesarias para correr el programa.
4. Actualizar contraseña en conexion.py por la que se tenga en localhost
5. Instalar el gestor de paquetes de python pip // curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py - esto trae el archivo get-pip.py, ejecutarlo.
6. Instalar mysql connector //pip install mysql-connector-python
7. Instalar el entorno virtual // python3 -m venv env
8. En Windows ejecutar // source env/Scripts/activate - a fín de iniciar el entorno (env)
9. Ejecutar //python3 iniciar.py

//Importar datos desde excel 
-- pip install numpy -- pip install pandas

import pandas as pd

crear variable donde vamos a almacenar dicho archivo

datosExcel = pd.read_excel(r'ruta archivo', sheet_name'nombreHoja') --> puede ser un input que pida que se ingrese la ruta del archivo formato xslx
*agregar r antes de la ruta

simil a agregar registro, pero desde hay que recibir datos desde allí

 exportar + facil ... pip install XlsxWriter

 <<Instalar ttkbootstrap>>
python -m pip install ttkbootstrap
