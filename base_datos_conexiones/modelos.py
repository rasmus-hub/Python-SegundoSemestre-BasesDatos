# Crear las tablas a incorporar en la bd

class Producto:
    def __init__(self, id=None, nombre='', precio=0, stock=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (f'ID Producto: {self.id} | Nombre: {self.nombre} | '
                f'Precio: {self.precio} | Stock: {self.precio}')
