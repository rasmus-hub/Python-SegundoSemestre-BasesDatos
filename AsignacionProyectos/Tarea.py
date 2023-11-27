import sqlite3

from Conexion import Conexion
class Tarea:
    def __init__(self, descripcion, proyecto_id):
        self.descripcion = descripcion
        self.proyecto_id = proyecto_id

    @staticmethod
    def crear_tabla():
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descripcion TEXT NOT NULL,
                    proyecto_id INTEGER,
                    FOREIGN KEY (proyecto_id) REFERENCES proyectos (id)
                )
            ''')
            conexion.conexion.commit()
            print("Tabla creada exitosamente")
        except sqlite3.Error as error:
            print("Error al crear la tabla de tareas: ", error)
        finally:
            conexion.cerrarConexion()