import sqlite3
class Conexion:
    def __init__(self, nombre_db='proyectos.db'):
        self.nombre_db = nombre_db
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.nombre_db)
            print("Conexion a la base de datos establecida")
        except sqlite3.Error as error:
            print("Error al conectar la base de datos: ", error)

    def cerrarConexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexion a la base de datos cerrada.")
