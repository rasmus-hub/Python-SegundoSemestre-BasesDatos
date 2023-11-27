import sqlite3

from conexion import Conexion

class Usuario:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
    
    @staticmethod
    def crear_tabla():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                ubicacion TEXT NOT NULL
            );
            ''')
            conn.conn.commit()
            print('Tabla de usuarios creada correctamente')
        except sqlite3.Error as e:
            print(f'Error al crear tabla de usuarios: {e}')
        finally:
            conn.cerrar_conexion()
    
    def guardar(self):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('INSERT INTO usuarios (nombre, ubicacion) VALUES (?, ?)', 
                      (self.nombre, self.ubicacion))
            conn.conn.commit()
            print('Datos correctamente insertados')
        except sqlite3.Error as e:
            print(f'Error al insertar datos en usuarios: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def obtener_usuarios():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('SELECT * FROM usuarios')
            usuarios = []
            for fila in c.fetchall():
                usuarios.append(fila)
            return usuarios
        except sqlite3.Error as e:
            print(f'Error al obtener los usuarios: {e}')
        finally:
            conn.cerrar_conexion()
    
    def actualizar(self, id_usuario):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('UPDATE usuarios SET nombre=?, ubicacion=? WHERE id=?', 
                      (self.nombre, self.ubicacion, id_usuario))
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al actualizar datos de usuarios: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def eliminar(id_usuario):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('DELETE FROM usuarios WHERE id=?', id_usuario)
            conn.conn.commit()
            print('Usuario eliminado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al eliminar dato de usuarios: {e}')
        finally:
            conn.cerrar_conexion()