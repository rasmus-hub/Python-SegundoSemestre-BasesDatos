# Ejecutamos las instrucciones para entrar a la bd

from db_manager import AdministradorBaseDatos
from modelos import Producto

def close_conexion(self):
        self.conexion.close()

def main():
    base_datos = AdministradorBaseDatos('inventario.db')

    opcion = None
    while opcion != 4:
        opcion = int(input('[ Menú Base de Datos ]'
                           '\n[1] Insertar productos'
                           '\n[2] Ver productos'
                           '\n[3] Eliminar productos'
                           '\n[4] Salir'
                           '\nIngrese una opción: '))
        
        match opcion:
            case 1:
                nombre = input('Ingrese el nombre: ')
                precio = int(input('Ingrese el precio: '))
                stock = int(input('Ingrese el stock: '))
                producto = Producto(nombre=nombre,precio=precio,stock=stock)
                base_datos.insertar_productos(producto)
            case 2:
                productos = base_datos.mostrar_productos()
                for producto in productos:
                    print(producto)
            case 3:
                id_producto = int(input('Ingrese id del producto: '))
                base_datos.eliminar_productos(id_producto)
            case _:
                if opcion != 4:
                    print('Opción inválida')
        print('-----------------------------------------------')


if __name__ == '__main__':
    main()