import sqlite3

from conexion import Conexion

class Libro:
    def __init__(self, id, titulo, autor, ano_publicacion):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
    
    @staticmethod
    def crear_tabla():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('''
            CREATE TABLE IF NOT EXISTS libros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacion INTEGER NOT NULL
            );
            ''')
            conn.conn.commit()
            print('Tabla de libros creada correctamente')
        except sqlite3.Error as e:
            print(f'Error al crear tabla de libros: {e}')
        finally:
            conn.cerrar_conexion()
    
    def guardar(self):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('INSERT INTO libros (titulo, autor, ano_publicacion) VALUES (?, ?, ?)', 
                      (self.titulo, self.autor, self.ano_publicacion))
            conn.conn.commit()
            print('Datos correctamente insertados')
        except sqlite3.Error as e:
            print(f'Error al insertar datos en libros: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def obtener_libros():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('SELECT * FROM libros')
            libros = []
            for fila in c.fetchall():
                libros.append(fila)
            return libros
        except sqlite3.Error as e:
            print(f'Error al obtener los libros: {e}')
        finally:
            conn.cerrar_conexion()
    
    def actualizar(self, id_libro):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('UPDATE libros SET titulo=?, autor=?, ano_publicacion=? WHERE id=?', 
                      (self.titulo, self.autor, self.ano_publicacion, id_libro))
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al actualizar datos de libros: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def eliminar(id_libro):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('DELETE FROM libros WHERE id=?', id_libro)
            conn.conn.commit()
            print('Libro eliminado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al eliminar dato de libros: {e}')
        finally:
            conn.cerrar_conexion()
