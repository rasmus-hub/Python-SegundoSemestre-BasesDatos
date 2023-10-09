# Se definen instrucciones para hacer cambios en la db

from db_manager import AdministradorBaseDatos
from modelos import Libro

def main():
    base_datos = AdministradorBaseDatos('libros.db')
    
    #Menu de la bd
    opcion = None
    while opcion != 4:
        opcion = int(input('[ Menú Base de Datos ]'
                           '\n[1] Insertar libros'
                           '\n[2] Ver libros'
                           '\n[3] Eliminar libros'
                           '\n[4] Salir'
                           '\nIngrese una opción: '))
        
        match opcion:
            case 1:
                titulo = input('Ingrese el titulo: ')
                descripcion = input('Ingrese la descripcion: ')
                autor = input('Ingrese el autor: ')
                libro = Libro(titulo=titulo,descripcion=descripcion,autor=autor)
                base_datos.ingresar_libros(libro)
            case 2:
                libros = base_datos.ver_libros()
                for libro in libros:
                    print(libro)
            case 3:
                id_libro = int(input('Ingrese la id del libro: '))
                base_datos.eliminar_libros(id_libro)
            case _:
                if opcion != 4:
                    print('Opción inválida')
        print('-----------------------------------------------')


if __name__ == '__main__':
    main()
