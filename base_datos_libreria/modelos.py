# Se crean los modelos de la base de datos

class Libro:
    def __init__(self, id=None, titulo='', descripcion='', autor=''):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.autor = autor
    
    def __str__(self):
        return (f'ID Libro: {self.id} | Titulo: {self.titulo}'
                f'| Descripción: {self.descripcion} | Autor: {self.autor}')