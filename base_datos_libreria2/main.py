from conexion import Conexion
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

def main():
    Libro.crear_tabla()

    libro1 = Libro(None, 'Matias y sus 4 amigos', 'Gustavo Olivera', 1997)
    libro2 = Libro(None, 'Don Matias de la mancha', 'Gustavo Olivera', 1998)
    Libro.guardar(libro1)
    Libro.guardar(libro2)

    libros = Libro.obtener_libros()
    for libro in libros:
        print(libro)

    libro1_actualizado = Libro(None, 'Matias y sus 2 amigos', 'Gustavo Olivera', 2004)
    Libro.actualizar(libro1_actualizado, 1)

    libros = Libro.obtener_libros()
    for libro in libros:
        print(libro)

    Libro.eliminar('1')

    libros = Libro.obtener_libros()
    for libro in libros:
        print(libro)
    
    print('\n')

    Usuario.crear_tabla()

    usuario1 = Usuario(None, 'Bastian Riffo', 'Puerto Montt')
    usuario2 = Usuario(None, 'Matias Bastias', 'Puerto Montt')
    Usuario.guardar(usuario1)
    Usuario.guardar(usuario2)

    usuarios = Usuario.obtener_usuarios()
    for usuario in usuarios:
        print(usuario)

    usuario2_actualizado = Usuario(None, 'Gabriel Bastias', 'Osorno')
    Usuario.actualizar(usuario2_actualizado, 2)

    usuarios = Usuario.obtener_usuarios()
    for usuario in usuarios:
        print(usuario)
    
    Usuario.eliminar('1')

    usuarios = Usuario.obtener_usuarios()
    for usuario in usuarios:
        print(usuario)
    
    print('\n')

    Prestamo.crear_tabla()

    prestamo = Prestamo(id=None, id_libro=1, id_usuario=2, fecha_prestamo='02/11/2023')

    Prestamo.guardar(prestamo)

    prestamos = Prestamo.obtener_prestamos()
    for prestamo in prestamos:
        print(prestamo)


if __name__ == '__main__':

    main()