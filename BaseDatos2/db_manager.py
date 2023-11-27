# Recorrer la bd

import sqlite3
from modelos import Cliente, Productos, Pedido


class AdministradorBaseDatos:
    def __init__(self, nombre_basedatos):
        self.conexion = sqlite3.connect(nombre_basedatos)
        self.crear_tablas()

    def crear_tablas(self):
        try:
            c = self.conexion.cursor()
            c.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL
            )''')
            c.execute('''
            CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio INTEGER NOT NULL
            )''')
            c.execute('''
            CREATE TABLE IF NOT EXISTS pedidos(
                id INTEGER PRIMARY KEY,
                cliente_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES
                    clientes(id)
            )''')
            c.execute('''
            CREATE TABLE IF NOT EXISTS pedidos_productos(
                pedido_id INTEGER,
                producto_id INTEGER,
                cantidad INTEGER,
                FOREIGN KEY (pedido_id) REFERENCES
                    pedidos(id),
                FOREIGN KEY (producto_id) REFERENCES
                    productos(id),
                PRIMARY KEY (pedido_id, producto_id)
            )''')
        except Exception as e:
            print(f'Error al crear tablas: {e}')
        finally:
            c.close()

    def insertar_ClientesProductos(self, tabla, dato):
        c = self.conexion.cursor()
        try:
            if tabla == 1:
                c.execute(('''
                INSERT INTO clientes(nombre,direccion)
                VALUES (?,?)
                '''), (dato.nombre, dato.direccion))
            elif tabla == 2:
                c.execute(('''
                INSERT INTO productos(nombre,precio)
                VALUES (?,?)
                '''), (dato.nombre, dato.precio))
            self.conexion.commit()
        except Exception as e:
            print(f'Error al insertar dato: {e}')
        finally:
            c.close()

    def insertar_pedidos(self, pedido, cantidad=1):
        try:
            c = self.conexion.cursor()
            c.execute(('''
            INSERT INTO pedidos(cliente_id,fecha)
            VALUES (?,?)
            '''), (pedido.cliente_id, pedido.fecha))
            pedido_id = c.lastrowid # Obtiene el ID del pedido insertado
            #Insertar productos del pedido en la tabla pedidos_productos con la cantidad
            for producto in pedido.productos:  # Los pedidos que tiene mis productos
                c.execute(('''
                INSERT INTO pedidos_productos(pedido_id,producto_id,cantidad)
                VALUES (?,?,?)
                '''), (pedido_id, producto.id, cantidad))
            self.conexion.commit()
        except Exception as e:
            print(f'Error al insertar dato: {e}')
        finally:
            c.close()

    def ver_datos(self, tabla):
        c = self.conexion.cursor()
        try:
            if tabla == 1:
                c.execute('SELECT * FROM clientes')
                clientes = [Cliente(id=fila[0], nombre=fila[1], direccion=fila[2])
                            for fila in c.fetchall()]
            elif tabla == 2:
                c.execute('SELECT * FROM productos')
                productos = [Productos(id=fila[0], nombre=fila[1], precio=fila[2])
                             for fila in c.fetchall()]
            elif tabla == 3:
                c.execute('SELECT * FROM pedidos')
                pedidos = [Pedido(id=fila[0], cliente_id=fila[1], productos=fila[2], fecha=fila[3])
                           for fila in c.fetchall()]
        except Exception as e:
            print(f'Error al ver dato: {e}')
        finally:
            c.close()
            if tabla == 1:
                return clientes
            elif tabla == 2:
                return productos
            elif tabla == 3:
                return pedidos
