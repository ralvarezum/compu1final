class EmptyError(ValueError):
    pass

class TemaMusical():
    def __init__(self, codigo=' ', nombre=' ', duracion=0, interprete=' '):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, entrada):
        if entrada == '':
            raise EmptyError('ERROR. No se puede asignar un codigo vacio')
        self._codigo = entrada

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, entrada):
        if entrada == '':
            raise EmptyError('ERROR. No se puede asignar un nombre vacio')
        self._nombre = entrada

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, entrada):
        if entrada < 0:
            raise ValueError
        self._duracion = entrada

    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self, entrada):
        if entrada == '':
            raise EmptyError('ERROR. No se puede asignar un interprete vacio')
        self._interprete = entrada

    def __str__(self):
        string = ''
        string = string + 'codigo: ' + self.codigo
        string = string + '\n\tnombre: ' + self.nombre
        string = string + '\n\tduracion: ' + str(self.duracion)
        string = string + '\n\tinterprete: ' + self.interprete
        string = string + '\n'
        return string

    def input(self, estado=False):
        if estado == False:
            self.codigo = input('Ingrese codigo: ')
        self.nombre = input('Ingrese nombre: ')
        self.duracion = int(input('Ingrese duracion: '))
        self.interprete = input('Ingrese interprete: ')







