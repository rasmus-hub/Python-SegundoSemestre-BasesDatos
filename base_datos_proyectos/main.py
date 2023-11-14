from conexion import Conexion
from modelos import Tareas, Usuarios, Proyectos, OperacionesBD

def main():
    conn = Conexion('proyectos.db')

    op_datos = OperacionesBD(conn)

    op_datos.crear_tablas()

    tarea = Tareas(nombre='Tarea 1', descripcion='Hacer tarea')
    op_datos.insertar_tareas(tarea)

    proyecto = Proyectos(nombre='Proyecto 1', fecha='02/11/2004')
    op_datos.insertar_proyectos(proyecto)

    usuario = Usuarios(nombre='Gustavo', direccion='Calle 51, Los Valles')
    op_datos.insertar_usuarios(usuario)
    
    op_datos.ver_datos()

if __name__ == '__main__':
    main()