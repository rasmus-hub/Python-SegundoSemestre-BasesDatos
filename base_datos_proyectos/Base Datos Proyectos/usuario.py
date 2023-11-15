import sqlite3

from conexion import Conexion


class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
    
    def __str__(self):
        return f'ID Usuario: {self.id} | Nombre: {self.nombre} | Email: {self.email}'


    @staticmethod  # No depende de atributos
    def crear_tabla():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            q = '''
                CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                );
                '''
            c.execute(q)
            conn.conn.commit()
            print('Tabla usuarios creada exitosamente')
        except sqlite3.Error as e:
            print(f'Error al crear tabla de usuarios: {e}')
        finally:
            conn.cerrar_conexion()

    def guardar(self):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('INSERT INTO usuarios (nombre, email) VALUES (?, ?)',
                      (self.nombre, self.email))
            conn.conn.commit()
            print('Usuario creado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al guardar el usuario: {e}')
        finally:
            conn.cerrar_conexion()

    @staticmethod
    def obtener_usuarios():
        usuarios = []
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('SELECT * FROM usuarios')
            usuarios = []
            for fila in c.fetchall():
                usuario = Usuario(fila[0], fila[1], fila[2])
                usuarios.append(usuario)
            return usuarios
        except sqlite3.Error as e:
            print(f'Error al obtener usuarios: {e}')
        finally:
            conn.cerrar_conexion()

    def actualizar(self, usuario_id):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('UPDATE usuarios SET nombre=?, email=? WHERE id=?',
                      (self.nombre, self.email, usuario_id))
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al actualizar usuario: {e}')
        finally:
            conn.cerrar_conexion()

    @staticmethod
    def eliminar(usuario_id):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('DELETE FROM usuarios WHERE id=?', usuario_id)
            conn.conn.commit()
            print('Usuario eliminado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al eliminar el usuario: {e}')
        finally:
            conn.cerrar_conexion()
