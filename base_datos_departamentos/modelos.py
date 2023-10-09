# Modelos de la bd

class Empleado:
    def __init__(self, id_empleado=None, nombre='', apellido='', email='', id_departamento=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.id_departamento = id_departamento
    
    def __str__(self):
        return (f'ID Empleado: {self.id_empleado} | Nombre: {self.nombre}'
                f' | Apellido: {self.apellido} | Email: {self.email} | ID Departamento: {self.id_departamento}')

class Departamento:
    def __init__(self, id_departamento=None, nombre='', ubicacion=''):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.ubicacion = ubicacion
    
    def __str__(self):
        return (f'ID Departamento: {self.id_departamento} | Nombre: {self.nombre} | Ubicación: {self.ubicacion}')
