import unittest
from unittest.mock import patch
from tema_musical import TemaMusical, EmptyError
from lista_musical import ListaMusical
from parameterized import parameterized

class TestMusical(unittest.TestCase):
    def setUp(self):
        self.t1 = TemaMusical('kJQP7kiw5Fk', 'Despacito', 281, 'Luis Fonzi')
        self.t2 = TemaMusical('fJ9rUzIMcZQ', 'Bohemian Rhapsody', 359, 'Queen')
        self.dict_modelo = {}
        self.dict_modelo[self.t1.codigo] = self.t1
        self.dict_modelo[self.t2.codigo] = self.t2

# la siguiente función testea que no se pueda asignar un código vacío a un
# objeto TemaMusical
    def test_tema_set_codigo_empty(self):
        tema = TemaMusical()
        with self.assertRaises(EmptyError):
            tema.codigo = ''


# la siguiente función testea que no se pueda asignar un nombre vacío a un
# objeto TemaMusical
    def test_tema_set_nombre_empty(self):
        tema = TemaMusical()
        with self.assertRaises(EmptyError):
            tema.nombre = ''


# la siguiente función testea que no se pueda asignar un valor negativo a
# la duracion de un objeto TemaMusical
    def test_tema_set_duracion_negativa(self):
        tema = TemaMusical()
        with self.assertRaises(ValueError):
            tema.duracion = -1


# la siguiente función testea que no se pueda asignar un valor vacío a un
# interprete de un objeto TemaMusical
    def test_tema_set_interprete_empty(self):
        tema = TemaMusical()
        with self.assertRaises(EmptyError):
            tema.interprete = ''


# la siguiente función testea que se le dé el formato requerido a la
# función __str__ del objeto TemaMusical
    @parameterized.expand([('kJQP7kiw5Fk', 'Despacito', 281, 'Luis Fonzi',
                            'codigo: kJQP7kiw5Fk\n\tnombre: Despacito' +
                            '\n\tduracion: 281\n\tinterprete: Luis Fonzi\n'),
                           ('fJ9rUzIMcZQ', 'Bohemian Rhapsody', 359, 'Queen',
                            'codigo: fJ9rUzIMcZQ\n\tnombre: Bohemian Rhap' +
                            'sody\n\tduracion: 359\n\tinterprete: Queen\n')])
    def test_tema_str(self, codigo, nombre, duracion, interprete, string):
        tema = TemaMusical(codigo, nombre, duracion, interprete)
        self.assertEqual(tema.__str__(), string)


# la siguiente función testea el funcionamiento correcto del método input
# incluyendo el código de un objeto TemaMusical
    @parameterized.expand([('kJQP7kiw5Fk', 'Despacito', 281, 'Luis Fonzi',
                            'codigo: kJQP7kiw5Fk\n\tnombre: Despacito' +
                            '\n\tduracion: 281\n\tinterprete: Luis Fonzi\n'),
                           ('fJ9rUzIMcZQ', 'Bohemian Rhapsody', 359, 'Queen',
                            'codigo: fJ9rUzIMcZQ\n\tnombre: Bohemian Rhap' +
                            'sody\n\tduracion: 359\n\tinterprete: Queen\n')])
    def test_tema_input_add(self, cod, nom, dur, inter, string):
        tema = TemaMusical()
        with patch('builtins.input', side_effect=(cod, nom, dur, inter)):
            tema.input()
            self.assertEqual(tema.__str__(), string)


# la siguiente función testea el funcionamiento correcto del método input
# sin incluir el código de un objeto TemaMusical. La exclusión del pedido
# del código se realiza por el parámetro True enviado a la función input()
    @parameterized.expand([('kJQP7kiw5Fk', 'Despacito', 281, 'Luis Fonzi',
                            'codigo: kJQP7kiw5Fk\n\tnombre: Despacito' +
                            '\n\tduracion: 281\n\tinterprete: Luis Fonzi\n'),
                           ('fJ9rUzIMcZQ', 'Bohemian Rhapsody', 359, 'Queen',
                            'codigo: fJ9rUzIMcZQ\n\tnombre: Bohemian Rhap' +
                            'sody\n\tduracion: 359\n\tinterprete: Queen\n')])
    def test_tema_input_update(self, cod, nom, dur, inter, string):
        tema = TemaMusical(cod)
        with patch('builtins.input', side_effect=(nom, dur, inter)):
            tema.input(True)
            self.assertEqual(tema.__str__(), string)


# la función add agrega un objeto TemaMusical a un objeto ListaMusical
    def test_lista_add_ok(self):
        lista = ListaMusical()
        lista.add(self.t1)
        lista.add(self.t2)
        self.assertDictEqual(lista.temas, self.dict_modelo)
    def test_lista_add_error(self):
        lista = ListaMusical()
        lista.add(self.t1)
        with self.assertRaises(KeyError):
            lista.add(self.t1)


# la función update modifica un objeto TemaMusical de un objeto ListaMusical
    def test_lista_update_ok(self):
        lista = ListaMusical()
        lista.add(TemaMusical(self.t1.codigo))
        lista.add(TemaMusical(self.t2.codigo))
        lista.update(self.t1, self.t1.codigo)
        lista.update(self.t2, self.t2.codigo)
        self.assertDictEqual(lista.temas, self.dict_modelo)
    def test_lista_update_error(self):
        lista = ListaMusical()
        lista.add(self.t1)
        with self.assertRaises(KeyError):
            lista.update(self.t2, self.t2.codigo)


# la función delete elimina del objeto ListaMusical un objeto TemaMusical
# según el id enviado
    def test_lista_delete_ok(self):
        lista = ListaMusical()
        lista.add(TemaMusical('newkey'))
        lista.add(self.t1)
        lista.add(self.t2)
        lista.delete('newkey')
        self.assertDictEqual(lista.temas, self.dict_modelo)
    def test_lista_delete_error(self):
        lista = ListaMusical()
        lista.add(self.t1)
        lista.add(self.t2)
        with self.assertRaises(KeyError):
            lista.delete('newkey')

# la funcion find_by_id devuelve un objeto TemaMusical del id indicado
    def test_lista_find_by_id_ok(self):
        lista = ListaMusical()
        lista.add(self.t1)
        lista.add(self.t2)
        self.assertEqual(lista.find_by_id(self.t1.codigo), self.t1)
    def test_lista_find_by_id_error(self):
        lista = ListaMusical()
        lista.add(self.t1)
        with self.assertRaises(KeyError):
            lista.find_by_id('newkey')


# la función find_all() devuelve una lista con todos los temas del objeto
# ListaMusical
    def test_lista_find_all(self):
        lista = ListaMusical()
        lista.add(self.t1)
        lista.add(self.t2)
        lista_test = []
        lista_test.append(self.t1)
        lista_test.append(self.t2)
        self.assertListEqual(lista.find_all(), lista_test)


if __name__ == '__main__':
    unittest.main()
