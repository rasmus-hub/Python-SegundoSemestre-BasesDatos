import sqlite3

from Conexion import Conexion

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    @staticmethod
    def crear_tabla():
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            query = '''
                    CREATE TABLE IF NOT EXISTS usuarios(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE
                    );
                    '''
            cursor.execute(query)
            conexion.conexion.commit()
            print("Tabla usuarios creada exitosamente")
        except sqlite3.Error as error:
            print("Error al crear la tabla de usuarios: ", error)
        finally:
            conexion.cerrarConexion()

    def guardar(self):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, email) VALUES (?, ?)',
                           (self.nombre, self.email))
            conexion.conexion.commit()
            print("Usuario creado exitosamente")
        except sqlite3.Error as error:
            print("Error al guardar el usuario: ", error)
        finally:
            conexion.cerrarConexion()

    @staticmethod
    def obtener_usuarios():
        usuarios = []
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
        except sqlite3.Error as error:
            print("Error al obtener usuarios: ", error)
        finally:
            conexion.cerrarConexion()
        return usuarios

    def actualizar(self, usuario_id):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('UPDATE usuarios SET nombre=?, email=? WHERE id=?',
                           (self.nombre, self.email, usuario_id))
            conexion.conexion.commit()
            print("Usuario actualizado exitosamente")
        except sqlite3.Error as error:
            print("Error al actualizar el usuario: ", error)
        finally:
            conexion.cerrarConexion()

    @staticmethod
    def eliminar(usuario_id):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id=?', (usuario_id))
            conexion.conexion.commit()
            print("Usuario eliminado exitosamente")
        except sqlite3.Error as error:
            print("Error al eliminar el usuario: ", error)
        finally:
            conexion.cerrarConexion()
