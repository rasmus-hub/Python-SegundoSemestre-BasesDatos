import sqlite3

class Conexion:
    def __init__(self, nombre_basedatos):
        self.conn = sqlite3.connect(nombre_basedatos)
        self.c = self.conn.cursor()
    
    def ejecutar_query(self, q):
        self.c.execute(q)
        self.conn.commit()
    
    def cerrar_conexion(self):
        self.conn.close()