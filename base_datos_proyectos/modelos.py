class Tareas:
    def __init__(self, id=None, nombre='', descripcion=''):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
    
    def __str__(self):
        return f'ID Tarea: {self.id} | Nombre: {self.nombre} | Descripción: {self.descripcion}'

class Usuarios:
    def __init__(self, id=None, proyectos=None, nombre='', direccion=''):
        self.id = id
        self.proyectos = proyectos if proyectos else []
        self.nombre = nombre
        self.direccion = direccion
    
    def __str__(self):
        proyectos_str = ' ,'.join([proyecto.nombre for proyecto in self.proyectos])
        return f'ID Usuario: {self.id} | Nombre: {self.nombre} | Dirección: {self.direccion} | Proyectos: {proyectos_str}'

class Proyectos:
    def __init__(self, id=None, tareas=None, nombre='', fecha=''):
        self.id = id
        self.tareas = tareas if tareas else []
        self.nombre = nombre
        self.fecha = fecha
    
    def __str__(self):
        tareas_str = ' ,'.join([tarea.nombre for tarea in self.tareas])
        return (f'ID Proyecto: {self.id} | Tareas: {tareas_str}'
                f'Nombre: {self.nombre} | Fecha: {self.fecha}')

class OperacionesBD:
    def __init__(self, conn):
        self.conn = conn

    def crear_tablas(self):
        try:
            self.conn.ejecutar_query('''
            CREATE TABLE IF NOT EXISTS tareas(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL
            )
            ''')
            self.conn.ejecutar_query('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL
            )
            ''')
            self.conn.ejecutar_query('''
            CREATE TABLE IF NOT EXISTS usuarios_proyectos(
                usuario_id INTEGER,
                proyecto_id INTEGER,
                FOREIGN KEY (usuario_id) REFERENCES
                    usuarios(id),
                FOREIGN KEY (proyecto_id) REFERENCES
                    proyectos(id),
                PRIMARY KEY (usuario_id, proyecto_id)
            )
            ''')
            self.conn.ejecutar_query('''
            CREATE TABLE IF NOT EXISTS proyectos(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                fecha TEXT NOT NULL
            )
            ''')
            self.conn.ejecutar_query('''
            CREATE TABLE IF NOT EXISTS proyectos_tareas(
                proyecto_id INTEGER,
                tarea_id INTEGER,
                FOREIGN KEY (proyecto_id) REFERENCES
                    proyectos(id),
                FOREIGN KEY (tarea_id) REFERENCES
                    tareas(id),
                PRIMARY KEY (proyecto_id, tarea_id)
            )
            ''')
        except Exception as e:
            print(f'Error al crear tabla: {e}')
    
    def insertar_tareas(self, tarea):
        try:
            self.conn.ejecutar_query(f'''
            INSERT INTO tareas(nombre, descripcion)
            VALUES ('{tarea.nombre}', '{tarea.descripcion}')''')
        except Exception as e:
            print(f'Error al insertar datos: {e}')
    
    def insertar_usuarios(self, usuario):
        try:
            self.conn.ejecutar_query(f'''
            INSERT INTO usuarios(nombre, direccion)
            VALUES ('{usuario.nombre}', '{usuario.direccion}')''')
            usuario_id = self.conn.c.lastrowid
            for proyecto in usuario.proyectos:
                self.conn.ejecutar_query(f'''
                INSERT INTO usuarios_proyectos(usuario_id, proyecto_id)
                VALUES ('{usuario_id}', '{proyecto.id}')''')
        except Exception as e:
            print(f'Error al insertar datos: {e}')
    
    def insertar_proyectos(self, proyecto):
        try:
            self.conn.ejecutar_query(f'''
            INSERT INTO proyectos(nombre, fecha)
            VALUES ('{proyecto.nombre}', '{proyecto.fecha}')''')
            proyecto_id = self.conn.c.lastrowid
            for tarea in proyecto.tareas:
                self.conn.ejecutar_query(f'''
                INSERT INTO proyectos_tareas(proyecto_id, tarea_id)
                VALUES ('{proyecto_id}', '{tarea.id}')''')
        except Exception as e:
            print(f'Error al insertar datos: {e}')
    
    def ver_datos(self):
        print('[ TAREAS ]')
        self.conn.ejecutar_query('SELECT * FROM tareas')
        tareas = []
        for fila in self.conn.c.fetchall():
            tarea = Tareas(fila[0], fila[1], fila[2])
            tareas.append(tarea)
        for tarea in tareas:
            print(tarea)
        
        print('-------------------------------------')

        print('[ USUARIOS ]')
        self.conn.ejecutar_query('SELECT * FROM usuarios')
        for fila in self.conn.c.fetchall():
            print(fila)
        
        print('-------------------------------------')
        
        print('[ PROYECTOS ]')
        self.conn.ejecutar_query('SELECT * FROM proyectos')
        for fila in self.conn.c.fetchall():
            print(fila)

    # Eliminar datos
