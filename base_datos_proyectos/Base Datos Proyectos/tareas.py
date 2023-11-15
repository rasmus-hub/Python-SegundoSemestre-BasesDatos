import sqlite3

from conexion import Conexion


class Tarea:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
    
    def __str__(self):
        return f'ID Tarea: {self.id} | Nombre: {self.nombre} | Descripción: {self.descripcion}'

    @staticmethod
    def crear_tabla():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            q = '''
            CREATE TABLE IF NOT EXISTS tareas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL
            )
            '''
            c.execute(q)
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al crear tabla de tareas: {e}')
        finally:
            conn.cerrar_conexion()

    def guardar(self):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('INSERT INTO tareas (nombre, descripcion) VALUES (?, ?)',
                      (self.nombre, self.descripcion))
            conn.conn.commit()
            print('Tarea creada exitosamente')
        except sqlite3.Error as e:
            print(f'Error al guardar la tarea: {e}')
        finally:
            conn.cerrar_conexion()

    @staticmethod
    def obtener_tareas():
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('SELECT* FROM tareas')
            tareas = []
            for fila in c.fetchall():
                tarea = Tarea(fila[0], fila[1], fila[2])
                tareas.append(tarea)
            return tareas
        except sqlite3.Error as e:
            print(f'Error al obtener las tareas: {e}')
        finally:
            conn.cerrar_conexion()
    
    def actualizar(self, tarea_id):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('UPDATE tareas SET nombre=?, descripcion=? WHERE id=?', 
                      (self.nombre, self.descripcion, tarea_id))
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al actualizar la tarea: {e}')
        finally:
            conn.cerrar_conexion()
    
    @staticmethod
    def eliminar(tarea_id):
        try:
            conn = Conexion()
            conn.conectar()
            c = conn.conn.cursor()
            c.execute('DELETE FROM tareas WHERE id=?', tarea_id)
            conn.conn.commit()
        except sqlite3.Error as e:
            print(f'Error al eliminar la tarea: {e}')
        finally:
            conn.cerrar_conexion()
