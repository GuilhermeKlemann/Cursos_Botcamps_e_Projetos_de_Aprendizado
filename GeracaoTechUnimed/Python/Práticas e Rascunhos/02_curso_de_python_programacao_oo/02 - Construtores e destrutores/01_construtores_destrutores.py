class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self): # __del__ é utilizado como método destrutor
        print("Removendo a instância da classe.")

    def latir(self):
        print("AUAUAU!")


def criar_cachorro():
    dog = Cachorro("Uni", "Caramelo", False)
    print(dog.nome)


dog = Cachorro("Bob", "Amarelo")
dog.latir()

print("Ola mundo")

del dog

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
