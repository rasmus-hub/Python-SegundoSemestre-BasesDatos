# Se crean las sentencias de la bd

import sqlite3
from modelos import Libro

class AdministradorBaseDatos:
    def __init__(self, nombre_basedatos):
        self.conexion = sqlite3.connect(nombre_basedatos)
        self.crear_tabla()
    
    def crear_tabla(self):
        try:
            cursor = self.conexion.cursor()
            query = '''
                CREATE TABLE libros(
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                autor TEXT NOT NULL
                )
            '''
            cursor.execute(query)
        except Exception as e:
            print(f'Error al crear tabla: {e}')
        finally:
            cursor.close()
    
    def ingresar_libros(self, libro):
        try:
            cursor = self.conexion.cursor()
            query = '''
                    INSERT INTO libros(titulo,descripcion,autor)
                    VALUES (?,?,?)
            '''
            cursor.execute(query, (libro.titulo,libro.descripcion,libro.autor))
            self.conexion.commit()
        except Exception as e:
            print(f'Error al ingresar libro: {e}')
        finally:
            cursor.close()
    
    def ver_libros(self):
        try:
            cursor = self.conexion.cursor()
            query = 'SELECT * FROM libros'
            cursor.execute(query)
            libros = [Libro(id=fila[0],titulo=fila[1],descripcion=fila[2],autor=fila[3])
                      for fila in cursor.fetchall()]
        except Exception as e:
            print(f'Error al ver libros: {e}')
        finally:
            cursor.close()
            return libros
    
    def eliminar_libros(self, id_libro):
        try:
            cursor = self.conexion.cursor()
            query = f'''
                    DELETE
                    FROM libros
                    WHERE id = {id_libro}
            '''
            cursor.execute(query)
            self.conexion.commit()
        except Exception as e:
            print(f'Error al eliminar libro: {e}')
        finally:
            cursor.close()
