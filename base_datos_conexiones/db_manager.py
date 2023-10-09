# Crear metodos para recorrer la db

import sqlite3
from modelos import Producto

class AdministradorBaseDatos:
    def __init__(self, nombre_basedatos):
        self.conexion = sqlite3.connect(nombre_basedatos)
        self.crear_tabla()
    
    def crear_tabla(self):
        try:
            cursor = self.conexion.cursor()
            query = '''
                CREATE TABLE productos(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio INTEGER NOT NULL,
                stock INTEGER NOT NULL
                )
            '''
            cursor.execute(query)
        except Exception as e:
            print(f'Error al crear tabla: {e}')
        finally:
            cursor.close()
    
    def insertar_productos(self, producto):
        try:
            cursor = self.conexion.cursor()
            query = '''
                    INSERT INTO productos(nombre,precio,stock)
                    VALUES (?,?,?)
            '''
            cursor.execute(query,(producto.nombre, producto.precio, producto.stock))
            self.conexion.commit()
        except Exception as e:
            print(f'Error al insertar datos: {e}')
        finally:
            cursor.close()
    
    def mostrar_productos(self):
        try:
            cursor = self.conexion.cursor()
            query = 'SELECT * FROM productos'
            cursor.execute(query)
            productos = [Producto(id=fila[0],nombre=fila[1],precio=fila[2],stock=fila[3])
                        for fila in cursor.fetchall()]
        except Exception as e:
            print(f'Error al mostrar productos: {e}')
        finally:
            cursor.close()
            return productos
    
    def eliminar_productos(self, id_producto):
        try:
            cursor = self.conexion.cursor()
            query = f'''
                    DELETE
                    FROM productos
                    WHERE id = {id_producto}
            '''
            cursor.execute(query)
            self.conexion.commit()
        except Exception as e:
            print(f'Error al eliminar producto: {e}')
        finally:
            cursor.close()
    def close_conexion(self):
        self.conexion.close()
