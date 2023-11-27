# Tablas de la bd
# muchos a muchos (n a n) (1, n)

class Cliente:
    def __init__(self, id=None, nombre='', direccion=''):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Dirección: {self.direccion}'


class Productos:
    def __init__(self, id=None, nombre='', precio=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Precio: {self.precio}'


class Pedido:
    def __init__(self, id=None, cliente_id=None, productos=None, cantidad=0, fecha=''):
        self.id = id
        self.cliente_id = cliente_id
        self.productos = productos if productos else []  # Si hay productos, asignar a productos, si es que no hay,
        # asignarlo a la lista
        self.cantidad = cantidad
        self.fecha = fecha

    def __str__(self):
        # Recorrer la lista de productos con producto destacando el nombre y a partir de comas
        productos_str = ', '.join([producto.nombre for producto in self.productos])
        return (f'Pedido: {self.id} | Cliente ID: {self.cliente_id}'
                f' | Productos: {productos_str} | Fecha: {self.fecha}')

# Relación composición
# pedidos_productos
