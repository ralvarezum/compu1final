class ListaMusical():
    def __init__(self):
        self.temas = {}

    @property
    def temas(self):
        return self._temas

    @temas.setter
    def temas(self, entrada):
        self._temas = entrada

    def add(self, tema):
        if tema.codigo in self.temas:
            raise KeyError('ERROR: El codigo debe ser nuevo')
        self.temas[tema.codigo] = tema

    def update(self, tema, id):
        if id not in self.temas:
            raise KeyError('ERROR: La id no existe')
        self.temas[id] = tema

    def delete(self, id):
        if id not in self.temas:
            raise KeyError('ERROR: La id no existe')
        del self.temas[id]

    def find_by_id(self, id):
        if id not in self.temas:
            raise KeyError('Error: La id no existe')
        return self.temas[id]

    def find_all(self):
        list = []
        for tema in self.temas.values():
            list.append(tema)
        return list





