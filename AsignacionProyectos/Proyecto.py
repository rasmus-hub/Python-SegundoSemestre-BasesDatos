import sqlite3

from Conexion import Conexion

class Proyecto:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id

    @staticmethod
    def crear_tabla():
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS proyectos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
                );
            ''')
            conexion.conexion.commit()
            print("Tabla de proyectos creada exitosamente")
        except sqlite3.Error as error:
            print("Error al crear la tabla de proyectos: ", error)
        finally:
            conexion.cerrarConexion()

    def guardar(self):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('INSERT INTO proyectos (nombre, usuario_id) VALUES (?, ?)',
                           (self.nombre, self.usuario_id))
            conexion.conexion.commit()
            print("Proyecto creado exitosamente.")
        except sqlite3.Error as error:
            print("Error al guardar el proyecto: ", error)
        finally:
            conexion.cerrarConexion()

    @staticmethod
    def obtener_proyectos():
        proyectos = []
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('SELECT * FROM proyectos')
            proyectos = cursor.fetchall()
        except sqlite3.Error as error:
            print("Error al obtener proyectos: ", error)
        finally:
            conexion.cerrarConexion()
        return proyectos
    def actualizar(self, proyecto_id):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('UPDATE proyectos SET nombre=?, usuario_id=?, WHERE id=?',
                           (self.nombre, self.usuario_id, proyecto_id))
            conexion.conexion.commit()
            print("Proyecto actualizado exitosamente")
        except sqlite3.Error as error:
            print("Error al actualizar el proyecto: ", error)
        finally:
            conexion.cerrarConexion()

    @staticmethod
    def eliminar(proyecto_id):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('DELETE FROM proyectos WHERE id=?', (proyecto_id))
            conexion.conexion.commit()
            print("Proyecto eliminado exitosamente")
        except sqlite3.Error as error:
            print("Error al eliminar el proyecto: ", error)
        finally:
            conexion.cerrarConexion()

