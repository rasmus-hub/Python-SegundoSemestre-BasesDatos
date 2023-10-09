# Se crean los metodos para recorrer la bd

import sqlite3
from modelos import Empleado
from modelos import Departamento

class AdministradorBaseDatos:
    def __init__(self, nombre_basedatos):
        self.conexion = sqlite3.connect(nombre_basedatos)
        self.crear_tabla_departamento()
        self.crear_tabla_empleado()
    
    def crear_tabla_empleado(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute( '''
                    CREATE TABLE IF NOT EXISTS empleados(
                    id_empleado INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT NOT NULL,
                    id_departamento INTEGER NOT NULL,
                    FOREIGN KEY (id_departamento) REFERENCES
                        departamentos(id_departamento)
                    )
            ''')
        except Exception as e:
            print(f'Error al crear tabla: {e}')
        finally:
            cursor.close()
    
    def crear_tabla_departamento(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute( '''
                    CREATE TABLE IF NOT EXISTS departamentos(
                    id_departamento INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    ubicacion TEXT NOT NULL
                    )
            ''')
        except Exception as e:
            print(f'Error al crear tabla: {e}')
        finally:
            cursor.close()

    def insertar_datos(self, tabla, dato):
        try:
            cursor = self.conexion.cursor()
            if tabla == 1:
                cursor.execute(( '''
                        INSERT INTO empleados(nombre,apellido,email,id_departamento)
                        VALUES(?,?,?,?)
                '''),(dato.nombre,dato.apellido,dato.email,dato.id_departamento))
            elif tabla == 2:
                cursor.execute(( '''
                        INSERT INTO departamentos(nombre,ubicacion)
                        VALUES(?,?)
                '''),(dato.nombre,dato.ubicacion))
            self.conexion.commit()
        except Exception as e:
            print(f'Error al insertar datos: {e}')
        finally:
            cursor.close()
    
    def ver_datos(self, tabla):
        try:
            cursor = self.conexion.cursor()
            if tabla == 1:
                cursor.execute('SELECT * FROM empleados')
                empleados = [Empleado(id_empleado=fila[0],nombre=fila[1],apellido=fila[2],
                            email=fila[3],id_departamento=fila[4])
                            for fila in cursor.fetchall()]
            elif tabla == 2:
                cursor.execute('SELECT * FROM departamentos')
                departamentos = [Departamento(id_departamento=fila[0],nombre=fila[1],
                                ubicacion=fila[2])
                                for fila in cursor.fetchall()]
            elif tabla == 3:
                cursor.execute('''
                        SELECT * FROM empleados INNER 
                        JOIN departamentos ON empleados.id_departamento = 
                        departamentos.id_departamento
                ''')
                datos = cursor.fetchall()
        except Exception as e:
            print(f'Error al ver tabla: {e}')
        finally:
            cursor.close()
            if tabla == 1:
                return empleados
            elif tabla == 2:
                return departamentos
            elif tabla == 3:
                return datos
    
    def eliminar_datos(self, tabla, id):
        try:
            cursor = self.conexion.cursor()
            if tabla == 1:
                cursor.execute(f'''
                        DELETE FROM empleados
                        WHERE id_empleado = {id}
                ''')
            elif tabla == 2:
                cursor.execute(f'''
                        DELETE FROM departamentos
                        WHERE id_departamento = {id}
                ''')
            self.conexion.commit()
        except Exception as e:
            print(f'Error al eliminar dato: {e}')
        finally:
            cursor.close()
        
    def cerrar_conexion(self):
        self.conexion.close()
            