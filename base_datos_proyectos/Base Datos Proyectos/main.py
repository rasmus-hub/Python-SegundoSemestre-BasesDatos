from conexion import Conexion
from usuario import Usuario
from proyecto import Proyecto
from tareas import Tarea

Usuario.crear_tabla()
Proyecto.crear_tabla()
Tarea.crear_tabla()

def main():

    op = None
    while op != 5:
        op = int(input('[ Menú Proyectos ]'
                       '\n[1] Ingresar datos'
                       '\n[2] Actualizar datos'
                       '\n[3] Eliminar datos'
                       '\n[4] Ver datos'
                       '\n[5] Salir'
                       '\nIngrese una opción: '))
        
        print('--------------------------------------------')

        match op:
            case 1:
                op2 = int(input('[1] Tareas'
                                '\n[2] Proyectos'
                                '\n[3] Usuarios'
                                '\nIngrese una opción: '))
                if op2 == 1:
                    nombre = input('Ingrese el nombre: ')
                    descripcion = input('Ingrese la descripción: ')
                    tarea = Tarea(None, nombre, descripcion)
                    Tarea.guardar(tarea)
                elif op2 == 2:
                    nombre = input('Ingrese el nombre: ')
                    fecha = input('Ingrese la fecha: ')
                    proyecto = Proyecto(None, nombre, fecha)
                    Proyecto.guardar(proyecto)
                elif op2 == 3:
                    nombre = input('Ingrese el nombre: ')
                    email = input('Ingrese el correo: ')
                    usuario = Usuario(None, nombre, email)
                    Usuario.guardar(usuario)
                else:
                    print('Opción Inválida...')
                
                print('--------------------------------------------')

            case 2:
                op2 = int(input('[1] Tareas'
                                '\n[2] Proyectos'
                                '\n[3] Usuarios'
                                '\nIngrese una opción: '))
                if op2 == 1:
                    nombre = input('Ingrese el nuevo nombre: ')
                    descripcion = input('Ingrese la nueva descripción: ')
                    tarea_id = int(input('Ingrese la ID de la tarea a actualizar: '))
                    tarea_actualizada = Tarea(None, nombre, descripcion)
                    tarea_actualizada.actualizar(tarea_id)
                elif op2 == 2:
                    nombre = input('Ingrese el nuevo nombre: ')
                    fecha = input('Ingrese la nueva fecha: ')
                    proyecto_id = int(input('Ingrese la ID del proyecto a actualizar: '))
                    proyecto_actualizado = Proyecto(None, nombre, fecha)
                    proyecto_actualizado.actualizar(proyecto_id)
                elif op2 == 3:
                    nombre = input('Ingrese el nuevo nombre: ')
                    email = input('Ingrese el nuevo correo: ')
                    usuario_id = int(input('Ingrese el ID del usuario a actualizar: '))
                    usuario_actualizado = Usuario(None, nombre, email)
                    usuario_actualizado.actualizar(usuario_id)
                else:
                    print('Opción Inválida...')
                
                print('--------------------------------------------')
                
            case 3:
                op2 = int(input('[1] Tareas'
                                '\n[2] Proyectos'
                                '\n[3] Usuarios'
                                '\nIngrese una opción: '))
                if op2 == 1:
                    tarea_id = input('Ingrese la ID de la tarea: ')
                    Tarea.eliminar(tarea_id)
                elif op2 == 2:
                    proyecto_id = input('Ingrese la ID del proyecto: ')
                    Proyecto.eliminar(proyecto_id)
                elif op2 == 3:
                    usuario_id = input('Ingrese la ID del usuario: ')
                    Usuario.eliminar(usuario_id)
                else:
                    print('Opción Inválida...')
                
                print('--------------------------------------------')

            case 4:
                print('[ Tareas ]')
                tareas = Tarea.obtener_tareas()
                for tarea in tareas:
                    print(tarea)
                print('--------------------------------------------')
                print('\n[ Proyectos ]')
                proyectos = Proyecto.obtener_proyectos()
                for proyecto in proyectos:
                    print(proyecto)
                print('--------------------------------------------')
                print('\n[ Usuarios ]')
                usuarios = Usuario.obtener_usuarios()
                for usuario in usuarios:
                    print(usuario)
                
                print('--------------------------------------------')


if __name__ == '__main__':
    main()
