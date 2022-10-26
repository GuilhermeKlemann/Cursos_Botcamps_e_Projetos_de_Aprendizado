class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # A @property é um decorator integrado à função property() em Python. Ela é usada para dar uma funcionalidade "especial" a certos métodos para fazer com que ajam como getters, setters ou deleters quando definimos as propriedades em uma classe.
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
