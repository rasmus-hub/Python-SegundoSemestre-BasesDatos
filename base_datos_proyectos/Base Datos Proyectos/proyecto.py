import sqlite3

from conexion import Conexion


class Proyecto:
    def __init__(self, id, nombre, fecha):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
    
    def __str__(self):
        return f'ID Proyecto: {self.id} | Nombre: {self.nombre} | Fecha: {self.fecha}'

    @staticmethod
    def crear_tabla():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            q = '''
            CREATE TABLE IF NOT EXISTS proyectos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha TEXT NOT NULL
            );
            '''
            c.execute(q)
            conn.conn.commit()
            print('Tabla de proyectos creada exitosamente')
        except sqlite3.Error as e:
            print(f'Error al crear tabla de proyectos: {e}')
        finally:
            conn.cerrar_conexion()

    def guardar(self):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('INSERT INTO proyectos (nombre, fecha) VALUES (?, ?)',
                      (self.nombre, self.fecha))
            conn.conn.commit()
            print('Proyecto creado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al guardar el proyecto: {e}')
        finally:
            conn.cerrar_conexion()

    @staticmethod
    def obtener_proyectos():
        proyectos = []
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('SELECT * FROM proyectos')
            proyectos = []
            for fila in c.fetchall():
                proyecto = Proyecto(fila[0], fila[1], fila[2])
                proyectos.append(proyecto)
            return proyectos
        except sqlite3.Error as e:
            print(f'Error al obtener proyectos: {e}')
        finally:
            conn.cerrar_conexion()

    def actualizar(self, proyecto_id):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('UPDATE proyectos SET nombre=?, fecha=? WHERE id=?',
                      (self.nombre, self.fecha, proyecto_id))
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al actualizar proyecto: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def eliminar(proyecto_id):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('DELETE FROM proyectos WHERE id=?', proyecto_id)
            conn.conn.commit()
            print('Proyecto eliminado exitosamente')
        except sqlite3.Error as e:
            print(f'Error al eliminar el proyecto: {e}')
