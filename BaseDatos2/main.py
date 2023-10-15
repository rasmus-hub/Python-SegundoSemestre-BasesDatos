from db_manager import AdministradorBaseDatos
from modelos import Cliente, Productos, Pedido


def main():
    base_datos = AdministradorBaseDatos('inventario.db')

    opcion = None
    while opcion != 4:
        opcion = int(input('[ Menú Pedidos ]'
                           f'\n[1] Insertar Datos'
                           f'\n[2] Ver Datos'
                           f'\n[3] Eliminar Datos'
                           f'\n[4] Salir'
                           f'\nIngrese una opción: '))

        print('\n-------------------------------------------------------------\n')

        match opcion:
            case 1:  # Insertar datos
                opcion = int(input('[1] Clientes'
                                   '\n[2] Productos'
                                   '\n[3] Pedidos'
                                   '\nIngrese una opción: '))
                if opcion == 1:
                    nombre = input('Ingrese el nombre: ')
                    direccion = input('Ingrese la dirección: ')
                    cliente = Cliente(nombre=nombre, direccion=direccion)
                    base_datos.insertar_ClientesProductos(1, cliente)

                elif opcion == 2:
                    nombre = input('Ingrese el nombre: ')
                    precio = input('Ingrese el precio: ')
                    producto = Productos(nombre=nombre, precio=precio)
                    base_datos.insertar_ClientesProductos(2, producto)

                elif opcion == 3:
                    cliente_id = int(input('Ingrese el ID del cliente: '))
                    fecha = input('Ingrese la fecha (DD/MM/YYYY): ')
                    cantidad = int(input('Cantidad productos a agregar: '))
                    pedido = Pedido(cliente_id=cliente_id, fecha=fecha)
                    base_datos.insertar_pedidos(pedido, cantidad=cantidad)

            case 2:  # Ver datos
                opcion = int(input('[1] Clientes'
                                   '\n[2] Productos'
                                   '\n[3] Pedidos'
                                   '\nIngrese una opción: '))

                if opcion == 1:
                    clientes = base_datos.ver_datos(1)
                    for cliente in clientes:
                        print(cliente)
                elif opcion == 2:
                    productos = base_datos.ver_datos(2)
                    for producto in productos:
                        print(producto)
                elif opcion == 3:
                    pedidos = base_datos.ver_datos(3)
                    for pedido in pedidos:
                        print(pedido)

        print('\n-------------------------------------------------------------\n')


if __name__ == '__main__':
    main()
