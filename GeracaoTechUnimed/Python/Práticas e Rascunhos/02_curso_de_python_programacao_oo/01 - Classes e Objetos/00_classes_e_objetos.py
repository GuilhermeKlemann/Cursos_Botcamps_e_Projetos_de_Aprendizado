# Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. 
# Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("AUAUAU!")

    def dormir(self):
        self.acordado = False
        print("ZzZZzzzzzZZZZZZz...")


# Objeto
cachorro_1 = Cachorro("Uni", "caramelo", False)
cachorro_2 = Cachorro("Bob", "amarelo")

cachorro_1.latir()

print(cachorro_2.acordado)
cachorro_2.dormir()
print(cachorro_2.acordado)