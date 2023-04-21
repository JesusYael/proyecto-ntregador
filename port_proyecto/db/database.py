import sqlite3

def creartablaconsesionario():
    #abre la conexion y si no existe el archivo lo crea
    connection = sqlite3.connect("db/admivo.sqlite3")

    cursor = connection.cursor()

    consesionario = "CREATE TABLE consesionario(\
                    id_consesionario integer primary key AUTOINCREMENT,\
                    nombre varchar(50) NOT NULL,\
                    primer_ap varchar (50) NOT NULL,\
                    segundo_ap varchar (50),\
                    email varchar (50) NOT NULL,\
                    password varchar (32) NOT NULL\
                    );"

    productos = "create table productos(\
                sku text,\
                nombre_producto text,\
                unidad text);\
                "
    
    cursor.execute(consesionario)
    cursor.close()

def creartablachoferes():
    #abre la conexion y si no existe el archivo lo crea
    connection = sqlite3.connect("db/admivo.sqlite3")

    cursor = connection.cursor()
    
    choferes = "CREATE TABLE choferes(\
                id_chofer integer primary key AUTOINCREMENT,\
                id_consesionario int NOT NULL,\
                nombre varchar (50) NOT NULL,\
                primer_ap varchar(50),\
                segundo_ap varchar (50),\
                curp varchar (50) NOT NULL,\
                numero_licencia varchar(50) NOT NULL,\
                CONSTRAINT id_consesionario\
                FOREIGN KEY(id_consesionario)\
                REFERENCES consesionario(id_consesionario)\
                );\
                "
    cursor.execute(choferes)
    cursor.close()
#creartablaconsesionario()
#creartablachoferes()