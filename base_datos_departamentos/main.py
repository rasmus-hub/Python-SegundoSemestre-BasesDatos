# Ejecutar las instrucciones para construir la bd y manejarla

from db_manager import AdministradorBaseDatos
from modelos import Empleado
from modelos import Departamento

def main():
    base_datos = AdministradorBaseDatos('inventario.db')

    #Menu de la bd
    opcion = None
    while opcion != 4:
        opcion = int(input('[ Menú Base de Datos ]'
                           '\n[1] Insertar datos'
                           '\n[2] Ver datos'
                           '\n[3] Eliminar datos'
                           '\n[4] Salir'
                           '\nIngrese una opción: '))
        
        match opcion:
            case 1:
                opcion =int(input('[1] Empleados'
                                '\n[2] Departamentos'
                                '\nIngrese una opción: '))
                if opcion == 1:
                    nombre = input('Ingrese el nombre: ')
                    apellido = input('Ingrese el apellido: ')
                    email = input('Ingrese el email: ')
                    id_departamento = int(input('Ingrese el ID del departamento: '))
                    empleado = Empleado(nombre=nombre,apellido=apellido,
                                        email=email,id_departamento=id_departamento)
                    base_datos.insertar_datos(1,empleado)
                
                elif opcion == 2:
                    nombre = input('Ingrese el nombre: ')
                    ubicacion = input('Ingrese la ubicación: ')
                    departamento = Departamento(nombre=nombre,ubicacion=ubicacion)
                    base_datos.insertar_datos(2,departamento)
            case 2:
                print('[ Empleados ]')
                empleados = base_datos.ver_datos(1)
                for empleado in empleados:
                    print(empleado)
                
                print('-----------------------------------------------------------------')

                print('[ Departamentos ]')
                departamentos = base_datos.ver_datos(2)
                for departamento in departamentos:
                    print(departamento)
                
                print('-----------------------------------------------------------------')

                print('[ Empleados y Departamentos ]')
                datos = base_datos.ver_datos(3)
                for dato in datos:
                    print(dato)
                
            case 3:
                opcion =int(input('[1] Empleados'
                                '\n[2] Departamentos'
                                '\nIngrese una opción: '))
                
                if opcion == 1:
                    id = int(input('Ingrese ID del empleado: '))
                    base_datos.eliminar_datos(1, id)
                elif opcion == 2:
                    id = int(input('Ingrese ID del departamento: '))
                    base_datos.eliminar_datos(2, id)
                
            case _:
                if opcion != 4:
                    print('Opción inválida')
        print('-----------------------------------------------------------------')


if __name__ == '__main__':
    main()