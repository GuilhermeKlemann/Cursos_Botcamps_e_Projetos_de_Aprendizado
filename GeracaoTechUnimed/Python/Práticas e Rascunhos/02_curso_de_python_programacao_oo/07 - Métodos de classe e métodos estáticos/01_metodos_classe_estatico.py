class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # Método de Classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): # cls = self nos métodos de classe
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod # Método Estático
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1997, 11, 1, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
