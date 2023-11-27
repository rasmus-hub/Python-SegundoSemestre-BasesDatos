import sqlite3

from conexion import Conexion

class Prestamo:
    def __init__(self, id, id_libro, id_usuario, fecha_prestamo):
        self.id = id
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.fecha_prestamo = fecha_prestamo
    
    @staticmethod
    def crear_tabla():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('''
            CREATE TABLE IF NOT EXISTS prestamos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_libro INTEGER NOT NULL,
                id_usuario INTEGER NOT NULL,
                fecha_prestamo TEXT NOT NULL,
                FOREIGN KEY (id_libro) REFERENCES
                    libros(id),
                FOREIGN KEY (id_usuario) REFERENCES
                    usuarios(id)
            );
            ''')
            conn.conn.commit()
            print('Tabla de prestamos creada correctamente')
        except sqlite3.Error as e:
            print(f'Error al crear tabla de prestamos: {e}')
        finally:
            conn.cerrar_conexion()
    
    def guardar(self):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('INSERT INTO prestamos (id_libro, id_usuario, fecha_prestamo) VALUES (?, ?, ?)', 
                      (self.id_libro, self.id_usuario, self.fecha_prestamo))
            conn.conn.commit()
            print('Datos correctamente insertados')
        except sqlite3.Error as e:
            print(f'Error al insertar datos en prestamos: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def obtener_prestamos():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('SELECT * FROM prestamos')
            usuarios = []
            for fila in c.fetchall():
                usuarios.append(fila)
            return usuarios
        except sqlite3.Error as e:
            print(f'Error al obtener los prestamos: {e}')
        finally:
            conn.cerrar_conexion()
    
    def actualizar(self, id_prestamo):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('UPDATE prestamos SET id_libro=?, id_usuario=?, fecha_prestamo=? WHERE id=?', 
                      (self.id_libro, self.id_usuario, self.fecha_prestamo, id_prestamo))
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al actualizar datos de prestamos: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def eliminar(id_prestamo):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('DELETE FROM prestamos WHERE id=?', id_prestamo)
            conn.conn.commit()
            print('Prestamo eliminado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al eliminar dato de prestamos: {e}')
        finally:
            conn.cerrar_conexion()