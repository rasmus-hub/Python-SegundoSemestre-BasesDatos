import sqlite3


class Conexion:
    def __init__(self, nombre_bd='proyectos.db'):
        self.nombre_bd = nombre_bd
        self.conn = None  # Objeto conexión

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nombre_bd)
            print('Conexión a la base de datos establecida')
        except sqlite3.Error as e:
            print(f'Error al conectar la base de datos: {e}')

    def cerrar_conexion(self):
        if self.conn:  # Si hay conexión, se cierra
            self.conn.close()
            print('Conexión a la base de datos cerrada.')
